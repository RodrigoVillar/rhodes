import front_end, datetime
class Rhodes(object):
    """
    Main Object of Rhodes software

    Current Attributes: name, date_joined, stocks_obj, options_obj, crypto_obj
    """

    # The following methods deals with IF a new user is being created
    def __init__(self, name):
        self.name = name
        self.date_joined = str(datetime.datetime.now())
        self.stocks_obj = front_end.Stocks()
        self.options_obj = front_end.Options()
        self.crypto_obj = front_end.Crypto()

    # The following deals with the terminal interface

    def run(self):
        while True:
            print("\nWeclome to Rhodes! We currently offer tools catered to those investing in stocks, options, and cryptocurrencies!\n")
            print("The following commands are available: 'stocks' - takes you to the stocks section, \
'options' - takes you to the options section, 'crypto' - takes you to the crypto section. Additionally, entering 'exit' will let you end this session of Rhodes.\n")
            while True:
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





        

    
