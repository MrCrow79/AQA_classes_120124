from lesson_13.phone_practise.phones.base_phone import BasePhone, BaseMobOperator
from lesson_13.phone_practise.mobile_apps.base_app import BaseApp


class IPhone(BasePhone):

    def __init__(self, model: str, mobile_operator: BaseMobOperator, memory_quantity: int):
        super().__init__(model, mobile_operator)
        self.__memory_quantity = memory_quantity
        self.apps = {}

    @property
    def free_memory(self):
        result = self.__memory_quantity
        for app in self.apps:  # {'name': instance}

            if self.apps[app].status is True:
                result -= self.apps[app].eat_memory

        return result

    def install_application(self, app: BaseApp):
        if self.apps.get(app.name):
            print('App already installed')
        else:
            self.apps[app.name] = app
            print('All was successfully installed')

    def uninstall_application(self, app: BaseApp):
        if self.apps.get(app.name):
            self.apps.pop(app.name)
        print(f'Your phone has no more {app.name}')

    def get_application(self, name) -> BaseApp:
        return self.apps.get(name)

    @property
    def full_memory(self):
        return self.__memory_quantity

    def __eq__(self, other):
        return self.full_memory == other.full_memory

    def __ge__(self, other):
        return self.full_memory >= other.full_memory

    def __gt__(self, other):
        return self.full_memory > other.full_memory

    def __le__(self, other):
        return self.full_memory <= other.full_memory

    def __lt__(self, other):
        return self.full_memory < other.full_memory
