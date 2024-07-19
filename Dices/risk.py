import random
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

totals = [0]
attack_wons = [0]
attack_won = 0

def all_policies():
    policies = []
    for i in range(1, 7):
        for j in range(1, 7):
            if j <= i: policies.append((i, j))
    return policies

def roll(): return random.choice([1,2,3,4,5,6])
def attack(): return sorted([roll(), roll(), roll()], reverse=True)
def defend(single = False): return [roll()] if single else sorted([roll(), roll()], reverse = True)

def once_one_defend(defenders, attackers_killed, attacker : list = None):
    if not attacker: attacker = attack()
    defender = defend(single = True)
    if attacker[0] <= defender[0]: attackers_killed += 1
    else: defenders -= 1
    return defenders, attackers_killed

def once_two_defend(defenders, attackers_killed, attacker : list = None):
    temp = attack_won
    if not attacker: attacker = attack()
    defender = defend()
    if attacker[0] <= defender[0]: attackers_killed += 1
    else: defenders -= 1
    if attacker[1] <= defender[1] and defenders > 0: attackers_killed += 1
    else: defenders -= 1
    return defenders, attackers_killed

def run_policy(policy: tuple, defenders: int):
    defenders_single, defenders_double = defenders, defenders
    attacker = [policy[0], policy[1]]
    attacks_killed_single = 0
    attacks_killed_double = 0
    while defenders_single > 0 and attacks_killed_single < defenders * 10:
        defenders_single, attacks_killed_single = once_one_defend(defenders_single, attacks_killed_single, attacker)
    while defenders_double > 0 and attacks_killed_double < defenders * 10:
        defenders_double, attacks_killed_double = once_one_defend(defenders_double, attacks_killed_double, attacker)
    return attacks_killed_single, attacks_killed_double

def run():
    RUNS = 10000
    results = {}
    for policy in tqdm(all_policies()):
        prob_single, prob_defend = run_policy(policy, RUNS)
        results[policy] = (prob_single, prob_defend)

    # Extract the policy names and the corresponding probabilities
    policies = list(results.keys())
    prob_singles = [result[0] for result in results.values()]
    prob_defends = [result[1] for result in results.values()]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Create a bar plot where prob_single and prob_defend is side by side for all the policies
    x = np.arange(len(policies))
    width = 0.35
    ax.bar(x - width/2, prob_singles, width, label='Attackers killed single defend')
    ax.bar(x + width/2, prob_defends, width, label='Attackers killed double defend')

    # Find the maximum probability and highlight it with a green line
    for policy, single, double in zip(results.keys(), prob_singles, prob_defends):
        best = ["One", "Two"][[single, double].index(max(single, double))]
        if abs(single - double) < RUNS/10000: best = "Does not matter"
        print(f"For policy {policy} the best options is to defend with {best}")

    # Set the x-axis tick labels
    ax.set_xticks(x)
    ax.set_xticklabels(policies, rotation = 45)

    # Set the title and labels
    ax.set_title('Probabilities of Single and Defend for Each Policy')
    ax.set_xlabel('Policy')
    ax.set_ylabel('Probability')

    # Add a legend
    ax.legend()

    print("-----------------------------------------------------")
    print(*results.items(), sep="\n")

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Attack 3 against defender 2
    run()