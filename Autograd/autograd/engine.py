
import numpy as np

class Tensor():
    def __init__(self, data, _children=()): 
        self.data = data
        self.grad =  0.0
        self._backward = lambda: None
        self._prev = set(_children)

    def __repr__(self): return f"Tensor(data={self.data})"

    def __add__(self, other):
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data + other.data, (self, other))
        def _backward(): self.grad += out.grad; other.grad += out.grad
        out._backward = _backward; return out

    def __mul__(self, other): 
        other = other if isinstance(other, Tensor) else Tensor(other)
        out = Tensor(self.data * other.data, (self, other))
        def _backward(): self.grad += other.data * out.grad; other.grad += self.data * out.grad
        out._backward = _backward; return out

    def __pow__(self, other):
        assert isinstance(other, (int, float)), "__pow__ currently only supports int & float"
        out = Tensor(self.data ** other, (self, ))
        def _backward(): self.grad += other * (self.data ** (other - 1)) * out.grad
        out._backward = _backward; return out

    def exp(self):
        out = Tensor(np.exp(self.data), (self, ))
        def _backward(): self.grad += out.data * out.grad
        out._backward = _backward; return out

    def __neg__(self): return self * -1
    def __sub__(self, other): return self + (-other)
    def __truediv__(self, other): return self * (other ** (-1))
    def __rmul__(self, other): return self * other
    def __radd__(self, other): return self + other
    def __rsub__(self, other): return self - other

    ## --- Assisting methods
    def __round__(self, ndigits): return round(self.data, ndigits)
    def item(self): return self.data

    ## --- Activation functions --- ##
    def tanh(self):
        t = (np.exp(2*self.data) - 1)/(np.exp(2*self.data) + 1)
        out = Tensor(t, (self, ))
        def _backward(): self.grad += (1 - t**2) * out.grad
        out._backward = _backward; return out

    def relu(self):
        return None

    ## --- Backward --- ## 

    def zero_grad(self): self.grad = 0.0
    def backward(self):
        self.grad = 1
        for tensor in reversed(Tensor.deepsearch(self, visited=set(), order = list())): tensor._backward()

    @staticmethod
    def deepsearch(tensor, visited, order):
        if tensor not in visited:
            visited.add(tensor)
            for child in tensor._prev: 
                Tensor.deepsearch(child, visited = visited, order = order)
            order.append(tensor)
        return order

    ## Comparisons:
    def __ge__(self, other): return self.data >= other.data if isinstance(other, Tensor) else self.data >= other