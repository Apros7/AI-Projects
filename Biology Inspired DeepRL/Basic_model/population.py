from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt
from tqdm import tqdm
import pickle
import torch
import sys

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
    - eval_info_steps [int, optional default 500] : Steps between printing evaluation information
    - eval_info [bool, optional, default True] : Whether to print out eval accuracy every 5th evaluation
    - complexity_level [int, optional, default 10] : The initial complexity of the cell initialized at generation 0
    - data_evaluation_factor [float, [0, 1], optional, default 0.1] : factor of dataset to use for evaluation
    - save [bool, optional, default False] : Whether to save population or 

    """
    def __init__(self, input_vector_size, output_vector_size, childs_per_parent = 50, top_performers_count = 25,
                eval_steps = 100, eval_info_steps = 500, eval_info = True, complexity_level = 10, 
                data_evaluation_factor = 0.1, save = False, save_dir = "") -> None:
        self.input_vector_size = input_vector_size
        self.output_vector_size = output_vector_size
        self.childs_per_parent = childs_per_parent
        self.top_performers_count = top_performers_count
        self.eval_steps = eval_steps
        self.eval_info_steps = eval_info_steps
        self.eval_info = eval_info
        self.complexity_level = complexity_level
        self.data_evaluation_factor = data_evaluation_factor
        self.save = save
        self.save_dir = save_dir

class Population():
    """
    Population

    Either one has to be defined:
    - PopulationArgument [optional, default None] : PopulationArgument object
    - Loading Path [string, optional, default None] : Path to saved population
    
    """
    def __init__(self, PopulationArgument = None, loading_path = None) -> None:
        self.parents_as_top_performers, self.parents_as_top_performers_lst = 0, []
        self.set_arguments(PopulationArgument)
        self.generation, self.loss_history, self.accuracy_history, self.eval_history, self.cell_stats = 0, [], [], [], []
        divider("\nInitiating Population...")
        population_size = (self.childs_per_parent + 1) * self.top_performers_count
        print(f"Creating {population_size} cells with complexity level {self.complexity_level}...")
        self.population = [Cell(complexity_level=self.complexity_level, input_vector_size=self.input_vector_size, output_vector_size=self.output_vector_size) for _ in tqdm(range(population_size))]
        tiny_divider()

    def set_arguments(self, arguments):
        self.input_vector_size = arguments.input_vector_size
        self.output_vector_size = arguments.output_vector_size
        self.childs_per_parent = arguments.childs_per_parent
        self.top_performers_count = arguments.top_performers_count
        self.eval_steps = arguments.eval_steps
        self.eval_info_steps = arguments.eval_info_steps
        self.eval_info = arguments.eval_info
        self.complexity_level = arguments.complexity_level
        self.data_evaluation_factor = arguments.data_evaluation_factor

    def evaluate_cell(self, cell, xs, ys):
        return cell.evaluate(xs, ys), cell

    def get_evaluation_set(self, xs, ys):
        evaluation_set_size = int(len(xs) * self.data_evaluation_factor)
        indexes = torch.tensor(random.sample(range(len(xs)), evaluation_set_size))
        # indexes = torch.randperm(len(xs))[:evaluation_set_size]
        eval_x = xs[indexes]
        eval_y = ys[indexes]
        return eval_x, eval_y
    
    def evaluate(self, xs, ys, prev_top_performers):
        eval_x, eval_y = self.get_evaluation_set(xs, ys)
        with ThreadPoolExecutor(max_workers=4) as executor:
            losses = list(executor.map(lambda x: self.evaluate_cell(x, eval_x, eval_y), self.population))
        losses.sort(key = lambda x: x[0])
        for i, (value, top_performer) in enumerate(losses[:self.top_performers_count]):
            top_performer.rating = i + 1
            if top_performer in prev_top_performers: top_performer.is_top_performer()
        self.parents_as_top_performers_lst.append(sum([x[1] in prev_top_performers for x in losses[:self.top_performers_count]]))
        top_performers = [x[1] for x in losses[:self.top_performers_count]]
        mean_top_performers_loss = np.mean([x[0] for x in losses[:self.top_performers_count]])
        self.loss_history.append(mean_top_performers_loss)
        self.top_performer = losses[0][1]
        self.accuracy_history.append(self.top_performer.accuracy(xs, ys))
        self.cell_stats.append(self.top_performer.get_stats())
        # self.cell_stats.append(np.mean([performer.get_stats() for performer in top_performers], axis=0))
        return top_performers

    def populate_next_generation(self, top_performers):
        children = [Cell(parent=parent, complexity_level=self.complexity_level) for parent in top_performers for i in range(self.childs_per_parent)]
        self.population = top_performers + children

    def track(self, x_test, y_test):
        if self.generation % self.eval_steps == 0:
            self.eval_history.append(self.top_performer.accuracy(x_test, y_test))
        if not self.eval_info: return
        if self.generation % self.eval_info_steps == 0: 
            tqdm.write(f"Generation {self.generation} | Eval accuracy: {round(self.eval_history[-1] * 100, 2)}% | Train accuracy: {round(self.accuracy_history[-1] * 100, 2)}%") 

    def progress(self, x_train, y_train, x_test, y_test, generations = 1):
        tiny_divider(f"Evolving population:")
        top_performers = []
        for _ in tqdm(range(generations), desc = f"Simulating {generations} generations"):
            # if self.generation % (generations // 4) == 0: self.complexity_level *= 5
            top_performers = self.evaluate(x_train, y_train, top_performers)
            self.populate_next_generation(top_performers)
            self.generation += 1
            self.track(x_test, y_test)
        divider(f"Final Eval Accuracy at generation {self.generation}: {round(self.top_performer.accuracy(x_test, y_test) * 100, 2)}%")

    def get_top_performers(self, xs, ys): return self.evaluate(xs, ys)

    def see(self):
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(12, 8))
        self.see_accuracy(ax1)
        self.see_loss(ax2)
        self.see_top_performers(ax3)
        self.see_cell_stats(ax4)
                
        plt.tight_layout()
        plt.show()

    def see_accuracy(self, ax):
        x = list(range(1, self.generation + 1))
        ax.set_ylabel('Accuracy', color='g')
        ax.plot(x, self.accuracy_history, label='Accuracy', color='g', linewidth=2, marker='s', markersize=5)
        ax.tick_params(axis='y', labelcolor='g')
        ax.plot([x * self.eval_steps for x in list(range(len(self.eval_history)))], self.eval_history, label='Evaluation', color='r', linewidth=2, marker='s', markersize=5)
        ax.set_title('Loss and Accuracy Over Generations')
        ax.legend(loc = 'lower left')


    def see_loss(self, ax): 
        # Include eval accuracy
        x = list(range(1, self.generation + 1))
        ax.plot(x, self.loss_history, label='Loss', color='b', linewidth=2, marker='o', markersize=5)
        ax.set_xlabel('Generation')
        ax.set_ylabel('Loss')
        ax.set_title('Top performers mean loss over generations')
        ax.grid(True, linestyle='--', alpha=0.7)
        
        ax.set_title('Loss and Accuracy Over Generations')
        ax.legend(loc='upper right')

    def see_top_performers(self, ax):
        ax.plot([x for x in list(range(len(self.parents_as_top_performers_lst)))], self.parents_as_top_performers_lst, label="Parents as top performers", linewidth=2, marker='o', markersize=5)
        ax.set_title("Number of parents that is in top performers")

    def see_cell_stats(self, ax):
        names = ["Dilution Factor", "Parent rating"]
        for i in range(len(self.cell_stats[0])):
            y = [x[i] for x in self.cell_stats]
            ax.plot([x for x in list(range(len(y)))], y, label=names[i], linewidth=2, marker='o', markersize=5)
        ax.set_xlabel('Generation')
        ax.set_ylabel('Value')
        ax.set_title('Overview of top performer stats over time')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend(loc='upper left')

    def save(self): 
        with open(f"/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL/PopulationGen{self.generation}.pickle", "wb") as file:
            pickle.dump(self, file)