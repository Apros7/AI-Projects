import random
import math
import numpy as np
import torch


second_tries = 0
dist = torch.distributions.Normal(1.0, 0.1)

testsize = 10
ones = [torch.distributions.Normal(0.0, 10 / 5).sample((1,)) for _ in range(testsize)]
twos = [torch.randn(1) for _ in range(testsize)]

print(ones)
print(twos)

# Function to calculate the inverse CDF
def inverse_cdf():
    global second_tries
    diff = dist.sample((1,))**2
    if diff < 0: second_tries += 1; return inverse_cdf()
    options = [1 / diff, diff]
    choice = random.choice(options)
    return choice

# Number of random samples
num_samples = 10000

# Generate random x values with mean 1
values = [inverse_cdf() for _ in range(num_samples)]

# Print the first few random x values
print(len([x for x in values if x < 1]), len([x for x in values if x > 1]))
print(values[:10])
print(f"{second_tries = }")