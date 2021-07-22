"""
The main class for Rhodes

This module acts as the head of the program, as this is where the user is taken to once they log in and for the
most part, most actions they take here will begin here and continue in another module. 
"""

import front_end
import datetime
import json
import datetime


class Rhodes(object):

    """
    Main Object of Rhodes Software

    Attribute username: the username of the user
    Invariant: handled by script.py

    Attribute date_joined: the data/time which the user first created their Rhodes account
    Invariant: date_joined is a tuple that is ordered as the following: year, month, day, hour, minute, second

    Attribute stocks_obj: the stocks object assigned to the user
    Invariant: stocks_obj is of type Stocks

    Attribute options_obj: the options object assigned to the user
    Invariant: options_obj is of type Options

    Attribute crypto_obj: the crypto object assigned to the user
    Invariant: crypto_obj is of type Crypto
    """

    def __init__(self, username=False):
        """
        Parameter username: the username of the user
        Invariant: handled by script.py

        Initializer for Rhodes. If the user is new, script.py passes no arguments which Rhodes renders as username = False. 
        If the user already has an account, the initializer loads the jsons for each component of Rhodes and initializes those components
        into objects.
        """

        if username == False:
            self.date_joined = self.set_date_joined()
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
            with open(directory + '/rhodes.json') as rho:
                rhodes_data = json.load(rho)

            self.stocks_obj = front_end.Stocks(stock_data)
            self.options_obj = front_end.Options(options_data)
            self.crypto_obj = front_end.Crypto(crypto_data)

            self.stocks_obj.set_username(username)
            self.crypto_obj.set_username(username)
            self.options_obj.set_username(username)

            self.stocks_obj.save()
            self.crypto_obj.save()
            self.options_obj.save()

            self.date_joined = rhodes_data['date_joined']
            self.username = username

            print('\nWelcome back ' + username + '!')

    # The following deals with the terminal interface

    def set_date_joined(self):
        """
        Helper function for __init__()

        This method is to be used when creating the profile of a new user. When called, this method
        initializes a datetime object which data will be pulled from. A list is then created, and all
        necessary values (year, month, day, hour, minute, second) is apended to the list. This method
        then returns the tuple form of the list
        """
        temp = datetime.datetime.now()

        date_list = []
        date_list.append(temp.year)
        date_list.append(temp.month)
        date_list.append(temp.day)
        date_list.append(temp.hour)
        date_list.append(temp.minute)
        date_list.append(temp.second)

        return tuple(date_list)

    def set_username(self, input):
        """
        Helper method for __init__()

        This method is meant to be user by script.py in the case that the user is new. Since entering a new user's username
        into the Rhodes initializer would make the code believe that the user is already existing, this method is to be called from 
        script.py to manually set the username of the new user.

        Parameter input: the username of the new user
        Precondition: handled by script.py
        """
        self.username = input
        self.stocks_obj.set_username(input)

    def run(self):
        """
        The method responsible for the Rhodes user experience

        When called, this method starts a while loop that is initially True; this outer while loop is what keeps the Rhodes from closing
        after closing one of its component. The inner while loop (also initially True) is tasked with asking the user for their command
        which will lead them to a component or to exit the program.
        """
        while True:
            print("\nWeclome to Rhodes! We currently offer tools catered to those investing in stocks, options, and cryptocurrencies!\n")
            while True:
                print("The following commands are available: 'stocks' - takes you to the stocks section, \
'options' - takes you to the options section, 'crypto' - takes you to the crypto section, 'user-info' - returns information about the user. \
Additionally, entering 'exit' will let you end this session of Rhodes.\n")
                command = input("Please enter a command here: ")
                if command == 'stocks':
                    self.stocks_obj.run()
                elif command == 'options':
                    self.options_obj.run()
                elif command == 'crypto':
                    self.crypto_obj.run()
                elif command == 'nimos':
                    print("you selected nimos!")
                elif command == 'exit':
                    self.save()
                    quit()
                elif command == 'user-info':
                    self.get_user_info()
                else:
                    print("Please enter a valid command!")

    def get_user_info(self):
        """
        When called, this method prints information regarding the user's account
        """
        x = datetime.datetime(self.date_joined[0], self.date_joined[1],
                              self.date_joined[2], self.date_joined[3], self.date_joined[4])
        print("Username: " + self.username)
        print("Date Joined: " + x.strftime("%B") + ' ' +
              x.strftime("%d") + ', ' + x.strftime("%Y") + '.')

    def save(self):
        """
        This method is responsible for saving the attributes of the user's Rhodes object whenever
        they exit the program and saves it to the user's respective rhodes.json file
        """

        result = {
            'date_joined': self.date_joined,
            'username': self.username
        }
        with open('user_data/' + self.username + '/rhodes.json', 'w') as file:
            json.dump(result, file)
