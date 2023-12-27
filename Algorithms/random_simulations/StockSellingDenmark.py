
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
starting_capital = 200000
yearly_investment = 72000
years = 30
yearly_investment_growth = 1.10 # 7% : Low but reasonable
initial_tax = 0.27
top_tax = 0.42

# Option 1: Selling every year
# Every year sells to the limit and then reinvestest after payed taxes

option1_capitals = [starting_capital]
option1_realized_profits = [0]

realized_profits = 0
capital = starting_capital
tax_limit = tax_limit_year0

for i in range(years-1):
    capital += yearly_investment
    capital *= yearly_investment_growth
    capital -= tax_limit
    realized_profits += tax_limit * (1 - initial_tax)
    capital += tax_limit * (1 - initial_tax)
    tax_limit *= 1 + tax_limit_growth_yoy
    option1_capitals.append(capital)
    option1_realized_profits.append(realized_profits)

# Last year:
capital += yearly_investment
capital *= yearly_investment_growth
capital -= tax_limit
realized_profits += tax_limit * (1 - initial_tax)
realized_profits += (capital - realized_profits) * (1 - top_tax)
option1_capitals.append(capital)
option1_realized_profits.append(realized_profits)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

ax = axs[0]
ax.plot(option1_capitals)
ax.scatter(list(range(years+1)), option1_capitals)
ax.plot(option1_realized_profits)
ax.scatter(list(range(years+1)), option1_realized_profits)
ax.set_title(f"Selling every year: {option1_realized_profits[-1]:,.2f}")

# Option 2: Selling last year
# Putting in money every year, selling everything at year 20

option2_capitals = [starting_capital]
option2_realized_profits = [0]

realized_profits = 0
capital = starting_capital
tax_limit = tax_limit_year0

for i in range(years-1):
    capital += yearly_investment
    capital *= yearly_investment_growth
    option2_capitals.append(capital)
    option2_realized_profits.append(realized_profits)

# Last year:
capital += yearly_investment
capital *= yearly_investment_growth
capital -= tax_limit
realized_profits += tax_limit * (1 - initial_tax)
realized_profits += (capital - realized_profits) * (1 - top_tax)
option2_capitals.append(capital)
option2_realized_profits.append(realized_profits)

ax = axs[1]
ax.plot(option2_capitals)
ax.scatter(list(range(years+1)), option2_capitals)
ax.plot(option2_realized_profits)
ax.scatter(list(range(years+1)), option2_realized_profits)
ax.set_title(f"Selling year 20: {option2_realized_profits[-1]:,.2f}")

max_y_value = max(option2_capitals + option1_capitals) * 1.05
axs[0].set_ylim(bottom = 0, top = max_y_value)
axs[1].set_ylim(bottom = 0, top = max_y_value)


plt.show()
