import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_data(curStock):
    # Get historical data for the stock from Yahoo Finance
    # duration = '3mo'
    stock_data = yf.download(curStock, period='3mo', progress=False)

    # Calculate daily percentage changes
    stock_data['Daily Change'] = stock_data['Close'].pct_change() * 100

    # Drop the first row since percentage change is NaN for it
    stock_data = stock_data.dropna()

    return stock_data


def calculate_mean(stock_data):
    # Calculate the mean of daily percentage changes
    change = stock_data['Daily Change'].mean()
    return change


# Example usage:
meanReturns = []
stock_symbols = ['AAPL', 'AMZN', 'GOOGL', 'META', 'IBM']
stock_data_list = []

for stock in stock_symbols:
    data = get_data(stock)
    stock_data_list.append(data)
    mean_change = calculate_mean(data)
    meanReturns.append(mean_change)

# Concatenate the daily percentage change data of all stocks
all_stock_data = pd.concat(stock_data_list, axis=1)

# Calculate the covariance matrix
covariance_matrix = np.cov(all_stock_data['Daily Change'], rowvar=False)

# Number of Simulations and Time Period
mc_sims = 2000  # Increased number of simulations
T = 200

# Initialize portfolio simulations array
portfolio_sims = np.full(shape=(T, mc_sims), fill_value=0.0)

initial_portfolio_sims = 100000  # Increased initial portfolio value

for m in range(0, mc_sims):
    # Generate random weights for each simulation
    weights = np.random.random(len(meanReturns))
    weights /= np.sum(weights)

    # Do Monte Carlo Simulation
    Z = np.random.normal(size=(T, len(weights)))
    L = np.linalg.cholesky(covariance_matrix)
    dailyReturns = np.dot(L, Z.T).T  # Generate daily returns using Cholesky decomposition
    cumulativeReturns = np.cumprod(1 + dailyReturns, axis=0)  # Calculate cumulative returns

    # Update the portfolio value at each step
    portfolio_value = initial_portfolio_sims * np.dot(weights, cumulativeReturns.T)
    portfolio_sims[:, m] = portfolio_value

# Plot all simulations together
plt.plot(portfolio_sims)
plt.ylabel('Portfolio Value')
plt.xlabel('Days')
plt.title('Monte Carlo Simulations')
plt.show()
