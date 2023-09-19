from Basic_model.population import Population
from Basic_model.cell import Cell
import pickle

import tensorflow as tf
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import numpy as np
num_samples = 200
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]

x_train = np.array(x_train)
y_train = np.array(y_train)

x_train = x_train / 255.0
x_train = x_train.reshape(num_samples, -1)

# cell1 = Cell(complexity_level = 10, input_vector_size=784, output_vector_size=10)
# print(cell1.evaluate([x_train[0]], [y_train[0]]))
# cell2 = Cell(complexity_level = 10, input_vector_size=784, output_vector_size=10)
# print(cell2.evaluate([x_train[0]], [y_train[0]]))

population = Population(input_vector_size=784, output_vector_size=10)
# generation = 1000
# population = pickle.load(open(f"PopulationGen{generation}.pickle", "rb"))
population.progress(x_train, y_train, generations = 1000)
population.see_history()
population.save()