from lesson_11.my_classes.base_car import Car
from abc import abstractmethod


class Elecric(Car):

    def __init__(self):
        super().__init__()
        self.engine = 'electric'

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_fuel(self):
        pass