# create class syntax


# class BaseCar:
#     engine = 'v8'  # attribute
#     model = None
#
#     def my_method(self):  # method
#         print('my_method calls')
#
#
# # Instances(екземпляри)
# # artts, methods
# base_car1 = BaseCar()
# base_car2 = BaseCar()
# base_car3 = BaseCar()
#
# print(id(base_car1))
# print(id(base_car2))
# print(id(base_car3))
# print('------------')
# base_car1.model = 'tesla'
# base_car1.color = 'blue'
# print(base_car1.color)
# print(base_car1.engine)
# print(base_car2.engine)
# print(base_car3.engine)
# base_car3.my_method()




# init


# class BaseCar:
#
#     # def __new__(cls, *args, **kwargs):
#     #     return super().__new__(cls)
#
#     #
#     # def __del__(self):
#     #     ...
#
#     def __init__(self, engine: str, model: str, color: str = 'Blue') -> None:
#         self.engine = engine
#         self.model = model
#         self.color = color
#         self.car_type = 'Base'
#
#     def print_engine(self):
#         print(self.engine)

        # def __eq__(self, other):
        # a = 'asd'
        #
        # a == 'asd'  # == a.__eq__('asd')
        # __new__, __del__


# my_tesla = BaseCar(engine='electric', model='t9')
# my_nissan = BaseCar(engine='v8', model='nano', color='Red')
# my_tesla.print_engine()  # == BaseCar.print_engine(my_tesla)
# my_nissan.print_engine()  # == BaseCar.print_engine(my_nissan)

# print(id(my_tesla.color))
# print(id(my_nissan.color))


# import

# Досутп до атрибути інстанса, доступ до атрібута класса(ззовні і зсередини)



# class BaseCar:
#
#     home_countries = ['Japan, USA']  # class attribute -  спільні для всіх інстансів
#     home_countries_2 = []  # class attribute -  спільні для всіх інстансів
#
#     def __init__(self, engine: str, model: str, color: str = 'Blue') -> None:
#         self.engine = engine  # для кожного instance свої
#         self.model = model
#         self.color = color
#         self.prices = []
#
#     def print_engine(self):
#         print(self.engine)
#
#     def add_price(self, price=1000):
#         self.price = price
#
#
# my_nis = BaseCar(model='pathfinder', engine='v6')  # створенні екземпляра(instance)
# my_tla = BaseCar(model='t9', engine='electr')
# my_tyo = BaseCar(model='t9', engine='v8')

#
# print(id(my_nis.home_countries_2))
# print(id(my_tla.home_countries_2))
# print(id(my_tyo.home_countries_2))
#
#
# print('-----')
# print(id(my_nis.prices))
# print(id(my_tla.prices))
# print(id(my_tyo.prices))

# my_nis.home_countries = ['Italy']  # add to self object
# my_tla.home_countries = ['German']
#
#
# print(my_nis.home_countries)
# print(my_nis.__class__.home_countries)
# print(id(my_tla.home_countries_2))
# print(id(my_tyo.home_countries_2))

#
# print(id(my_nis.home_countries_2))
# print(id(my_tla.home_countries_2))
# print(id(my_tyo.home_countries_2))

#
# print(my_tla.home_countries_2)
# print(my_nis.home_countries_2)

# print('prices')
# print(id(my_nis.prices))
# print(id(my_tla.prices))
# print('-'*10)
# print('home_countries_2')
# print(id(my_nis.home_countries_2))
# print(id(my_tla.home_countries_2))
# print('-'*10)
# print('home_countries')
# print(id(my_nis.home_countries))
# print(id(my_tla.home_countries))
# print('-'*10)


# my_nis.home_countries = ['Italy']  # add to self object
# print(my_nis.home_countries)
# print(my_nis.__class__.home_countries)
# print(my_tla.home_countries)
# print('-'*20)
#
#
# my_tla.__class__.home_countries = ['Germany']  # add to class object
# print(my_nis.home_countries)
# print(my_nis.__class__.home_countries)
# print(my_tla.home_countries)
# print('-'*20)

# class Toyota(BaseCar):
#
#
#     def print_engine(self):
#         print(f"Toyota {self.engine}")
#
#
# my_base_car = BaseCar(model='base_car_model', engine='bc_v6')
# my_toyota = Toyota(model='toyota_model', engine='t_v6')
#
#
# my_base_car.print_engine()
# my_toyota.print_engine()

# my_nis.add_price()
