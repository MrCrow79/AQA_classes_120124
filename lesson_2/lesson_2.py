"""
print(1 == 2)
print(1 != 2)

print(1 > 1)
print(1 < 1)

print(1 <= 1)
print(1 >= 1)

# if file_date < today:
#     if file_size > 600:
#         pass


# if (file_date < yesterday OR file_date == today) AND (file_size > 600):
#     pass


False
[1,2] == [1,2]
True
[1,2] is [1,2]

2
lst
[1, 2, 3, 4]
1 in lst
True
dct = {'fs': 1, 'sc': 2, 'th': 3}
dct['fs']
1
'th' in dct
True
3 in dct
False
"""


# age = 20
# salary = 100
# name = 'John'
#
# if age > 20 and salary == 100:
#     print('AND operator: Age > 20')
#
#
# if age > 20 or salary == 100:
#     print('OR operator:Age > 20')
#
# if age > 20:
#     print('Never')
# else:
#     print('Age <= 20')
#

method = 'GET'
where_to_send = None

if method == 'GET':
    where_to_send = 'http_get'
    pass
elif method == 'POST':
    where_to_send = 'http_post'
else:
    where_to_send = ''

if where_to_send is None:
    print('is None')
elif where_to_send != '':
    print(where_to_send)
else:
    print('Unknown path')

# if where_to_send:  # if bool(where_to_send)
#     print('non None')
# if where_to_send != '': #  if bool(where_to_send != ''):

your_age = float(input('Enter your age: '))

if your_age < 18:
    print("You're too yang")
else:
    print("you're too old")


def methodd(age: int|float) -> float|int:
    pass