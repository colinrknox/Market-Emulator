import json

class Portfolio:

    def __init__(self, name, start_value=100000, stocks=None):
        self.name = name
        self.buy_power = start_value
        if not stocks:
            self.stocks = dict()
        else:
            self.stocks = stocks

    def buy_stock(self, symbol, quantity, price):
        if not self._is_buyable(quantity, price):
            raise ValueError('Not enough buying power for stock purchase')
        if symbol in self.stocks.keys():
            self.stocks[symbol] = self.stocks[symbol] + quantity
        else:
            self.stocks[symbol] = quantity
        self.buy_power = self.buy_power - (price * quantity)

    def _is_buyable(self, quantity, price):
        return (quantity * price) <= self.buy_power

    def sell_stock(self, symbol, quantity, price):
        if not self._is_sellable(symbol, quantity):
            raise ValueError('Not enough stock to sell')
        self.buy_power = self.buy_power + (price * quantity)
        self.stocks[symbol] = self.stocks[symbol] - quantity

    def _is_sellable(self, symbol, quantity):
        return quantity <= self._get_quantity(symbol)

    def _get_quantity(self, symbol):
        if symbol in self.stocks.keys():
            return self.stocks[symbol]
        else:
            return 0

    def get_portfolio(self):
        return json.dumps(self.__dict__)
