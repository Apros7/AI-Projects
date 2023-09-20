from Basic_model.population import Population, PopulationArguments
from Basic_model.cell import Cell
import pickle
import torch
import tensorflow as tf

torch.set_grad_enabled(False)

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(len(x_train), len(x_test))

import numpy as np

## Could be more efficient to evaluate of part of the dataset for every cell

## Work cells in parallel?

## Train this using pytorch and compare eval accuracy

num_samples = 50000
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]

# x_train = np.array(x_train)
# y_train = np.array(y_train)
x_train = torch.tensor(x_train, dtype=torch.float32)
y_train = torch.LongTensor(y_train)

x_train = x_train / 255.0
x_train = x_train.reshape(num_samples, -1)

x_test_len = len(x_test)
x_test = (torch.tensor(x_test, dtype=torch.float32) / 255).reshape(len(x_test), -1)
y_test = torch.LongTensor(y_test)

# cell1 = Cell(complexity_level = 10, input_vector_size=784, output_vector_size=10)
# print(cell1.evaluate([x_train[0]], [y_train[0]]))
# cell2 = Cell(complexity_level = 10, input_vector_size=784, output_vector_size=10)
# print(cell2.evaluate([x_train[0]], [y_train[0]]))

arguments = PopulationArguments(
    input_vector_size = 784, 
    output_vector_size = 10, 
    childs_per_parent = 50, 
    top_performers_count = 25,
    eval_steps = 100, 
    eval_info = True, 
    complexity_level = 10, 
    data_evaluation_factor = 0.1
)

population = Population(arguments)

# generation = 500 # 500 generationer, 5000 billeder, 57:09 min, final acc = 84.51%
# generation = 500 # 500 generationer, 5000 billeder, 36:38 min, final acc = 84.48%
# generation = 500 # 500 generationer, 5000 billeder, 36:38 min, final acc = 84.48%
# Compare these values with nn

# population = pickle.load(open(f"/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL/PopulationGen{generation}.pickle", "rb"))
population.progress(x_train, y_train, x_test, y_test, generations = 500)
population.save()
population.see_performance()
population.see_stats()