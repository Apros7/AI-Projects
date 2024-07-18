import random
import matplotlib.pyplot as plt

totals = [0]
attack_wons = [0]
attack_won = 0

def roll(): return random.choice([1,2,3,4,5,6])
def attack(): return sorted([roll(), roll(), roll()], reverse=True)
def defend(): return sorted([roll(), roll()], reverse = True) 
def once():
    global totals
    global attack_wons
    global attack_won
    temp = attack_won
    attacker = attack()
    defender = defend()
    if attacker[0] > defender[0]: temp += 1
    if attacker[1] > defender[1]: temp += 1
    attack_won = temp
    totals.append(totals[-1] + 2)
    # totals.append(totals[-1] + 1)
    attack_wons.append(temp/totals[-1])

def run():
    for i in range(1000):
        once()
    # print(attack_wons)
    print(attack_wons[-1])
    plt.plot(list(range(len(attack_wons))), attack_wons)
    plt.show()

if __name__ == "__main__":
    # Attack 3 against defender 2
    run()