from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self):
        self.wheel = 4
        self.color = None
        self.engine = None

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_fuel(self):
        pass
