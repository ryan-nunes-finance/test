import numpy as np
from scipy.stats import norm

# parameters
S0 = 95
sigma = 0.2
r = 0.02
T = 1

# strikes 
K = np.array([55, 65, 75, 85, 95])

# black scholes formula 
d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
d2 = (np.log(S0 / K) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))

put_prices = K * np.exp(-r * T) * norm.cdf(-d2) - S0 * norm.cdf(-d1)

# create solution form - using pandas 
import pandas as pd 

put_table = pd.DataFrame({
    "Strike": K,
    "Put Price": put_prices
}).round(3)

print("\n--- Black-Scholes Put Prices ---")
print(put_table)
