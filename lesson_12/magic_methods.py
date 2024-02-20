

# __new__, коли викликаеться, що можна робити

# class Car:  # (object):  # наслідується від object
#
#     instance = None
#
#     def __new__(cls, model, engine):
#         if not cls.instance:
#             cls.instance = super().__new__(cls)
#         return cls.instance
#
#     def __init__(self, model, engine):
#         self.model = model
#         self.engine = engine
#
#
# tesla1 = Car('modelT', 'electric')
# tesla2 = Car('modelT', 'electric')
#
# print(id(tesla1))
# print(id(tesla2))


# __str__, __repr__


class Car:  # (object):  # наслідується від object

    # __slots__ = ["model", "engine", "__security_level", "color"]  # обмеження атрибутив

    def __init__(self, model, engine):
        self.model = model
        self.engine = engine
        self.__security_level = 9

    def __str__(self):  # друкування об'єкта
        return f'my str {self.model}'

    def __repr__(self):  # репрезентація
        return f'Car(model={self.model}, engine={self.engine})'

    # print(str(tesla1))
    # print(repr(tesla1))

    def __bool__(self):  # __bool__
        if len(self.model) > 0:
            return True
        else:
            return False
        # print(bool(tesla1))
        # print(bool(unknown))

    # def __del__(self):
    #     print(f'object Car {self.model}, {self.engine} was deleted')

    # del tesla1
    # del unknown

    def __getattr__(self, key): # __getattr__ - неіснуючий атрибут
        self.key = None  # default value
        return self.key


    def __getattribute__(self, key: str):  # при кожній спробі отримати атрибут
        # print(f'User wants to know value of {key}')
        if key.startswith(f'_Car_'):
            print('Access denied')
        else:
            return super().__getattribute__(key)

    # def __setattr__(self, key, value):
    #     print('SetAttr')
    #     super().__setattr__(key, value)



tesla1 = Car('modelT', 'electric')
tesla2 = Car('modelT', 'electric')
# unknown = Car('', '')

tesla1.color = 'red'
tesla1.car_type = 'electro'
# print(tesla1.model)
# print(tesla1.color)

# print(hasattr(tesla1, "model"))
# print(hasattr(tesla1, "model2"))
# print(tesla1.__dict__)
#
# property_list = ['model', 'color']
#
# for key in property_list:
#     if tesla1.__dict__.get(key) != tesla2.__dict__.get(key):
#         raise AttributeError(f'There is no {key}')

# for k in tesla1.__dir__():
#     print(k)



# print(tesla1._Car__security_level)





# композиція
# class Button:
#
#     def click_button(self):
#         print("Press")
#
#
# class TurnOnButton(Button):
#
#     def click_button(self):
#         print("Turn on button was clicked")
#
#
# class VolumeOnButton(Button):
#
#     def click_button(self):
#         print("Volume on  button was clicked")
#
#
# class Phone:
#
#     def __init__(self, model, os):
#         self.model = model
#         self.os = os
#
#
# class Android(Phone):
#
#     def __init__(self,  model, version, turn_on_button: Button, volume_on_button: Button):
#         super().__init__(model=model, os='Android')
#         self.version = version
#         self.turn_on_button = turn_on_button
#         self.volume_on_button = volume_on_button
#
#
# my_turn_on_button = TurnOnButton()
# my_volume_on_button = VolumeOnButton()
# android = Android('onePlus 8t', '16', my_turn_on_button, my_volume_on_button)
#
# # print(android.version)
# android.turn_on_button.click_button()
# android.volume_on_button.click_button()





# property
# class A:
#
#     def __init__(self):
#         self.__a = 1
#
#     @property
#     def a(self):
#         return self.__a
#
#     @a.setter
#     def a(self, value):
#         if isinstance(value, int):
#             self.__a = value
#
#     def get_a(self):
#         return self.__a
#
#     def set_a(self, value):
#         if isinstance(value, int):
#             self.__a = value
#
#
# inst_a = A()
#
# print(inst_a.a)
#
# inst_a.a = 10
# inst_a.set_a(10)
# print(inst_a.a)
