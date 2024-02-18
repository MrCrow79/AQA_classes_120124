from lesson_11.my_classes.electic.base_electric import Elecric


class Tesla(Elecric):

    def __init__(self):
        super().__init__()
        self.color = 'red'

    def turn_on(self):
        print('Tesla turn on')

    def turn_off(self):
        print('Tesla turn of')

    def get_fuel(self):             # поліморфізм
        self.__check_accumulator()
        print('Charging')

    def __check_accumulator(self):  #  інкапсуляція
        print('Checking accumulator')


