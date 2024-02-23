class BaseMobOperator:

    def __init__(self, name, call_price, text_price):
        self.name = name
        self.__call_price = call_price
        self.__text_price = text_price

    def make_call(self):
        pass

    def send_text(self):
        pass

    @property
    def price_of_call(self):
        return self.__call_price

    @property
    def price_of_message(self):
        return self.__text_price

