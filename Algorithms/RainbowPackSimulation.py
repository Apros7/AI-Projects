import matplotlib.pyplot as plt
import random
from tqdm import tqdm
from collections import Counter
import numpy as np 

def simulate_pack(threshold):
    if random.uniform(0, 100) <= 50: return False
    if random.uniform(0, 100) <= threshold: return True
    return False

def simulate_until_success():
    threshold = 0
    while not simulate_pack(threshold):
        threshold += 3
    return threshold

def get_result(ending_thresholds):
    count_dict = Counter(ending_thresholds)
    all_possibilities = list(np.arange(0, 103, 3))
    result = [0] * len(all_possibilities)
    for i, num in enumerate(all_possibilities):
        result[i] = count_dict.get(num, 0)
    return all_possibilities, result

def probability(value, results_to_plot):
    # Probability of value or higher
    number_of_simulations = sum(results_to_plot[1])
    number_of_simulations_higher_than_x = sum([y for (x, y) in zip(results_to_plot[0], results_to_plot[1]) if x > value])
    likelihood = number_of_simulations_higher_than_x / number_of_simulations * 100
    print(f"Likelihood of getting above {value} = {round(likelihood, 2)}%")

def simulate_x_packs(x):
    ending_thresholds = []
    for _ in tqdm(range(x)):
        ending_thresholds.append(simulate_until_success())
    results_to_plot = get_result(ending_thresholds)
    return results_to_plot

def show_plot(results_to_plot):
    plt.scatter(results_to_plot[0], results_to_plot[1])
    plt.bar(results_to_plot[0], results_to_plot[1], width=2)
    plt.show()

if __name__ == "__main__":
    results_to_plot = simulate_x_packs(10000)
    probability(30, results_to_plot)
    probability(50, results_to_plot)
    probability(60, results_to_plot)
    show_plot(results_to_plot)
    