import json, config, requests

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

    def get_stock_price(self, input):
        # ADD SAFEGUARD AGAINST INVALID TICKERS
        url = 'https://finnhub.io/api/v1/quote?symbol=' + str(input) + '&token=' + str(config.finhub_key)
        r = requests.get(url)
        temp = r.json()
        return temp['c']


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