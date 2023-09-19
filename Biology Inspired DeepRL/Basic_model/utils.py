import numpy as np

def divider(text = None): print_text(text); print(f"{'=' * 40}")
def tiny_divider(text = None): print_text(text); print(f"{'-' * 40}")
def print_text(text): 
    if text: print(text) 

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()
