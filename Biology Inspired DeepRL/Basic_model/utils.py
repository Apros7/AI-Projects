import numpy as np
import torch
import random

def divider(text = None): print_text(text); print(f"{'=' * 40}")
def tiny_divider(text = None): print_text(text); print(f"{'-' * 40}")
def print_text(text): 
    if text: print(text) 

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

# Making a normal dist with mean 1 and sd 0.1
dist = torch.distributions.Normal(1.0, 0.1).sample((1,))

def sample():
    diff = dist.sample((1,))**2
    if diff < 0: return sample()
    options = [1 / diff, diff]
    choice = random.choice(options)
    return choice
