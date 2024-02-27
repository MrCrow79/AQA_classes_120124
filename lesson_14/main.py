# DRY
# don't repeat yourself
#
# import os
#
#
# class Animal:
#
#     def __init__(self, name, age, type):
#         self.name = name
#         self.age = age
#         self.type = type
#
#     def print_animal_name_and_age(self):
#         print(get_name_age_of_object(self))
#
#     @staticmethod
#     def print_cur_env():
#         def_print_current_env()
#
#
# class Car:
#
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def get_car_name_and_age(self):
#         return get_name_age_of_object(self)
#
#     @staticmethod
#     def print_cur_env():
#         def_print_current_env()
#
#
# def get_name_age_of_object(obj):
#     return f'{obj.name} is {obj.age} old'
#
#
#
# def def_print_current_env():
#     print(os.getenv('env_cur'))
#
#
# Car.print_cur_env()
# Animal.print_cur_env()


# KISS(example with len> 0 and number !=0 )


# class Train:
#     wagons = [[], [], [], []] #  first is locomotive, 2,3,4 is wagons
#
#     def add_passager(self, name, wagon_number):
#
#         if wagon_number < len(self.wagons):  # wagon існує
#             if wagon_number != 0:  # не локомотив
#                 if len(self.wagons[wagon_number]) < 10:  # кількість пасажирів в вагоні
#                     self.wagons[wagon_number].append(name)
#                 else:
#                     print('No free places')
#             else:
#                 print('You cant add to locomotive')
#         else:
#             print('wagon does not exist')
#
#
#     def add_passager_2(self, name, wagon_number):
#
#         if wagon_number >= len(self.wagons):  # wagon існує
#             print('wagon does not exist')
#             return
#         if wagon_number == 0:  # не локомотив
#             print('You cant add to locomotive')
#             return
#         if len(self.wagons[wagon_number]) >= 10:  # кількість пасажирів в вагоні
#             print('No free places')
#             return
#
#         self.wagons[wagon_number].append(name)



#  Single Responsibility: принцпи единої відповідальності(RentCar: find, book, print details, send message)

# class RentCar:
#
#     # def find_car(self): окремий класс
#     #     pass
#
#     def book_car(self):
#         pass
#
#     # def print_details(self):
#     #     pass
#
#
# class PrintCarDetails:
#
#     def __init__(self, car_obj):
#         self.car = car_obj
#
#     def print_base_details(self):
#         pass
#
#     def print_full_details(self):
#         pass


#  Open closed Principle: принцип закритості-відкритості(Send notification)


class BaseAccount:

    def __init__(self, user, card, balance):
        self.user = user
        self.card = card
        self.balance = balance

    def get_user_info(self):
        return f'{self.user} has {self.card} with {self.balance} UAH'



class NonInternetAccount(BaseAccount):

    def open_debit_card(self):
        pass


class MonoAccount(NonInternetAccount):

    def __init__(self, user, card, balance):
        super().__init__(user, card, balance)

    def open_credit_card(self):
        pass


class UkrsibAccount(BaseAccount):

    def __init__(self, user, card, balance):
        super().__init__(user, card, balance)
        pass


class InternetAccount(BaseAccount):

    def __init__(self, user, card, balance):
        super().__init__(user, card, balance)







#  Liskov substitution: принцип підстановка Барбари Лісков(розширення, не доповнення), Батько vs Син(Bank account: Salary with payment, Deposit without payment)


# class BaseAccount:
#
#     def __init__(self, user, card, balance):
#         self.user = user
#         self.card = card
#         self.balance = balance
#
#     def get_user_info(self):
#         return f'{self.user} has {self.card} with {self.balance} UAH'
#
#
# class MonoAccount(BaseAccount):
#
#     def __init__(self, user, card, balance):
#         super().__init__(user, card, balance)
#
#     def open_credit_card(self):
#         pass
#
#     def open_debit_card(self):
#         pass
#
#
# class UkrsibAccount(BaseAccount):
#
#     def __init__(self, user, card, balance):
#         super().__init__(user, card, balance)
#
#     def open_debit_card(self):
#         pass
