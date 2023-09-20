import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
import pickle
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

sys.path.append("/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL")
from Basic_model.utils import *
from Basic_model.cell import Cell


class PopulationArguments():
    """
    Arguments for controlling a population:
    - input_vector_size [int, required] : size of flattened input vector
    - output_vector_size [int, required] : size of flattened output vector
    - childs_per_parent [int, optional, default 50] : number of mutated children per parent when populating next generation
    - top_performers_count [int, optional, ]
    - eval_steps [int, optional, default 100] : Steps between doing evaluation on test set and store results
    - eval_info [bool, optional, default True] : Whether to print out eval accuracy every 5th evaluation
    - complexity_level [int, optional, default 10] : The initial complexity of the cell initialized at generation 0
    - data_evaluation_factor [float, [0, 1], optional, default 0.1] : factor of dataset to use for evaluation

    """
    def __init__(self, input_vector_size, output_vector_size, childs_per_parent = 50, top_performers_count = 25,
                eval_steps = 100, eval_info = True, complexity_level = 10, data_evaluation_factor = 0.1) -> None:
        self.input_vector_size = input_vector_size
        self.output_vector_size = output_vector_size
        self.childs_per_parent = childs_per_parent
        self.top_performers_count = top_performers_count
        self.eval_steps = eval_steps
        self.eval_info = eval_info
        self.complexity_level = complexity_level
        self.data_evaluation_factor = data_evaluation_factor

def evaluate_cell(cell, xs, ys):
    return cell.evaluate(xs, ys), cell

class Population():
    """
    Population
    - PopulationArgument [required] : PopulationArgument object
    
    """
    def __init__(self, PopulationArgument) -> None:
        self.set_arguments(PopulationArgument)
        self.generation = 0
        self.loss_history, self.accuracy_history, self.eval_history, self.cell_stats = [], [], [], []
        divider("\nInitiating Population...")
        self.population_size = (self.childs_per_parent + 1) * self.top_performers_count
        print(f"Creating {self.population_size} cells with complexity level {self.complexity_level}...")
        self.population = [Cell(complexity_level=self.complexity_level, input_vector_size=self.input_vector_size, output_vector_size=self.output_vector_size) for _ in tqdm(range(self.population_size))]
        tiny_divider()

    def set_arguments(self, arguments):
        self.input_vector_size = arguments.input_vector_size
        self.output_vector_size = arguments.output_vector_size
        self.childs_per_parent = arguments.childs_per_parent
        self.top_performers_count = arguments.top_performers_count
        self.eval_steps = arguments.eval_steps
        self.eval_info = arguments.eval_info
        self.complexity_level = arguments.complexity_level
        self.data_evaluation_factor = arguments.data_evaluation_factor

    def get_evaluation_set(self, xs):
        evaluation_set_size = len(xs) * self.data_evaluation_factor
        # still missing some
    
    def evaluate(self, xs, ys):
        with ThreadPoolExecutor(max_workers=4) as executor:
            losses = list(executor.map(lambda x: evaluate_cell(x, xs, ys), self.population))
        losses.sort(key = lambda x: x[0])
        top_performers = [x[1] for x in losses[:self.top_performers_count]]
        mean_top_performers_loss = np.mean([x[0] for x in losses[:self.top_performers_count]])
        self.loss_history.append(mean_top_performers_loss)
        self.top_performer = losses[0][1]
        self.accuracy_history.append(self.top_performer.accuracy(xs, ys))
        return top_performers

    def populate_next_generation(self, top_performers):
        parents = top_performers * (self.childs_per_parent + 1)
        children = [Cell(parent=parent) for parent in top_performers for _ in range(self.childs_per_parent)]
        self.population = parents + children

    def progress(self, x_train, y_train, x_test, y_test, generations = 1):
        tiny_divider(f"Evolving population:")
        for _ in tqdm(range(generations), desc = f"Simulating {generations} generations"):
            top_performers = self.evaluate(x_train, y_train)
            self.populate_next_generation(top_performers)
            self.generation += 1
            self.cell_stats.append(self.top_performer.get_stats())
            if self.generation % self.eval_steps == 0: 
                self.eval_history.append(self.top_performer.accuracy(x_test, y_test))
                if self.generation % (5 * self.eval_steps) == 0: 
                    # Make equally distanced 
                    tqdm.write(f"Generation {self.generation} | Eval accuracy: {round(self.eval_history[-1] * 100, 2)}% | Train accuracy: {round(self.accuracy_history[-1] * 100, 2)}%")
        divider(f"Final Eval Accuracy at generation {self.generation}: {round(self.top_performer.accuracy(x_test, y_test) * 100, 2)}%")

    def get_top_performers(self, xs, ys): return self.evaluate(xs, ys)

    def see_performance(self): 
        # Include eval accuracy
        x = list(range(1, self.generation + 1))
        fig, ax1 = plt.subplots(figsize=(8, 6))
        ax1.plot(x, self.loss_history, label='Loss', color='b', linewidth=2, marker='o', markersize=5)
        ax1.set_xlabel('Generation')
        ax1.set_ylabel('Loss')
        ax1.set_title('Top performers mean loss over generations')
        ax1.grid(True, linestyle='--', alpha=0.7)
        ax2 = ax1.twinx()
        ax2.set_ylabel('Accuracy', color='g')
        ax2.plot(x, self.accuracy_history, label='Accuracy', color='g', linewidth=2, marker='s', markersize=5)
        ax2.tick_params(axis='y', labelcolor='g')
        ax2.plot([x * self.eval_steps for x in list(range(len(self.eval_history)))], self.eval_history, label='Evaluation', color='r', linewidth=2, marker='s', markersize=5)
        
        ax1.set_title('Loss and Accuracy Over Generations')
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper right')
        
        plt.tight_layout()
        plt.show()

    def see_stats(self):
        fig, ax = plt.subplots(figsize=(8, 6))
        y = [x[0] for x in self.cell_stats]
        ax.plot([x * self.eval_steps for x in list(range(len(y)))], y, label='Divider', color='b', linewidth=2, marker='o', markersize=5)
        ax.set_xlabel('Generation')
        ax.set_ylabel('Divider')
        ax.set_title('Divider over time')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='upper left')
        plt.tight_layout()
        plt.show()

    def save(self): 
        with open(f"/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL/PopulationGen{self.generation}.pickle", "wb") as file:
            pickle.dump(self, file)