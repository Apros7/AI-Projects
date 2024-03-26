import unittest
from autograd.engine import Tensor
from autograd.nn import Neuron, Perceptron
import numpy as np

def topo_search(v):
    topo = []
    visited = set()
    def build_topo(v):
        if v not in visited:
            visited.add(v)
            for child in v._prev:
                build_topo(child)
            topo.append(v)
    build_topo(v)
    return topo

class TestImplementation(unittest.TestCase):
    def test_values(self):
        x1 = Tensor(2.0)
        x2 = Tensor(0.0)
        w1 = Tensor(-3.0)
        w2 = Tensor(1.0)
        b = Tensor(6.8813735870195432)
        o = (x1*w1+x2*w2 + b).tanh()
        assert round(o.data, 4) == 0.7071 

    def test_grads(self):
        x1 = Tensor(2.0)
        x2 = Tensor(0.0)
        w1 = Tensor(-3.0)
        w2 = Tensor(1.0)
        b = Tensor(6.8813735870195432)
        o = (x1*w1+x2*w2 + b).tanh()
        o.backward()
        assert round(x1.grad, 3) == -1.500
        assert round(x2.grad, 3) == 0.500
        assert round(w1.grad, 3) == 1.000
        assert round(w2.grad, 3) == 0.000

    def test_exp(self):
        x1 = Tensor(2.0)
        x2 = Tensor(0.0)
        w1 = Tensor(-3.0)
        w2 = Tensor(1.0)
        b = Tensor(6.8813735870195432)
        n = x1*w1+x2*w2 + b
        e = (2*n).exp()
        o = (e - 1) / (e + 1)
        o.backward()
        assert round(o.data, 4) == 0.7071 
        assert round(x1.grad, 3) == -1.500
        assert round(x2.grad, 3) == 0.500
        assert round(w1.grad, 3) == 1.000
        assert round(w2.grad, 3) == 0.000

    def test_neuron(self):
        n = Neuron(4)
        x = [2.0, 1.0, 2.0, 1.0]
        assert round(n(x), 4) == round(sum([wi * xi for wi, xi in zip(n.w, x)], n.b).tanh(), 4)

    def test_mlp(self):
        p = Perceptron(3, [4, 4, 1])
        x = [2.0, 2.0, 4.0]
        assert type(p(x)) == Tensor

    def test_params(self):
        p = Perceptron(3, [4, 4, 1])
        x = [2.0, 2.0, 4.0]
        assert type(p.parameters()) == list
        assert len(p.parameters()) == 41

    def test_deepsearch(self):
        x1 = Tensor(2.0)
        x2 = Tensor(0.0)
        w1 = Tensor(-3.0)
        w2 = Tensor(1.0)
        b = Tensor(6.8813735870195432)
        n = x1*w1+x2*w2 + b
        e = (2*n).exp()
        o = (e - 1) / (e + 1)
        topo = topo_search(o)
        deep = Tensor.deepsearch(o, visited=set(), order=list())
        assert all([t.data == d.data for t,d in zip(topo, deep)])

if __name__ == "__main__":
    unittest.main()