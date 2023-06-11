The main.py file scans through the tickers.xlsx file, checking for each ticker's existence using the yfinance library. If the ticker is located, the output is tagged as True; if not, it is marked as False. Alongside this, when a ticker is found (i.e., True), the corresponding last closing price is also appended to the output.

Original ticker list compiled by FML-Research https://github.com/FML-Research/us_stock_tickers
