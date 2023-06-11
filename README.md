The main.py file processes each ticker listed in the tickers.xlsx file, using the yfinance library to confirm its presence. If a given ticker is successfully located, the program labels its status as True and fetches its most recent closing price (just as an additional confirmation the ticker exists), both of which are then appended to the output. However, if the ticker cannot be located or an error occurs during the process, its status is labeled as False and no closing price is appended for that ticker. All of these results are then stored in a new CSV file called 'tickers_with_yahoo.csv'.

Original ticker list compiled by FML-Research https://github.com/FML-Research/us_stock_tickers
