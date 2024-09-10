# Checks the speed of autograd on 10 steps

from autograd.engine import Tensor
from autograd.nn import Perceptron, MSELoss
import numpy as np
from tqdm import tqdm
import random
import time

from tinygrad.helpers import fetch
import gzip

# taken from tinygrad.extra.datasets:
def fetch_mnist(tensors=False):
  parse = lambda file: np.frombuffer(gzip.open(file).read(), dtype=np.uint8).copy()
  BASE_URL = "https://storage.googleapis.com/cvdf-datasets/mnist/"   # http://yann.lecun.com/exdb/mnist/ lacks https
  X_train = parse(fetch(f"{BASE_URL}train-images-idx3-ubyte.gz"))[0x10:].reshape((-1, 28*28)).astype(np.float32)
  Y_train = parse(fetch(f"{BASE_URL}train-labels-idx1-ubyte.gz"))[8:].astype(np.int8)
  X_test = parse(fetch(f"{BASE_URL}t10k-images-idx3-ubyte.gz"))[0x10:].reshape((-1, 28*28)).astype(np.float32)
  Y_test = parse(fetch(f"{BASE_URL}t10k-labels-idx1-ubyte.gz"))[8:].astype(np.int8)
  if tensors: return Tensor(X_train).reshape(-1, 1, 28, 28), Tensor(Y_train), Tensor(X_test).reshape(-1, 1, 28, 28), Tensor(Y_test)
  else: return X_train, Y_train, X_test, Y_test

def one_hot_encode(array):
    encoded_array = np.zeros((array.size, array.max()+1), dtype=int)
    encoded_array[np.arange(array.size),array] = 1 
    return encoded_array

def speedtest():
    start_time = time.time()

    X_train, Y_train, X_test, Y_test = fetch_mnist()
    X_train, X_test = X_train/255.0, X_test/255.0
    Y_train = one_hot_encode(Y_train)
    Y_test = one_hot_encode(Y_test)

    layers = [784, 10]
    loss_func = MSELoss()
    model = Perceptron(layers)
    lr = 0.005

    steps = 10
    batch_size = 32
    indexes = list(range(len(X_train)))

    print(f"Speedtest running a {layers} perceptron for {steps} steps and {batch_size} batch size")

    for k in tqdm(range(steps)):
        batch_idx = list(random.sample(indexes, batch_size))
        # forward
        ypreds = [model(X_train[i]) for i in batch_idx]
        ypreds = np.concatenate(ypreds)
        ycorr = np.concatenate([Y_train[i] for i in batch_idx])
        loss = loss_func(ypreds, ycorr)

        # backward
        model.zero_grad()
        loss.backward()

        # update
        for p in model.parameters():
            p.data += -lr * p.grad

    print(f"The time for {steps} steps is {time.time() - start_time} seconds")
    return time.time() - start_time

if __name__ == "__main__": speedtest()

