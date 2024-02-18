# питання

# getter setter + privat, protected



# class Animals:
#
#     def __init__(self, name, age, count):
#         self.name = name  # public
#         self._age = age  # protected
#         self.__count = count  #  privat
#
#     def move_to(self, place):  # public
#         print('I\'m public')
#
#     def _eat(self, food):  # protected
#         print('I\'m protected')
#
#
#     def __calcilate_distance(self, food):  # privat
#         print('I\'m privat')

#
# horses = Animals('norse', 33, 12)
# print(horses.name)
# print(horses._age)
# print(horses._Animals__count)
# print(horses.move_to('asd'))
# print(horses._eat('asd'))
# print(horses._Animals__calcilate_distance('asd'))



# class Animal:
#
#     def __init__(self, a_type, name, age, count):
#         self.a_type = name
#         self.name = name
#         self.age = age
#         self.count = count
#         self.__sum_age_of_animals = None
#
#
#     def get_sum_age_of_animals(self):  # getter
#         if self.__sum_age_of_animals is None:
#             return self.count * self.age
#         else:
#             return self.__sum_age_of_animals
#
#
#     def set_sum_age_of_animals(self, value):  # setter
#         self.__sum_age_of_animals = value
#
#
# horses = Animal('horses', 'Antuan', 25, 10)
#
#
# horses.set_sum_age_of_animals(50)
# print(horses.get_sum_age_of_animals())


# class UserAuth:
#
#     def __init__(self, username: str, user_pass: str):
#         self.username = username
#         self.__user_pass = user_pass
#         self.__old_passwords = []
#
#
#     def get_password(self):
#         return self.__user_pass
#
#     def set_new_user_password(self, value, old_password):
#         if old_password == self.__user_pass:
#             self.__user_pass = value
#         else:
#             raise ValueError('Wrong password')
#
#
# den = UserAuth('den', '123')
# den.set_new_user_password('456', '123')
# den.set_new_user_password('789', '123')


# class UserAuth:
#
#     def __init__(self, username: str, user_pass: str):
#         self.username = username
#         self.__user_pass = user_pass
#         self.__old_passwords = []
#
#     @property
#     def password(self):
#         return self.__user_pass
#
#
#     @password.setter
#     def password(self, passwords: tuple):
#         old_password = passwords[0]
#         new_password = passwords[1]
#         if old_password == self.__user_pass:
#             self.__user_pass = new_password
#         else:
#             raise ValueError('Wrong password')
#
#
#
# den = UserAuth('den', '123')
#
# print(den.password)
# den.password = ('123', '456')
# print(den.password)
# den.password = ('123', '789')




# наслідування ієрархія


# class Animals:
#     base_type = 'Animals'
#     pass
#
#     def go_to_the_filed(self):
#         print('go_to_the_filed fo the Animals class')
#
# class Horses(Animals):
#
#     def __init__(self):
#         self.legs = 4
#         self.head = 1
#         self.food_type = 'gross'
#         self.colour = None
#         self.size = 180 # cm
#
#     def go_to_the_filed(self):
#         print('go_to_the_filed fo the Horses class')
#
# class AppleHorses(Horses):
#     base_type = 'AppleHorses'
#
#     def __init__(self):
#         super().__init__()
#         self.colour = 'brown with white'
#
#     def go_to_the_filed(self):
#         super().go_to_the_filed()  # super(AppleHorses, self).go_to_the_filed()
#         print('go_to_the_filed fo the AppleHorses class')
#
#     def go_to_the_filed_2(self):
#         super(Horses, self).go_to_the_filed()
#         print('go_to_the_filed_2 fo the AppleHorses class')
#
# class Poni(Horses):
#     base_type = 'Poni'
#
#     def __init__(self):
#         super().__init__()
#         self.colour = 'brown'
#         self.size = 100 # cm
#
#     def go_to_the_filed(self):
#         super().go_to_the_filed()  # super(AppleHorses, self).go_to_the_filed()
#         print('go_to_the_filed fo the AppleHorses class')
#
#     def go_to_the_filed_2(self):
#         super(Horses, self).go_to_the_filed()
#         print('go_to_the_filed_2 fo the AppleHorses class')


# Я хочу працювати з БД
# class BaseConnector:
#     pass
#
# class BaseDB:
#     pass
#
# class PostrgerConnect(BaseConnector):
#
#     def __init__(self):
#         super().__init__()
#         self.host = None
#         self.port = None
#         self.user = None
#         self.password = None
#         self.cursor = None
#
#
#     def connector(self):
#         self.cursor = cursor
#
#
#     def close_connection(self):
#         self.cursor.close()
#
#
# class PostgersSender(BaseDB):
#
#     def __init__(self, connector):
#         super().__init__()
#         self.connector = connector
#
#     def get_all_users(self):
#         return self.__seriallzie_response(self.connector.send_request())
#
#
#     def __seriallzie_response(response):
#         pass

#  issubclass, object


# print(issubclass(AppleHorses, Animals))
# print(issubclass(Animals, object))
# print(issubclass(AppleHorses, object))
#
# class Car:  # class Car(object)
#     pass

# base_hourse = Horses()
# antonio = AppleHorses()
# antonio.go_to_the_filed_2()

# print(antonio.base_type)
# print(antonio.colour)
# print(antonio.food_type)



# множинне наслідування

# class Animal():
#
#     def how_to_move(self):
#         return 'walk'
#
#
#     def fast_move(self):
#         return 'run'
#
#
# class Bird():
#
#     def how_to_move(self):
#         return 'fly'
#
#     def fast_fly(self):
#         return 'fast fly'
#
#
#
# class BirdAnimal(Bird, Animal): # страус
#     pass
#
# anibird = BirdAnimal()
#
# print(anibird.fast_fly())
# print(anibird.fast_move())
#
# print(anibird.how_to_move())


# кастомні атрибути поза init
# наслідування __init__
# super
# mro - механіз який вирішуе в якому порядку наслідуютсья класи


# class A: #  class A(object)
#     def method(self):
#         print("A.method() called")
#
# class B:
#     def method(self):
#         print("B.method() called")
#
# class C(A, B):
#     pass
#
#
#
# class D(C, B): # D -> C -> A -> B -> B
#     pass
#
# # print(D.mro())
# class D(B, C): # D -> B -> C -> A -> B
#     pass


# d = C()
# d.method()



# поліморфізм

# a = 1
# b = 2
# c = 'x'
# d = 'y'
#
# a + b
# c + d
# [1,2] + [3,4]


# абстракція


# from abc import ABC, abstractmethod
#
# class Car(ABC):
#
#     def __init__(self):
#         self.wheel = 4
#         self.color = None
#         self.engine = None
#
#     @abstractmethod
#     def turn_on(self):
#         pass
#
#     @abstractmethod
#     def turn_off(self):
#         pass
#
#     @abstractmethod
#     def get_furel(self):
#         pass
#
#
# class Tesla(Car):
#     def __init__(self):
#         super().__init__()
#         self.engine = 'electic'
#
#     def turn_on(self):
#         print('Tesla start')
#
#     def turn_off(self):
#         print('Tesla stop')
#
#     def get_furel(self):
#         print('Charging')
#
#
# class Nissan(Car):
#     def __init__(self):
#         super().__init__()
#         self.engine = 'diesel'
#
#     def turn_on(self):
#         print('Nissan start')
#
#     def turn_off(self):
#         print('Nissan stop')
#
#     def get_furel(self):
#         print('Get diesel')
#
#
# tesla = Tesla()
#
# tesla.turn_on()
# tesla.turn_off()
# tesla.get_furel()
#
# nissan = Nissan()
# nissan.turn_on()
# nissan.turn_off()
# nissan.get_furel()  #


from lesson_11 import Tesla, Nissan

nissan = Nissan()
tesla = Tesla()


# slots























