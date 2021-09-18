"""
The front-end module for Rhodes

This module contains the three classes that make up most of the Rhodes experience: Stocks, Options, Crypto. All three
of these classes inherit from the class FrontEnd, which contains the method/attribute that they have in common.
"""

import json
import config
import requests


class FrontEnd(object):

    """
    The class that Stocks, Options, Crypto inherit from.

    Attribute username: the username of the user
    Invariant: handled by script.py
    """

    def get_json(self):
        """
        Returns a JSON of the object it is called from
        """

        return json.dumps(self.__dict__)

    def set_username(self, input):
        """
        When called, this function sets the username attribute of the object equal to input

        Parameter input: the username of the user
        Invariant: handled by script.py
        """

        self.username = input


class Stocks(FrontEnd):

    """
    The class that handles anything stock related AND relating to the front-end experience.

    Stocks is meant to fulfill any tasks relating to 1) accessing real-time/historical data from stock market and 2) storing
    stock data related to the user.

    Attribute favorite_stocks: a list of the user's favorite stocks
    Invariant: each element of favorite_stocks contains a string that is a valid stock ticker
    """

    def __init__(self, data={}):
        """
        Initializer for Stocks

        This initializer accounts for the two cases: if the user is new (or if the user has never accessed the stocks
        component of Rhodes), no argument is entered and as a result, the attribute favorite_stocks is set equal to an
        empty list. If the user has already used the stocks component of Rhodes in the past, a dictionary containing the user's
        Stocks data is sent through the data parameter and the initializer sets the attributes equal to its equivalent
        keys

        Parameter data: a dictionary containing the Stocks data of the user
        Precondition: data is a dictionary whose key-pairs are derived from a Stocks object
        """

        if data == {}:  # If data is empty (in this case, a new user)
            self.favorite_stocks = []
        else:
            self.favorite_stocks = data['favorite_stocks']
            self.username = data['username']

    def run(self):
        """
        The method responsible for the Stocks user experience

        When called, this method starts a while loop that is initially True; this while loop is responsible for keeping the program
        running after a user enters a command. The inner while loop (also initially True) is tasked with asking the user for
        a command, which will lead to the specific command being executed or the user returning to the Rhodes home screen
        """
        while True:
            self.run_instructions()
            while True:
                command = input("Please input a command here: ")
                if command == 'view-favorites':
                    print(
                        "Your current stock favorites consists of the following: " + str(self.favorite_stocks))
                    self.continue_instructions()
                elif command == 'remove-favorite':
                    print(
                        "Your current stock favorites consists of the following: " + str(self.favorite_stocks))
                    stock = input(
                        "Please input the stock which you wish to remove: ")
                    self.delete_favorite_stock(stock)
                    self.continue_instructions()
                elif command == 'add-favorite':
                    stock = input(
                        "Please enter the ticker of the stock you wish to add to your favorites list: ")
                    self.add_favorite_stock(stock)
                    self.continue_instructions()
                elif command == 'view-current-price':
                    stock = input(
                        "Please input a stock ticket to see its current price: ")
                    self.get_stock_price(stock)
                    self.continue_instructions()
                elif command == 'back':
                    self.save()
                    return
                else:
                    print("That command is invalid!")

    def save(self):
        """
        This method is responsible for saving the attributes of the user's Stocks object to its respective JSON file every
        time the user exits the program.
        """
        with open('user_data/' + self.username + '/stocks.json', 'w') as file:
            json.dump(self.__dict__, file)

    def run_instructions(self):
        """
        When called, this method prints a welcome message along with the commands that are available to the user
        """
        print("Welcome to the Stocks Section of Rhodes!")
        print("The following commands are available to you: 'view-favorites' - returns a list of your current favorite stocks, \
'add-favorite' - allows you to add a stock to your favorites list, 'remove-favorite' - allows you to remove one of your favorite stocks,\
'view-current-price' - allows you to view the current price of a stock, 'back' - returns you to the main menu of Rhodes.")

    def continue_instructions(self):
        """
        When called, this method reminds the user that they can type in another command
        """
        print("You can continue to use any other command in the Stocks section of Rhodes")
        print("Additionally, you can type in 'back' to go back to the main screen")

    def add_favorite_stock(self, input):
        """
        This method appends input to attribute favorite_stocks

        Attribute input: the stock to be added to favorite_stocks
        Precondition: input is a valid stock ticker
        """
        url = "https://www.alphavantage.co/query?function=OVERVIEW&symbol=" + \
            str(input) + "&apikey=" + str(config.alpha_vantage_key)
        r = requests.get(url)
        temp = r.json()
        if temp == {}:
            print("That is not a valid stock ticker, please try again!")
        else:
            self.favorite_stocks.append(input)
            print("Successfully added " + input +
                  " to your favorite stocks list!")

    def delete_favorite_stock(self, input):
        """
        This method removes input from attribute favorite_stocks

        Attribute input: the stock to be removed from favorite_stocks
        Precondition: input is an element of favorite_stocks
        """
        stock_present = False
        for x in self.favorite_stocks:
            if x == input:
                stock_present = True
        if stock_present:
            self.favorite_stocks.remove(input)
            print("You have successfully removed " +
                  input + " from your favorite stocks list!")
        else:
            print("Sorry, but this stock isn't present in your favorite stocks list.\n")

    def get_stock_price(self, input):
        """
        This method returns the real-time price of input

        Parameter input: the stock to get the current price of
        Precondition: input is a valid stock ticker
        """
        # ADD SAFEGUARD AGAINST INVALID TICKERS IN FUTURE
        url = 'https://finnhub.io/api/v1/quote?symbol=' + \
            str(input) + '&token=' + str(config.finhub_key)
        r = requests.get(url)
        temp = r.json()
        if temp['c'] == 0:
            print("Sorry, but that isn't a valid stock ticker.")
        else:
            print("The current stock price of " +
                  input + " is $" + str(temp['c']))


class Options(FrontEnd):

    """
    This class handles anything related to options trading AND that is related to the user experience

    NOT TO BE USED, STILL IN DEVELOPMENT
    """

    def __init__(self, data={}):
        self.favorite_options = []

    def run(self):
        print("run!")

    def add_favorite_option(self, input):
        self.favorite_options.append(input)

    def delete_favorite_option(self, input):
        self.favorite_options.remove(input)

    def save(self):
        with open('user_data/' + self.username + '/options.json', 'w') as file:
            json.dump(self.__dict__, file)


class Crypto(FrontEnd):

    """
    This class handles anything related to cryptocurrency trading AND that is related to the user experience

    Crypto is meant to handle the following:

    * Access real-time/historical cryptocurrency data *
    * Store cryptocurrency data relating to the user *

    Attribute favorite_cryptos: a list of the user's favorite cryptocurrencies
    Invariant: favorite_cryptos is a list, with each element being a string that represents the valid ticker of a cryptocurrency
    """

    def __init__(self, data={}):
        """
        Initializer for Crypto

        This initializer accounts for two possibilities: if the user is new (or has never accessed the crypto section of Rhodes),
        then data is, by default, set to an empty dictionary and as a result, attribute favorite_cryptos is set equal to an empty
        list. If the user has accessed the Crypto component in the past, then the initializer fetches the user's crypto.json file
        and matches each attribute to its equivalent key-pair value.
        """
        if data == {}:
            self.favorite_cryptos = []
        else:
            self.favorite_cryptos = data["favorite_cryptos"]
            self.username = data["username"]

    def run(self):
        """
        The method responsible for the Crypto user experience

        When called, run() starts a while loop that is set to True, which makes sure that the Crypto component
        doesn't end after the user enters a command. Inside the while loop is another while loop (which is also
        initially True); the inner while loop is tasked with making sure the user enters a command
        """

        while True:
            self.run_instructions()
            while True:
                command = input("Please enter a command: ")
                if command == 'back':
                    self.save()
                    return
                elif command == 'view-favorites':
                    print("Your current crypto favorites consist of the following: " +
                          str(self.favorite_cryptos))
                    self.continue_instructions()
                elif command == 'add-favorite':
                    temp = input(
                        "Please enter the cryptocurrency which that you wish to add to your favorites list: ")
                    self.add_favorite_crypto(temp)
                    self.continue_instructions()
                elif command == 'get-current-price':
                    temp = input(
                        "Please enter the cryptocurrency which you wish to get the price of: ")
                    value = self.get_current_price(temp)
                    print("The current price of " + str(temp) + " is " + value)
                    self.continue_instructions()
                else:
                    print("That command is invalid!")

    def run_instructions(self):
        """
        When called, this method prints out a welcome message while also displaying the commands
        available to the user
        """

        print("Welcome to the Cryptocurrency Section of Rhodes!")
        print("The following commands are available to you: ")
        print("Additionally, you can enter 'back' to return to the home screen of Rhodes")

    def continue_instructions(self):
        """
        Meant to be used after a user enters a command

        When called, this method reminds the user of the commands available to them.
        """

        print("The following commands are available to you: ")
        print("Additionally, you can enter 'back' to return to the home screen of Rhodes")

    def add_favorite_crypto(self, input):
        """
        When called, this method appends input to favorite_cryptos

        Parameter input: the cryptocurrency to be added to favorite_cryptos
        Precondition: input is a valid cryptocurrency ticker
        """

        self.favorite_cryptos.append(input)

    def delete_favorite_crypto(self, input):
        """
        When called, this method removes input from favorite_cryptos

        Parameter input: the cryptocurrency to be removed from favorite_cryptos
        Precondition: input is an element of favorite_cryptos
        """

        self.favorite_crypto.remove(input)

    def get_current_price(self, input):
        """
        When called, this method returns the price of input

        Parameter input: the cryptocurrency to get the real-time price of
        Precondition: input is a valid cryptocurrency ticker
        """

        url = "https://api.nomics.com/v1/currencies/ticker?key=" + config.nomics_key + \
            "&ids=" + str(input) + \
            "&interval=1d&convert=USD&per-page=100&page=1"
        r = requests.get(url)
        r_json = r.json()
        return str(r_json["price"])

    def save(self):
        """
        This method is responsible for saving the attributes of the user's Stocks object to its respective JSON file every
        time the user exits the program.
        """

        with open('user_data/' + self.username + '/crypto.json', 'w') as file:
            json.dump(self.__dict__, file)
