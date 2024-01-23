# range

# range1 = range(10)  # 0-9
#
# print(range1)
# print(list(range1))

# range1 = range(1, 11, 2)  # 4-9
#
# print(range1)
# print(list(range1))


# for else(check break)

list_of_symbols = ['a', 'b', 'c', 'd', 'e']
#
# for el in list_of_symbols:
#     print(el)


# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# for row in matrix:
#     print(row)
#     if 3 in row:
#         continue
#
#     for number in row:
#         print(number)
#         if number in (2, 5, 8):
#             break

# res = False
#
# list_of_number = [5, 5, 5, 5, 5, 5]
#
# for k in list_of_number:
#     if k != 5:
#         break
#     print(k)
# else:
#     res = True
#
# print(res)

# break and continue

# while

# names = ['Alex', 'Joe']
#
# while len(names) > 0:
#     # do something
#     print(names)
#     names.remove(names[0])
#
# print('done')

# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }

# for position in positions:
#     # print(key)
#     # print(positions[key])
#     # print('\n')
#     print(f'Position name is {position}. Descriptions is: {positions[position]}')



# comprehension list, dict

# numbers = [1,2,3,4,5]
# #
# pow_operation = []
# for num in numbers:
#     if num < 4:
#         pow_operation.append(num**2)
#
# print(numbers)
# print(pow_operation)
#
# pow_operation2 = [num**2 for num in numbers if num < 4]
#
# print(pow_operation2)


# {k,v for k,v in } + if + tern operator
# [a.update({k: 2}) for k in range(5)]

# positions = {
#
#     'AQA': 'create your tests',
#     'DevOPs': 'create your instance',
#     'Dev': 'create your app',
# }
# new_positions = {}
#
# for key in positions:
#     if key.startswith('D'):
#         new_positions[key] = 'Cool'
#
# new_positions1 = {k: 'cool' for k in positions if k.startswith('D')}
#
# print(new_positions)
# print(new_positions1)

positions = {

    'AQA': 'create your tests',
    'DevOPs': 'create your instance',
    'Dev': 'create your app',
}


for key in positions:
    print(f'positions is {key}. Descriptions is {positions[key]}')

print('\n')
for key, value in positions.items():
    print(f'positions is {key}. Descriptions is {value}')
print('\n')

[print(f'positions is {key}. Descriptions is {value}') for key, value in positions.items()]