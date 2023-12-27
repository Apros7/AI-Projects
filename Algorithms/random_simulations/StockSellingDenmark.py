
import matplotlib.pyplot as plt

# Script for simulation when it is best to sell stocks in Denmark

# Tax are as following:
# 27% on first 58.900 (2023) every year (61.000 in 2024)
# 42% on all other profit over that

# This script aims to answer:
# Is it best to sell every year to realize profits or to sell when needed?
# Starting capital: 200.000
# Yearly investment: 60.000

tax_limit_year0 = 58900
tax_limit_growth_yoy = (61000 - 58900) / 58900 # 3.5% (Assumed to continue)

# Constants:
starting_capital = 300000
yearly_investment = 0
years = 30
yearly_investment_growth = 0.10
initial_tax = 0.27
top_tax = 0.42

# Option 1: Selling every year
# Every year sells to the limit and then reinvestest after payed taxes

realized_profits = 0
capital = starting_capital
money_put_in = starting_capital
tax_limit = tax_limit_year0

option1_capitals = [capital]
option1_if_sold_all = [0]

for i in range(years):
    money_put_in += yearly_investment
    capital += yearly_investment
    capital_growth = capital * yearly_investment_growth
    capital += capital_growth
    profit_to_tax = min(capital_growth, tax_limit)
    capital -= profit_to_tax
    realized_profits += profit_to_tax * (1 - initial_tax)
    capital += profit_to_tax * (1 - initial_tax)
    money_put_in += profit_to_tax * (1 - initial_tax)
    option1_capitals.append(capital)
    option1_if_sold_all.append(money_put_in + (capital - money_put_in) * (1 - top_tax))
    tax_limit *= 1 + tax_limit_growth_yoy

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

ax = axs[0]
ax.plot(option1_capitals)
ax.scatter(list(range(years+1)), option1_capitals)
ax.plot(option1_if_sold_all)
ax.scatter(list(range(years+1)), option1_if_sold_all)
ax.set_title(f"Selling every year: {option1_if_sold_all[-1]:,.2f}")
ax.set_xlabel("Year")
ax.set_xlabel("Profit after tax")

# Option 2: Selling last year
# Putting in money every year, selling everything at year 20

option2_capitals = [starting_capital]
option2_realized_profits = [0]
option2_if_sold_all = [0]

realized_profits = 0
capital = starting_capital
tax_limit = tax_limit_year0
money_put_in = starting_capital

for i in range(years):
    money_put_in += yearly_investment
    capital += yearly_investment
    capital_growth = capital * yearly_investment_growth
    capital += capital_growth
    option2_capitals.append(capital)
    option2_realized_profits.append(realized_profits)
    profit_to_tax = min(capital_growth, tax_limit)
    realized_profits = (profit_to_tax * (1 - initial_tax))
    option2_if_sold_all.append(money_put_in + realized_profits + (capital - profit_to_tax - money_put_in) * (1 - top_tax))
    tax_limit *= 1 + tax_limit_growth_yoy

ax = axs[1]
ax.plot(option2_capitals)
ax.scatter(list(range(years+1)), option2_capitals)
ax.plot(option2_if_sold_all)
ax.scatter(list(range(years+1)), option2_if_sold_all)
ax.set_title(f"Selling year {years}: {option2_if_sold_all[-1]:,.2f}")
ax.set_xlabel("Year")
ax.set_xlabel("Profit after tax")

max_y_value = max(option2_capitals + option1_capitals) * 1.05
axs[0].set_ylim(bottom = 0, top = max_y_value)
axs[1].set_ylim(bottom = 0, top = max_y_value)

ax = axs[2]
ax.set_title("What is best? (Sold all at end - Sold every year)")
difference = [op2 - op1 for op1, op2 in zip(option1_if_sold_all, option2_if_sold_all)]
ax.plot(difference)
ax.scatter(list(range(years+1)), difference)
ax.set_xlabel("Year")
ax.set_xlabel("Profit after tax")

plt.show()
