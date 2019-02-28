from src.rw import save_file, read_file
from src.trade import get_price
from src.portfolio import *
from src.response import *

def start_with_new_portfolio():
    return Portfolio(get_name())

def get_name():
    return input("Please enter a portfolio name: ")

def load_portfolio(name):
    data = read_file(name)
    return Portfolio(data['name'], data['buy_power'], data['stocks'])


def read_eval_print_loop(file_name=None):
    if file_name:
        portfolio = load_portfolio(file_name)
    else:
        portfolio = start_with_new_portfolio()

    while True:
        line = input('>>> ')
        tokens = line.split(' ')
        if tokens[0].lower() == 'buy':
            price = float(get_price(tokens[1]))
            try:
                portfolio.buy_stock(tokens[1], int(tokens[2]), price)
            except ValueError as e:
                print(e.message)
            else:
                print(BuyStockResponse.generate(tokens[1], int(tokens[2]), price))
        elif tokens[0].lower() == 'sell':
            price = float(get_price(tokens[1]))
            try:
                portfolio.sell_stock(tokens[1], int(tokens[2]), price)
            except ValueError as e:
                print(e.message)
            else:
                print(SellStockResponse.generate(tokens[1], int(tokens[2]), price))
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
