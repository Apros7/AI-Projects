import random
import numpy as np

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
        self.feature_numbers = self.input_size * self.output_size
        features = np.random.normal(0, 1, self.feature_numbers)
        feature_segments = np.array_split(features, self.output_size)
        self.A = np.vstack(feature_segments).T
        self.B = np.random.normal(0, 1, (1, self.output_size))

    def _initiate_from_parent(self, parent):
        self.input_size, self.output_size = parent.input_size, parent.output_size
        self.A = parent.A + np.random.normal(0, 1, parent.A.shape) / 10
        self.B = parent.B + np.random.normal(0, 1, parent.B.shape) / 10

    def forward(self, x):
        logits = np.dot(x, self.A) + self.B
        softmaxed = np.exp(logits - np.max(logits)) / np.sum(np.exp(logits - np.max(logits)))
        return softmaxed

    def evaluate(self, xs, ys):
        epsilon = 1e-15
        ys = self.convert_ys_to_one_hot(ys)
        preds = self.forward(np.array(xs))
        clipped_preds = np.clip(preds, epsilon, 1 - epsilon)
        losses = -np.sum(ys * np.log(clipped_preds), axis=1)
        return np.mean(losses)

    def convert_ys_to_one_hot(self, ys): return np.eye(10)[ys] # return np.eye(self.output_size)[y]

    def accuracy(self, xs, ys):
        ys_one_hot = self.convert_ys_to_one_hot(ys)
        preds = self.forward(np.array(xs))
        pred_indices = np.argmax(preds, axis=1)
        correct_predictions = np.equal(pred_indices, ys_one_hot)
        accuracy = np.mean(correct_predictions)
        return accuracy

