from Basic_model.population import Population, PopulationArguments
from Basic_model.cell import Cell
import pickle
import torch
import tensorflow as tf

torch.set_grad_enabled(False)

# Hvorfor vælges bedste aldrig??
# Maybe use backprob for values and mutation for structure
# Maybe multiple stages?
# Maybe multiple populations?

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(len(x_train), len(x_test))

num_samples = 10000
x_train = x_train[:num_samples]
y_train = y_train[:num_samples]

x_train = torch.tensor(x_train, dtype=torch.float32)
y_train = torch.LongTensor(y_train)

x_train = x_train / 255.0
x_train = x_train.reshape(num_samples, -1)

x_test_len = len(x_test)
x_test = (torch.tensor(x_test, dtype=torch.float32) / 255).reshape(len(x_test), -1)
y_test = torch.LongTensor(y_test)


arguments = PopulationArguments(
    input_vector_size = 784, 
    output_vector_size = 10, 
    # childs_per_parent = 100, 
    # top_performers_count = 20,
    childs_per_parent = 10, 
    top_performers_count = 10,
    eval_steps = 5, 
    eval_info_steps = 25,
    eval_info = True, 
    complexity_level = 10, 
    data_evaluation_factor = 1
)

population = Population(arguments)

# Without optim:            generation = 500 # 500 generationer, 5000 billeder, 57:09 min, final acc = 84.51%
# With optim1:              generation = 500 # 500 generationer, 5000 billeder, 36:38 min, final acc = 84.48%
# With workers:             generation = 500 # 500 generationer, 5000 billeder, 37:44 min, final acc = 83.69%
# With random evalset:      generation = 500 # 500 generationer, 50000 billeder, 36:42 min, final acc = 85.91%
# With small child and tp:  generation = 500 # 1000 generationer, 50000 billeder, 07:56 min, final acc = 85.96%
# With population optim:    generation = 500 # 1000 generationer, 50000 billeder, 04:19 min, final acc = 86.65%
# Compare these values with nn:                                   50000 billeder, 01:05 min, final acc = 92.54%

# population = pickle.load(open(f"/Users/lucasvilsen/Desktop/AI-FunProjects/Biology Inspired DeepRL/PopulationGen{generation}.pickle", "rb"))
population.progress(x_train, y_train, x_test, y_test, generations = 1000)
population.save()
population.see_performance()
population.see_stats()