import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Global variables 
sns.set(style="darkgrid")
print("This program uses moving averages of diferent time periods and compares them to predict when to buy or sell stock.")
tickers = input("Enter stock ticker symbol(s) (separated by commas): ").upper().split(',')
startDate = "2020-04-01"
endDate = "2025-04-01"
shortWindow = int(input("What's your desired short moving average window: "))
longWindow = int(input("What's your desired long moving average window: "))
startEnd = int(input("Please enter any number to start (0 to end the programm):  "))
results = {}

#Will compare different performance across different stocks
while startEnd != 0:
    for i in tickers:
        data = yf.download(i, start=startDate, end=endDate)[['Close']]
   
        if data.empty or len(data) < longWindow:
            print(f"Not enough data for {i}, skipping...")
            continue

    # Calculate Moving Averages
        data['MA_short'] = data['Close'].rolling(window=shortWindow).mean()
        data['MA_long'] = data['Close'].rolling(window=longWindow).mean()

    # Generate trading signals
        data['Signal'] = 0
        data.loc[data.index[longWindow:], 'Signal'] = (
            data['MA_short'][longWindow:] > data['MA_long'][longWindow:]
        ).astype(int)

    # Identify buy/sell triggers
        data['Position'] = data['Signal'].diff()

    # Calculate returns
        data['Returns'] = data['Close'].pct_change()
        data['Strategy_Returns'] = data['Returns'] * data['Signal'].shift(1)

    # Compute performance metrics
        cumulativeReturn = ((1 + data['Strategy_Returns'].dropna()).prod() - 1)*100 
        sharpeRatio = (
            data['Strategy_Returns'].mean() / data['Strategy_Returns'].std()
        ) * np.sqrt(252)

    # Save to dictionary
        results[i] = {
            'Cumulative Return (%)': round(cumulativeReturn, 4),
            'Sharpe Ratio': round(sharpeRatio, 2)
        }

    # Plot strategy
        plt.figure(figsize=(12, 6))
        plt.plot(data['Close'], label=' Close Price', alpha=0.5)
        plt.plot(data['MA_short'], label=f'{shortWindow}-day Moving Average')
        plt.plot(data['MA_long'], label=f'{longWindow}-day Moving Average')

    # Buy/sell markers
        plt.plot(data[data['Position'] == 1].index, data['Close'][data['Position'] == 1],
             '^', markersize=10, color='green', label='Buy')
        plt.plot(data[data['Position'] == -1].index, data['Close'][data['Position'] == -1],
             'v', markersize=10, color='red', label='Sell')

        plt.title(f"{i} Moving Average Crossover Strategy")
        plt.xlabel("Date")
        plt.ylabel("Price ($)")
        plt.legend()
        plt.tight_layout()
        plt.show()
    startEnd = int(input("Please enter any number to start (0 to end the programm):  "))

# === DISPLAY RESULTS ACROSS ALL TICKERS ===
resultsDF = pd.DataFrame(results).T
print("\n--- Strategy Results ---")
print(resultsDF)
