
import numpy as np
from autograd.engine import Tensor
from typing import List

class Module:
    def zero_grad(self): [p.zero_grad() for p in self.parameters()]

class Neuron(Module):
    def __init__(self, nweights, bias=True):
        self.w = np.array([Tensor(np.random.uniform(-1, 1)) for _ in range(nweights)])
        self.b = Tensor(np.random.uniform(-1, 1)) if bias else None
    def __call__(self, x): return (np.array(x)@self.w + self.b).tanh() if self.b else (np.array(x)@self.w).tanh() 
    def parameters(self) -> np.ndarray[Tensor]: return np.concatenate((self.w, np.array([self.b])))

class Layer(Module):
    def __init__(self, nin, nout): self.ns = [Neuron(nin) for _ in range(nout)]
    def __call__(self, x): return [n(x) for n in self.ns] 
    def parameters(self) -> List[Tensor]: return [p for n in self.ns for p in n.parameters()]

class Perceptron(Module):
    def __init__(self, nin, nouts): ls = [nin] + nouts; self.layers = [Layer(ls[i], ls[i+1]) for i in range(len(ls)-1)]
    def __call__(self, x): 
        for l in self.layers: x = l(x)
        return x[0] if len(x) == 1 else x
    def parameters(self) -> List[Tensor]: return [p for l in self.layers for p in l.parameters()]

## --- Loss Functions --- ##

class Loss:
    def __init__(self): pass # something goes here
    def __call__(self, ycs, yps) -> Tensor: return self.loss_func(ycs, yps)

class MSELoss(Loss):
    def __init__(self): 
        super().__init__(); 
        self.loss_func = lambda ycs, yps: sum((yc - yp)**2 for yc, yp in zip(ycs, yps))

