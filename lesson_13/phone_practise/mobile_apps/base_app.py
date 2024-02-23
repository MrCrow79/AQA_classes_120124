class BaseApp:

    def __init__(self, name, eat_memory):
        self.name = name
        self.eat_memory = eat_memory
        self.__is_running = False

    def turn_on(self):
        print('app is turned on')
        self.__is_running = True

    def turn_off(self):
        print('app is turned off')
        self.__is_running = False

    @property
    def status(self):  # is running
        return self.__is_running
