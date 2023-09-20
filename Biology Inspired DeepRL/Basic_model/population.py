import matplotlib.pyplot as plt
from tqdm import tqdm
import sys
import pickle

sys.path.append("/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL")
from Basic_model.utils import *
from Basic_model.cell import Cell

class Population():
    """
    Population
    - childs_per_parent [number, default: 5] : number of childs per parent when populating new population
    - number_top_performers [number, default: 25] : number of best cells after simulation used to populate 
    new population
    - complexity_level: Complexity number [positive, int] : higher number gives higher complexity
    - input_vector_size: int : size of flattened input vector
    - output_vector_size: int : size of flattened output vector
    
    """
    def __init__(self, childs_per_parent = 50, number_top_performers = 25, complexity_level = 10,
                input_vector_size = None, output_vector_size = None, eval_steps = 100) -> None:
        self.eval_steps = eval_steps
        self.generation = 0
        self.loss_history, self.accuracy_history, self.eval_history, self.cell_stats = [], [], [], []
        self.childs_per_parent = childs_per_parent
        self.number_top_performers = number_top_performers
        divider("\nInitiating Population...")
        self.population_size = (self.childs_per_parent + 1) * number_top_performers
        print(f"Creating {self.population_size} cells with complexity level {complexity_level}...")
        self.population = [Cell(complexity_level=complexity_level, input_vector_size=input_vector_size, output_vector_size=output_vector_size) for _ in tqdm(range(self.population_size))]
        tiny_divider()
    
    def evaluate(self, xs, ys):
        losses = sorted([(cell.evaluate(xs, ys), cell) for cell in self.population], key=lambda x: x[0])
        top_performers = [x[1] for x in losses[:self.number_top_performers]]
        mean_top_performers_loss = np.mean([x[0] for x in losses[:self.number_top_performers]])
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
                    print(f"Eval accuracy at generation {self.generation}: {round(self.eval_history[-1] * 100, 2)}")

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