# MA-Crossover-Trading-Strategy

Overview
This Python project utilizes a Moving Average Crossover strategy for stock trading simulation. It automatically fetches historical stock data using the Yahoo Finance API, calculates moving averages over custom time windows, and generates Buy/Sell signals based on crossovers.The strategy's performance is measured using Cumulative Return and Sharpe Ratio.
It is able to analyze multiple stock tickers at once. Calculate short-term and long-term moving averages. Identify trading signals and visualize them on price charts. Compute and display key performance metrics. And has robust error handling for missing data and short history periods.

In financial markets, moving averages are widely used to filter out noise from price data and highlight underlying trends.
A Moving Average Crossover is a simple but powerful technique based on two key ideas: Short-Term Momentum: A short moving average that reacts faster to recent price changes. Long-Term Trend: A long moving average that reflects the broader market direction.

Buying signals are indicated when the short-term average crosses above the long-term average. This is because when the short-term average crosses above the long-term average, it means recent prices are getting stronger compared to the longer-term trend, suggesting a bullish momentum.
However selling signals are indicated when the short-term average crosses below the long-term average, signaling potential market weakness. When the short-term average crosses below the long-term average, it means recent prices are falling compared to the longer-term trend, suggest ing a bearish momentum — weakness.

The strategy captures the phenomenon of autocorrelation in asset returns — once a trend begins, it's statistically more likely to continue for some time rather than immediately reverse.
By following these crossovers, the strategy attempts to ride upward trends and exit during downturns, minimizing emotional decision-making.


Requirements are:
Python 3.8+, the yfinance, pandas, numpy, matplotlib, seaborn libraries. Which you can install via: the bash in your operating system. You can copy and paste this code to install the libraries: pip install yfinance pandas numpy matplotlib seaborn

Once installed run the code in your preferred Python IDE.


At the end you can view the printed performance table summarizing Cumulative Return (%) and Sharpe Ratio for each stock.

Example Output:

![Screenshot 2025-04-26 201141](https://github.com/user-attachments/assets/7faab8b0-ccc6-4d1b-8b8f-dcd8ffe350d9)


Christian Burke
April 2025
