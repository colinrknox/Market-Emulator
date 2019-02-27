import unittest
from src.portfolio import Portfolio

class TestPortfolio(unittest.TestCase):

    def setUp(self):
        self.port_one_name = 'one'
        self.port_two_name = 'two'
        self.port_two_buy_power = 40000
        self.port_two_stocks = { 'msft' : 100 }
        self.port_three_name = 'three'
        self.port_three_buy_power = 150000
        self.port_three_stocks = { 'aapl' : 150, 'goog' : 200 }
        self.portfolio_one = self.get_portfolio_one()
        self.portfolio_two = self.get_portfolio_two()
        self.portfolio_three = self.get_portfolio_three()

    def get_portfolio_one(self):
        return Portfolio(self.port_one_name)

    def get_portfolio_two(self):
        return Portfolio(self.port_two_name, self.port_two_buy_power, dict(self.port_two_stocks))

    def get_portfolio_three(self):
        return Portfolio(self.port_three_name, self.port_three_buy_power, dict(self.port_three_stocks))

    def test_constructor_defaults(self):
        self.assertEqual(self.portfolio_one.buy_power, 100000)
        self.assertEqual(self.portfolio_one.stocks, dict())

    def test_constructor_user_defined(self):
        portfolio = Portfolio(self.port_two_name, self.port_three_buy_power, self.port_two_stocks)
        self.assertEqual(portfolio.name, 'two')
        self.assertEqual(portfolio.buy_power, 150000)
        self.assertEqual(portfolio.stocks, { 'msft' : 100 })

    def test__is_buyable_true(self):
        quantity = 10
        price = 200
        self.assertTrue(self.portfolio_one._is_buyable(quantity, price))
        quantity = 400
        price = 100
        self.assertTrue(self.portfolio_two._is_buyable(quantity, price))

    def test__is_buyable_false(self):
        quantity = 1000
        price = 1000
        self.assertFalse(self.portfolio_two._is_buyable(quantity, price))

    def test__get_quantity(self):
        symbol = 'aapl'
        self.assertEqual(self.portfolio_three._get_quantity(symbol), 150)

    def test__get_quantity_zero(self):
        symbol = 'aaaa'
        self.assertEqual(self.portfolio_one._get_quantity(symbol), 0)

    def test__is_sellable(self):
        symbol = 'goog'
        quantity = 200
        self.assertTrue(self.portfolio_three._is_sellable(symbol, quantity))

    def test__is_sellable_false(self):
        symbol = 'msft'
        quantity = 101
        self.assertFalse(self.portfolio_two._is_sellable(symbol, quantity))

    def test_buy_stock(self):
        symbol = 'msft'
        quantity = 20
        price = 100
        self.portfolio_one.buy_stock(symbol, quantity, price)
        self.assertEqual(self.portfolio_one.buy_power, 100000 - (quantity * price))
        self.assertEqual(self.portfolio_one.stocks[symbol], 20)

    def test_buy_stock_error(self):
        symbol = 'amzn'
        quantity = 200
        price = 1000
        self.assertRaises(ValueError, lambda: self.portfolio_two.buy_stock(symbol, quantity, price))

    def test_sell_stock(self):
        symbol = 'goog'
        quantity = 100
        price = 1000
        self.portfolio_three.sell_stock(symbol, quantity, price)
        self.assertEqual(self.portfolio_three.buy_power, 150000 + (price * quantity))
        self.assertEqual(self.portfolio_three.stocks[symbol], 100)

    def test_sell_stock_error(self):
        symbol = 'goog'
        quantity = 201
        price = 1000
        self.assertRaises(ValueError, lambda: self.portfolio_three.sell_stock(symbol, quantity, price))

    def test_get_portfolio(self):
        port_str = self.portfolio_one.get_portfolio()
        self.assertEqual(port_str, '{"name": "one", "buy_power": 100000, "stocks": {}}')
        port_str = self.portfolio_three.get_portfolio()
        self.assertEqual(port_str, '{"name": "three", "buy_power": 150000, "stocks": {"aapl": 150, "goog": 200}}')
