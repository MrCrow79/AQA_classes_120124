
# decorators


# def greetinngs():
#     print('Hi')
#
#
# def say_hello(user_name):
#     print(user_name)
#
#
# my_fun = greetinngs
#
# print(id(greetinngs))
# print(id(my_fun))
# print('-'*10)
# print('greetinngs', greetinngs)
# print('my_fun', my_fun)
#
# greetinngs = say_hello
#
# print('-'*10)
# print('greetinngs', greetinngs)
# print('my_fun', my_fun)


# def greetinngs(fn):
#
#     def wrapper(user_name):
#         # print('Hi')
#         fn(user_name)
#         fn(user_name)
#         # print('Bye')
#     return wrapper


# def say_hello(user_name):
#     print(f'Hello, {user_name}')
#
#
# say_hello = greetinngs(say_hello)
# say_hello('Denys')

# greetinngs(say_hello)('Denys2')

@greetinngs
def say_hello(user_name):
    print(f'Hello, {user_name}')

say_hello('Denys3')



# def greetinngs(fn):
#     def wrapper(user_name):
#         fn(user_name)
#     return wrapper

# with params

# def retry(retry_count):
#     def decorator(fn):
#         def wrapper(*args, **kwargs):
#
#             local_retry = retry_count
#             while local_retry > 0:
#                 try:
#                     return fn(*args, **kwargs)
#                 except Exception as e:
#                     print(f'Try again, you have {local_retry} attemps')
#                     local_retry -=1
#
#         return wrapper
#
#     return  decorator
#
#
# @retry(5)
# def number_chooser(number):
#     if number < 5:
#         raise Exception('To small number')
#     print('Correct nummber')
#
#
# number_chooser(4)


import time

from faker import Faker

fake = Faker()

print(fake.name())

# current_time = time.time()
# print(type(current_time))
# time.sleep(2)
# print(round(time.time() - current_time, 2))


# import time


# https://www.codewars.com/


