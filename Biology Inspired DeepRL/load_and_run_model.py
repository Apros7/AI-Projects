import pickle

import tensorflow as tf
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

import numpy as np
num_samples = 1000
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]

x_train = np.array(x_train)
y_train = np.array(y_train)

x_train = x_train / 255.0
x_train = x_train.reshape(num_samples, -1)

generation = 1000
population = pickle.load(open(f"PopulationGen{generation}.pickle", "rb"))

top_performers = population.evaluate(x_train, y_train)
population.populate_next_generation(top_performers)

best_performer = population.top_performer
print(best_performer.evaluate(x_train, y_train))
print(best_performer.accuracy(x_train, y_train))