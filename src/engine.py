import sys
from rw import save_file, read_file
from trade import get_price
from portfolio import *

def start_with_new_portfolio():
    return Portfolio(get_name())

def get_name():
    return input("Please enter a portfolio name: ")

def load_portfolio(name):
    data = read_file(name)
    return Portfolio(data['name'], data['buy_power'], data['stocks'])


if __name__ == '__main__':
    if len(sys.argv) == 1:
        portfolio = start_with_new_portfolio()
    elif len(sys.argv) == 2:
        portfolio = load_portfolio(sys.argv[1])
    else:
        print(f'Invalid number of arguments {len(sys.argv) - 1}')
        print("Usage: engine.py {name} (optional)")
        print("No arguments - You will be prompted to create a new portfolio")
        print("{name} - the name of the portfolio that you wish to open should be in /resources")
        exit()
    while True:
        line = input('>>> ')
        tokens = line.split(' ')
        if tokens[0].lower() == 'buy':
            price = get_price(tokens[1])
            try:
                portfolio.buy_stock(tokens[1], tokens[2], price)
            except ValueError as e:
                print(e.message)
        elif tokens[0].lower() == 'sell':
            price = get_price(tokens[1])
            try:
                portfolio.sell_stock(tokens[1], tokens[2], price)
            except ValueError as e:
                print(e.message)
        elif tokens[0].lower() == 'display':
            print(portfolio.get_portfolio())
        elif tokens[0].lower() == 'price':
            price = get_price(tokens[1])
            print(f'{tokens[1]} current price data is {price}')
        elif tokens[0].lower() == 'exit':
            save_file(portfolio.name, data=portfolio.get_portfolio())
            break
        else:
            print(f'Invalid command {tokens[0]}.')
