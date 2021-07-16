import front_end
class Rhodes(object):
    """
    Main Object of Rhodes software

    Current Attributes: name, date_joined, stocks_obj, options_obj, crypto_obj
    """

    def __init__(self, name, date_joined):
        self.name = name
        self.date_joined = date_joined
        self.stocks_obj = front_end.Stocks()
        self.options_obj = front_end.Options()
        self.crypto_obj = front_end.Crypto()





        

    
