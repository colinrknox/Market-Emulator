from abc import abstractmethod, ABCMeta

class TransactionResponse(metaclass=ABCMeta):

    @staticmethod
    @abstractmethod
    def generate(self, symbol, quantity, price):
        raise NotImplementedError(f'Subclass {self.__class__.__name__} needs to implement Command.execute()')


class BuyStockResponse(TransactionResponse):

    def generate(self, symbol, quantity, price):
        return f'Bought {quantity} share{"s" if quantity > 1 else ""} of {symbol} stock for ${price} each.\n\
                 Total purchase was ${price * quantity}.'


class SellStockResponse(TransactionResponse):

    def generate(self, symbol, quantity, price):
        return f'Bought {quantity} share{"s" if quantity > 1 else ""} of {symbol} stock for ${price} each.\n\
                 Total sale was ${price * quantity}.'
