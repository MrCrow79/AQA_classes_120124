# base syntax

# bad call
# def print_say_hi(function, user_name):
#
#     print(f'Hi')
#     return function(user_name)
#
#
# def greetings(user_name):
#     print(f'hello, {user_name}\nthis is greetings function')
#
#
# #
# my_function_variable = greetings
# my_function_variable('Alex')
# my_name = 'Alex'
#
# new_greetings = print_say_hi
# new_greetings(my_function_variable, my_name)


# typical call

def print_before_and_after_decorator(function):

    def wrapper(user_name):
        print('decorator start')
        function(user_name)
        print('decorator end')

    return wrapper


def do_twice(function):

    def wrapper(user_name):
        function(user_name)
        function(user_name)

    return wrapper


@print_before_and_after_decorator  # greetings = print_before_and_after_decorator(greetings)
def greetings(user_name):
    print(f'hello, {user_name}')


@do_twice  # greetings_2 = do_twice(greetings_2)
def greetings_2(user_name):
    print(f'hello, {user_name}')


@print_before_and_after_decorator   # greetings_3 = print_before_and_after_decorator(greetings_3)
@do_twice  # greetings_2 = do_twice(greetings_2)
def greetings_3(user_name):
    print(f'hello, {user_name}')


# greetings('Alex')
# greetings_2('Ivan')
# greetings_3('Viktor')

# def greetings(user_name):
#     print(f'hello, {user_name}')
#
# greetings = print_say_hi_decorator(greetings)
#
# greetings('Alex')
# with params

# import time

