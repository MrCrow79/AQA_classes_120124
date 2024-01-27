# continue with real example

# resp = [
#     {'name': 'asd1', 'bd': '12-12-1989', 'gender': 'M', 'has_discount': False},
#     {'name': 'asd2', 'bd': '12-12-1991', 'gender': 'W', 'has_discount': True},
#     {'name': 'asd3', 'bd': '12-08-1989', 'has_discount': False},
#     {'name': 'asd4', 'bd': '01-01-1900', 'gender': 'M'},
#     {'name': 'asd5', 'bd': '12-12-2015', 'has_discount': False},
# ]
#
# # has_discount = True | false default
# # Age > 65 for M, > 62 for F
#
# user_with_discount = 0
# current_year = 2024
#
# for user in resp:
#     if user.get('has_discount', False):
#         user_with_discount += 1
#         continue
#
#     user_age = current_year - int(user['bd'].split('-')[-1])
#
#     # int(user['bd'].split('-')[-1])
#     # '12-12-1991'
#     # user['bd'] == '12-12-1991'
#     # (user['bd'].split('-') == '12-12-1991'.split('-') = ['12', '12', '1991']
#     # '12-12-1991'.split('-')[-1] = '1991'
#
#     if user.get('gender', 'M') == 'M':
#         if user_age < 65:
#             continue
#     else:
#         if user_age < 62:
#             continue
#
#     user_with_discount += 1
#
# print(user_with_discount)

#
# schedule = {
#     'monday':
#         [
#             {'id': '001', 'category': ['scary', 'comedy', 'bollywood']},
#             {'id': '002', 'category': ['scary', 'comedy']},
#             {'id': '003', 'category': ['action']},
#             {'id': '005', 'category': ['scary', 'action', 'comedy']}
#         ],
#     'friday':
#         [
#             {'id': '005', 'category': ['comedy', 'bollywood']},
#             {'id': '003', 'category': ['comedy', 'action']},
#             {'id': '002', 'category': ['scary', 'comedy']}
#         ]
# }
#
#
# day_without_comedy = None
# for day in schedule:
#
#     films_count = len(schedule[day])
#
#     while not day_without_comedy and films_count > 0:
#         films_count -= 1
#         if 'comedy' in schedule[day][films_count]['category']:
#             continue
#         day_without_comedy = day
#
#     if day_without_comedy:
#         break
#
#
# print(day_without_comedy)

#  zip: list, dict
# dict(zip([1,2,3,8,9], [4,5,6,7])) == for i in range(min(len(

# zip_list = list(zip([1,2,3, 4], ['a', 'b', 'c', 'd', 'e']))
# print(zip_list)

# zip_dict = dict(zip([1, 2, 3, 4], ['a', 'b', 'c', 'd', 'e']))
# print(zip_dict)
#
# m1 = [1, 2, 3, 4]
# m2 = ['a', 'b', 'c', 'd', 'e']
# res = []
#
# for indx in range(min(len(m1), len(m2))):
#
#     res.append((m1[indx], m2[indx]))
#
# print(dict(res))


# lambda

# def my_func(number_1):
#     return number_1 ** 2
#
# print(my_func(8))

# res = {
#     '+': lambda x, y: x+y,
#     '-': lambda x, y: x-y,
#     '*': lambda x, y: x*y,
#     '/': lambda x, y: x/y if y != 0 else 'Division by 0'
# }
# x = 2
# y = 0
# operator = '/'
#
# result = res.get(operator)
#
# if result is not None:
#     print(result(x, y))
# else:
#     print('Unknown operator')


# map(fn, iter) vs comprehension

# lst = [1,2,3,4,5]
#
# # res = list(map(lambda x: x+x, lst))
# res = list(map(lambda x: x+x, 'asd'))
# print(res)


# filter(fn, intr)

# res = list(filter(lambda x: x.isdigit(), 'ads123asd5ads'))
# print(res)
#
# res1 = []
# for k in 'ads123asd5ads':
#
#     if k.isdigit():
#         res1.append(k)
#
# print(res1)
#
# res2 = [k for k in 'ads123asd5ads' if k.isdigit()]
#
# print(res2)


# isinstance int and bool

# print(isinstance(True, int))
# print(isinstance(True, bool))

# all any

# print(all([1, 2, 3, None]))
# print(all([1, 2, 3]))
#
# print(any([1, 2, 3, False]))
# print(any([False, False, False]))


# correct ip




