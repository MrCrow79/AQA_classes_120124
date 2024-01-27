# 1/0

#
# try:
#     1 + 'asd'
# except Exception as e:
#     print(e)
# else:
#     print('Else')
# finally:
#     print('Finally')


# is_connected = False
# try_counter = 0
#
# while not is_connected and try_counter < 5:
#     try:
#         try_counter += 1
#         is_connected = True
#     except ConnectionError as e:
#         print('ZeroDivisionError error custom')
#     except TimeoutError as e:
#         print('ZeroDivisionError error custom')

# raise

age = 30
if age > 65:
    raise AttributeError("Age can't be more than 65")


response = [
    {
        'id': 1,
        'name': "Antonio"
    },
    {
        'id': 0,
        'name': "Antonio"},
    {
        'id': 1,
        'name': ''}
]

#
# has_error = False
# try:
#     for user in response:
#         if user['id'] == 0:
#             raise AssertionError('id is 0')
#
#         if len(user['name']) == 0:
#             raise AssertionError('Name is null')
# except AssertionError as e:
#     has_error = True
#     print(e)
#
# assert has_error


# try except else finally

# bullet-in exeptions


# class TooSmallError(Exception):
#     pass
#
#
# class TooHugeError(Exception):
#     pass
#
#
# is_correct_number = False
# while not is_correct_number:
#     try:
#         user_input_number = input('Enter the number')
#         try:
#             user_input_number = float(user_input_number)
#             is_correct_number = True
#         except ValueError:
#             print('Try again enter a number')
#             raise ValueError
#
#         if user_input_number <= 6:
#             print('Number have to be bigger than 6')
#             raise TooSmallError()
#
#         if user_input_number >= 100:
#             print('Number have to be less than 100')
#             raise TooHugeError()
#
#     except TooSmallError:
#         is_correct_number = False
#     except TooHugeError:
#         is_correct_number = False
#     except ValueError:
#         is_correct_number = False
#     else:
#         print('Number is correct')






