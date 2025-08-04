import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Hyperparameters
company = '^IXIC'  # NASDAQ 
start_date = '2010-01-01'
end_date = '2025-08-04'


# Download and preprocess data
df = yf.download(company, start_date, end_date)
df = df[['Close']]
df_close = df['Close'].copy()

# Apply transformations
df_close_log = np.log(df_close)
df_close_tf = np.sqrt(df_close_log)
df_close_shift = df_close_tf.diff().dropna()


"""# --- New: Visualize the fetched and transformed data ---"""

# Plot 1: Raw Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.title(f'Historical Close Prices for {company} ({start_date} to {end_date})')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.grid(True)
plt.savefig('close_prices_plot.png')  
plt.show() 

# Plot 2: Log-Transformed Closing Prices
plt.figure(figsize=(12, 6))
plt.plot(df_close_log.index, df_close_log, label='Log-Transformed Close', color='green')
plt.title(f'Log-Transformed Close Prices for {company}')
plt.xlabel('Date')
plt.ylabel('Log(Close)')
plt.legend()
plt.grid(True)
plt.savefig('log_transformed_plot.png')
plt.show()

# Plot 3: Differenced Series (for stationarity check in time series)
plt.figure(figsize=(12, 6))
plt.plot(df_close_shift.index, df_close_shift, label='Differenced Sqrt(Log(Close))', color='red')
plt.title(f'Differenced Transformed Series for {company}')
plt.xlabel('Date')
plt.ylabel('Differenced Value')
plt.legend()
plt.grid(True)
plt.savefig('differenced_series_plot.png')
plt.show()

# Optional: Save data to CSV for users to download
df.to_csv('historical_close_prices.csv', index=True)
print("Data and plots saved successfully.")
