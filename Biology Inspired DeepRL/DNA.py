import random
from termcolor import colored
from itertools import product
import torch
import torch.nn as nn

MIN_DNA_LENGTH = 40
CODON_LIST = ["start", "start", "0.2", "0.5", "3", "5", "initiate_layer", "tanh", "sigmoid", "relu", "learning_rate", "batch_size", "dropout", "neurons", "stop", "stop"]
combinations = ["".join([str(el) for el in x]) for x in product([0, 1], repeat=4)]
CODON_DICT = {k: v for k, v in zip(combinations, CODON_LIST)}

class Species:
    def __init__(self, input_size, output_size, DNA_string_length = 100, mutation_risk = 1e-3) -> None:
        self.population = Cell()

class Cell:
    def __init__(self, mutated_parent_DNA = None, DNA_string_length = 100, mutation_risk = 1e-3) -> None:
        self.alive = False
        if mutated_parent_DNA is None: self.DNA = self._initiate_DNA(DNA_string_length, mutation_risk)
        else: self.DNA = mutated_parent_DNA
        if len(self.DNA.string) > 40: self.alive = True

    def _initiate_DNA(self, DNA_length, mutation_risk):
        DNA_string = [random.randint(0, 1) for _ in range(DNA_length)]
        return DNA(DNA_string, mutation_risk=mutation_risk)

    def mutate(self): return Cell(mutated_parent_DNA = self.DNA.mutate())

class DNA:
    """
    DNA of cell
    """
    def __init__(self, DNA_string, mutation_risk = 1e-3) -> None:
        self.string = DNA_string
        self.mutation_risk = mutation_risk

    def mutate(self):
        new_string = self._unlist([self.mutate_bit(bit) if random.random() < self.mutation_risk else bit for bit in self.string])
        return DNA(new_string, self.mutation_risk)
    
    def mutate_bit(self, bit):
        mutation_types = [1 - bit, 1 - bit, [0, bit], [1, bit], [], []]
        return random.choice(mutation_types)

    def _unlist(self, string): return [bit for sublist in string for bit in (sublist if isinstance(sublist, list) else [sublist])]

class Ribosome:
    """
    Converts DNA to Neural Network
    """
    def __init__(self) -> None: pass
    def to_nn(self, string, input_size, output_size):
        codons = self._get_codons(string)
        words = self._to_words(codons)
        layers, values = self._get_layers(words)
        nn = self._turn_to_nn(input_size, output_size, layers, values)
        return nn

    def _get_codons(self, string): return ["".join([str(x) for x in string[i:i+4]]) for i in range(0, len(string)-1, 4)]
    def _to_words(self, codons): return [CODON_DICT[el] for el in codons]
    def _turn_to_nn(self, input_size, output_size, layers, values): return NeuralNetwork(input_size, output_size, layers, values)
    def _get_layers(self, words):
        layers = []
        values = {"batch_size": 1, "learning_rate": 1e-4}
        ongoing, temp, cur_key, cur_value = False, {}, "", 1
        for codon in words:
            if codon == "start": ongoing = True
            if codon != "start" and not ongoing: continue
            if codon == "stop": 
                if cur_key in temp: temp[cur_key] *= cur_value
                elif cur_key in values: values[cur_key] *= cur_value
                cur_key = ""; layers.append(temp); temp = {}; ongoing = False; continue
            if codon == "initiate_layer": temp = {"neurons": 10, "activation": "relu", "dropout": 0.1}
            if codon in ["learning_rate", "batch_size", "dropout", "neurons"]:
                if cur_key in temp: temp[cur_key] *= cur_value
                elif cur_key in values: values[cur_key] *= cur_value
                cur_key = codon
            if codon in ["0.01", "0.1", "2", "5", "10"] and codon != "": cur_value *= float(codon)
        return [layer for layer in layers if len(layer) > 0], values

activation = {"relu": nn.ReLU(), "tanh": nn.Tanh(), "sigmoid": nn.Sigmoid()}

class NeuralNetwork(nn.Module):
    def __init__(self, input_size, output_size, layers, values) -> None:
        super(NeuralNetwork, self).__init__()
        layers = self._clean_layers(layers)
        self.batch_size = values["batch_size"]
        self.lr = values["learning_rate"]
        self._make_layers(input_size, output_size, layers)
    
    def _clean_layers(self, layers): return [layer for layer in layers if layer["dropout"] < 1 and layer["neurons"] > 1 and layer["neurons"] < 100000]
    def _make_layers(self, input_size, output_size, layers):
        nn_layers = []
        for layer in layers:
            neurons = int(round(layer["neurons"]))
            nn_layers.append(nn.Linear(input_size, neurons))
            input_size = neurons
            nn_layers.append(activation[layer["activation"]])
        nn_layers.append(nn.Linear(input_size, output_size))
        nn_layers.append(nn.Softmax(dim=1))
        self.layers = nn_layers

    def forward(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def train(self, xs, ys):
        pass

    def eval(self, xs, ys):
        pass

def compare_strings(string1, string2):
    min_len = min(len(string1), len(string2))
    differences_indexes = [i for i in range(min_len) if string1[i] != string2[i]]
    dna1 = ''.join([str(n) if i not in differences_indexes or i > min_len else colored(str(n), 'white', 'on_red') for i, n in enumerate(string1)])
    dna2 = ''.join([str(n) if i not in differences_indexes or i > min_len else colored(str(n), 'white', 'on_red') for i, n in enumerate(string2)])
    print("DNA 1: ", dna1)
    print("DNA 2: ", dna2)

if __name__ == "__main__":
    input_size = 10
    output_size = 4

    cell = Cell(DNA_string_length = 10000, mutation_risk = 1e-3)
    ribosome = Ribosome()
    original_dna_string = cell.DNA.string
    small_nn = ribosome.to_nn(original_dna_string, input_size, output_size)

