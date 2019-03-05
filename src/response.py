from abc import abstractmethod, ABCMeta


class TransactionResponseFactory():

    def __init__(self):
        pass

    def createResponse(self, type):
        if type.lower() == "buy":
            return BuyStockResponse()
        elif type.lower() == "sell":
            return SellStockResponse()
        else:
            raise ValueError(f"Invalid message passed to {self.__class__.__name__}")


# Super class for defining transaction responses to be printed by the REPL in engine.py
class TransactionResponse(metaclass=ABCMeta):

    @abstractmethod
    def generate(symbol, quantity, price):
        raise NotImplementedError(f'Subclass {self.__class__.__name__} needs to implement {super().__class__.__name__}.execute()')


class BuyStockResponse(TransactionResponse):

    def generate(self, symbol, quantity, price):
        return f'Bought {quantity} share{"s" if quantity > 1 else ""} of {symbol} stock for ${price} each.\n\
                 Total purchase was ${price * quantity}.'


class SellStockResponse(TransactionResponse):

    def generate(self, symbol, quantity, price):
        return f'Bought {quantity} share{"s" if quantity > 1 else ""} of {symbol} stock for ${price} each.\n\
                 Total sale was ${price * quantity}.'
