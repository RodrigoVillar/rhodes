import json, config, requests

class FrontEnd(object):

    def get_json(self):
        return json.dumps(self.__dict__)

class Stocks(FrontEnd):

    def __init__(self):
        self.favorite_stocks = []

    def run(self):
        while True:
            self.run_instructions()
            while True: 
                command = input("Please input a command here: ")
                if command == 'view-favorites':
                    print("Your current stock favorites consists of the following: " + str(self.favorite_stocks))
                    self.continue_instructions()
                elif command == 'remove-favorite':
                    print("Your current stock favorites consists of the following: " + str(self.favorite_stocks))
                    stock = input("Please input the stock which you wish to remove: ")
                    self.delete_favorite_stock(stock)
                    self.continue_instructions()
                elif command == 'view-current-price':
                    stock = input("Please input a stock ticket to see its current price: ")
                    price = self.get_stock_price(stock)
                    print("The current price of " + stock + " is $" + str(price))
                    self.continue_instructions()
                elif command == 'back':
                    return
                else:
                    print("That command is invalid!")


    def run_instructions(self):
        print("Welcome to the Stocks Section of Rhodes!")
        print("The following commands are available to you:")

    def continue_instructions(self):
        print("You can continue to use any other command in the Stocks section of Rhodes")
        print("Additionally, you can type in 'back' to go back to the main screen")

    def add_favorite_stock(self, input):
        self.favorite_stocks.append(input)
        print(self.favorite_stocks)

    def delete_favorite_stock(self, input):
        self.favorite_stocks.remove(input)

    def get_stock_price(self, input):
        # ADD SAFEGUARD AGAINST INVALID TICKERS IN FUTURE
        url = 'https://finnhub.io/api/v1/quote?symbol=' + str(input) + '&token=' + str(config.finhub_key)
        r = requests.get(url)
        temp = r.json()
        return temp['c']


class Options(FrontEnd):

    def __init__(self):
        self.favorite_options = []

    def run(self):
        print("run!")

    def add_favorite_option(self, input):
        self.favorite_options.append(input)

    def delete_favorite_option(self, input):
        self.favorite_options.remove(input)

class Crypto(FrontEnd):

    def __init__(self):
        self.favorite_cryptos = []

    def run(self):
        print("run!")

    def add_favorite_crypto(self, input):
        self.favorite_cryptos.append(input)

    def delete_favorite_crypto(self, input):
        self.favorite_crypto.remove(input)