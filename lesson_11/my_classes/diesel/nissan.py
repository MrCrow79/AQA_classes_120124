from lesson_11.my_classes.diesel.base_diesel import DieselCar


class Nissan(DieselCar):

    def __init__(self):
        super().__init__()
        self.color = 'Black'

    def turn_on(self):
        print('Nissan turn on')

    def turn_off(self):
        print('Nissan turn of')

    def get_fuel(self):             # поліморфізм
        self.__check_diesel_money()
        print('Getting diesel')

    def __check_diesel_money(self):  #  інкапсуляцяя
        print('Checking money')
