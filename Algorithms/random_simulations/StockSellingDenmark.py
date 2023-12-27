
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
yearly_investment = 60000
years = 20

# Option 1: Selling every year
