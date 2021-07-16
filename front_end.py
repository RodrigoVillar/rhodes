import json

class FrontEnd(object):

    def get_json(self):
        return json.dumps(self.__dict__)

class Stocks(FrontEnd):


    def __init__(self):
        self.favorite_stocks = ["AAPL", "TSLA"]

    def add_favorite_stock(self, input):
        self.favorite_stocks.append(input)
        print(self.favorite_stocks)

    def delete_favorite_stock(self, input):
        self.favorite_stocks.remove(input)

class Options(FrontEnd):

    def __init__(self):
        self.favorite_options = []

    def add_favorite_option(self, input):
        self.favorite_options.append(input)

    def delete_favorite_option(self, input):
        self.favorite_options.remove(input)

class Crypto(FrontEnd):

    def __init__(self):
        self.favorite_cryptos = []

    def add_favorite_crypto(self, input):
        self.favorite_cryptos.append(input)

    def delete_favorite_crypto(self, input):
        self.favorite_crypto.remove(input)