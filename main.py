import pandas as pd
import yfinance as yf

# Read the Excel file
df = pd.read_excel('tickers.xlsx')

# Initialize lists to store yahoo status and closing prices
yahoo_status = []
closing_prices = []

for ticker in df['Ticker']:
    ticker_obj = yf.Ticker(ticker)
    try:
        quote_table = ticker_obj.get_info()  # This will return a dictionary
        closing_prices.append(quote_table['previousClose'])
        yahoo_status.append(True)
    except Exception as e:
        yahoo_status.append(False)
        closing_prices.append(None)

# Add the Yahoo status and closing prices to the DataFrame
df['Yahoo'] = yahoo_status
df['Closing Price'] = closing_prices

# Save the DataFrame to a new CSV file
df.to_csv('tickers_with_yahoo.csv', index=False)
