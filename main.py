import pandas as pd
import yfinance as yf

# Read the Excel file
df = pd.read_excel('tickers.xlsx')

# Initialize lists to store yahoo status and closing prices
yahoo_status = []
closing_prices = []

for ticker in df[' Ticker']:  # Update column name here
    ticker_obj = yf.Ticker(ticker)
    # Try to get the historical data. If the ticker is invalid, it will return an empty DataFrame
    hist = ticker_obj.history(period="1d")
    if hist.empty:
        yahoo_status.append(False)
        closing_prices.append(None)
    else:
        yahoo_status.append(True)
        # Select the 'Close' column from the last row (the most recent trading day)
        closing_prices.append(hist['Close'][-1])

# Add the Yahoo status and closing prices to the DataFrame
df['Yahoo'] = yahoo_status
df['Closing Price'] = closing_prices

# Save the DataFrame to a new CSV file
df.to_csv('tickers_with_yahoo.csv', index=False)
