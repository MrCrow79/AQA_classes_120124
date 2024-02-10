from faker import Faker


from lesson_9.my_package.my_modult_math import my_sum

fake = Faker()

my_sum(10, 2)


# module and package
# alias
# from *, function

# init file
# circle import


# import lesson_9.my_package.my_modult_math as my_math
# from lesson_9.my_package.my_modult_math import my_sum, my_division, my_number as first_number
# from lesson_9.my_package_2.my_modult_math import my_number as second_number
#
# print(my_math.my_sum(1,2))
# print(my_division(3,4))
# print(first_number)
# print(second_number)

# from lesson_9.my_package.my_modult_math import my_new_number



# # built-in: time, random



# import random

# print(random.random())
# print(random.choice(['Alex', 'Viktor', 'Heorgii']))
# print(random.choices(['Alex', 'Viktor', 'Heorgii'], k=1))
# print(random.choice(range(100)))



# 3rd party
# pypi.org

# from faker import Faker
# fake = Faker()

# from lesson_9.variables.my_global_objects import fake
# from lesson_9 import fake
#
# print(fake.name())


# print(fake.pystr(min_chars=5, max_chars=20))


# requrements
# pip list, freeze






# print(fake.address())
# '426 Jordy Lodge
#  Cartwrightshire, SC 88120-6700'

import os

user_name = os.environ.get('USER_NAME')