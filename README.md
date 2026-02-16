# Black–Scholes European Put Option (Python)

## Overview
This project implements the Black–Scholes model to price a European put option in Python.

The model calculates the theoretical option price based on:
- Underlying asset price
- Strike price
- Risk-free interest rate
- Volatility
- Time to maturity

## Methods
- Analytical Black–Scholes formula
- Standard normal distribution (SciPy)
- Modular Python implementation

## Example Parameters
- Spot price (S): 95  
- Strike prices (K): [55, 65, 75, 85, 95]  
- Risk-free rate (r): 2%  
- Volatility (σ): 20%  
- Time to maturity (T): 1 year

## Output
European put option price computed using the Black–Scholes closed-form solution.

## Files
- `blck_schls_euro_put.py` – main pricing script

## Skills Demonstrated
- Financial modelling
- Derivative pricing
- Python for quantitative finance
- Numerical implementation of analytical models
