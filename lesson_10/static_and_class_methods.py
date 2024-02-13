# @staticmethod
# classmethod


# class SQLQueries:
#
#     products_table = 'products'
#
#     @staticmethod
#     def get_user_by_name(user_name):
#         return f'Select * from user_table where user="{user_name}";'
#
#     @classmethod
#     def get_product_by_id(cls, product_id):
#         return f'Select * from {cls.products_table} where id={product_id};'
#
#
#
# user_query = SQLQueries.get_user_by_name('Denys')
# product_query = SQLQueries.get_product_by_id(5)
# print(user_query)
# print(product_query)


# class BaseCar:
#     car_type = 'Base'
#
#     def __init__(self, engine: str, model: str, color: str = 'Blue') -> None:
#         self.engine = engine
#         self.model = model
#         self.color = color
#
#     @classmethod
#     def print_car_type(cls):
#         print(cls.car_type)
#
#     @staticmethod
#     def print_hi():
#         print('Hi')


# car = BaseCar(engine='v8', model='asd')
# car.car_type = 'New car type'
# car.print_car_type()
# BaseCar.print_car_type()
# BaseCar.print_hi()

# інкапсуляція

import time


# public, protected, private
class Worker:

    def __init__(self, name, bd):
        self.name = name         # public
        self._birth_day = bd     # protected
        self.__sallary = 1000    # private


    def is_bd_today(self):
        today = "20-08"
        if today == self._birth_day:
            print('Happy BD')

    def start_work(self):
        self.drink_coffee()
        self.turn_on_pc()

    def end_work(self):
        self.turn_off_pc()

    def drink_coffee(self):
        print("Coffee is drinking")

    def turn_on_pc(self):
        print('PC is tuned on')

    def turn_off_pc(self):
        print('PC is tuned off')



den = Worker('Denys', '20-08')

print(den.name)
print(den._birth_day)
print(den._Worker__sallary)
#
# den.start_work()
# den.end_work()
# den.drink_coffee()



# getter, setter