import random
import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim

class Cell:
    """
    Cell

    You have to define either (parent1 & parent2) or (complexity_level, input_vector_size & output_vector_size)
    - parent: List of attributes of parent
    - complexity_level: Complexity number [positive, int] : higher number gives higher complexity
    - input_vector_size: int : size of flattened input vector
    - output_vector_size: int : size of flattened output vector
    """
    def __init__(self, parent = None, complexity_level = None, input_vector_size = None, output_vector_size = None) -> None:
        self.input_size, self.output_size = input_vector_size, output_vector_size
        if (not parent) and (not complexity_level or not input_vector_size or not output_vector_size) or (complexity_level and complexity_level <= 0): 
            raise ValueError("Either Complexity or Parent1 and Parent2 has to be defined properly")
        # self.complexity = int(complexity_level) # currently not used
        if parent: self._initiate_from_parent(parent)
        else: self._initiate_from_complexity()

    def _initiate_from_complexity(self):
        self.A = torch.randn(self.input_size, self.output_size)
        self.B = torch.randn(1, self.output_size)
        # self.fertility = torch.tensor(1)
        # self.element_multipliers = torch.tensor([1, 1])
        self.dilution_factor = torch.tensor(10)
        # self.mutation_rate = torch.tensor(0.01)

    def _initiate_from_parent(self, parent):
        self.input_size, self.output_size = parent.input_size, parent.output_size
        self.dilution_factor = (parent.dilution_factor + torch.randn(1, 1))
        # self.mutation_rate = parent.mutation_rate + torch.randn(1, 1)
        self.A = parent.A + torch.randn(parent.A.shape) / self.dilution_factor
        self.B = parent.B + torch.randn(parent.B.shape) / self.dilution_factor

    def forward(self, x):
        logits = torch.matmul(x, self.A) + self.B
        softmaxed = torch.softmax(logits, dim=1)
        return softmaxed

    def evaluate(self, xs, ys):
        epsilon = 1e-15
        ys_one_hot = self.convert_ys_to_one_hot(ys)
        preds = self.forward(xs)
        clipped_preds = torch.clamp(preds, epsilon, 1 - epsilon)
        losses = -torch.sum(ys_one_hot * torch.log(clipped_preds), dim=1)
        return torch.mean(losses).item()

    def convert_ys_to_one_hot(self, ys):
        return torch.eye(self.output_size)[ys]#[torch.LongTensor(ys)]

    def accuracy(self, xs, ys):
        preds = self.forward(xs)
        pred_indices = torch.argmax(preds, dim=1)
        correct_predictions = torch.eq(pred_indices, ys)
        accuracy = torch.mean(correct_predictions.float()).item()
        return accuracy

    def get_stats(self):
        return [self.dilution_factor]

