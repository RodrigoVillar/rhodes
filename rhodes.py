import front_end
import datetime
import json


class Rhodes(object):
    """
    Main Object of Rhodes software

    Current Attributes: name, date_joined, stocks_obj, options_obj, crypto_obj
    """

    # The following methods deals with IF a new user is being created
    def __init__(self, username=False):
        if username == False:
            self.date_joined = str(datetime.datetime.now())
            self.stocks_obj = front_end.Stocks()
            self.options_obj = front_end.Options()
            self.crypto_obj = front_end.Crypto()
            self.username = ''
        else:
            directory = 'user_data/' + str(username)  # Sets directory

            stock_data = {}  # Sets variables for data to be pasted into
            options_data = {}
            crypto_data = {}

            with open(directory + '/stocks.json') as stck:
                stock_data = json.load(stck)
            with open(directory + '/options.json') as opt:
                options_data = json.load(opt)
            with open(directory + '/crypto.json') as crypto:
                crypto_data = json.load(crypto)

            self.stocks_obj = front_end.Stocks(stock_data)
            self.options_obj = front_end.Options(options_data)
            self.crypto_obj = front_end.Crypto(crypto_data)

            self.stocks_obj.set_username(username)
            self.crypto_obj.set_username(username)
            self.options_obj.set_username(username)

            self.stocks_obj.save()
            self.crypto_obj.save()
            self.options_obj.save()

            print('\nWelcome back ' + username + '!')

    # The following deals with the terminal interface
    def set_username(self, input):
        self.username = input
        self.stocks_obj.set_username(input)

    def run(self):
        while True:
            print("\nWeclome to Rhodes! We currently offer tools catered to those investing in stocks, options, and cryptocurrencies!\n")
            while True:
                print("The following commands are available: 'stocks' - takes you to the stocks section, \
'options' - takes you to the options section, 'crypto' - takes you to the crypto section. Additionally, entering 'exit' will let you end this session of Rhodes.\n")
                command = input("Please enter a command here: ")
                if command == 'stocks':
                    self.stocks_obj.run()
                elif command == 'options':
                    self.options_obj.run()
                elif command == 'crypto':
                    self.options_obj.run()
                elif command == 'nimos':
                    print("you selected nimos!")
                elif command == 'exit':
                    quit()
                else:
                    print("Please enter a valid command!")
