# Monte Carlo Simulation for Portfolio Value

## Overview

This project implements a Monte Carlo simulation to predict the future value of a portfolio of stocks. It retrieves historical stock data from Yahoo Finance, calculates daily percentage changes, and simulates potential portfolio outcomes over a specified time period using Cholesky decomposition and covariance matrix-based modeling.

The main steps include:
- Fetching historical stock data.
- Calculating daily percentage changes.
- Generating simulations using a random process (Monte Carlo).
- Plotting the results to visualize possible future portfolio values.

## Key Components

### `get_data(curStock)`
This function fetches historical stock data from Yahoo Finance and calculates daily percentage changes.

- **Arguments:**
  - `curStock` (str): The stock symbol to fetch data for (e.g., 'AAPL' for Apple).
- **Returns:** 
  - A `DataFrame` containing stock data with a column for daily percentage changes.

### `calculate_mean(stock_data)`
This function calculates the mean of daily percentage changes for the given stock data.

- **Arguments:**
  - `stock_data` (DataFrame): A DataFrame with stock price data.
- **Returns:** 
  - The mean daily percentage change.

### Monte Carlo Simulation
This section of the code simulates the future value of a portfolio based on randomly generated stock returns. It models 2000 different scenarios for the portfolio's growth over 200 days.

- **Covariance Matrix:** Derived from historical daily percentage changes to model correlations between stocks.
- **Cholesky Decomposition:** Used to simulate random returns with the same statistical properties as historical returns.
- **Portfolio Simulations:** Each simulation randomly allocates weights to different stocks, and portfolio values are updated accordingly over time.

### Plotting
The final portfolio values for each simulation are plotted using Matplotlib, visualizing the range of possible outcomes over the specified time period (200 days).
