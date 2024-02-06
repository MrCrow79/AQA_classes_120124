# yield


# def get_numbers(numbers):
#     for num in numbers:
#         print(f'current num is {num}')
#         yield num
#         print('You get your number')


# def get_numbers(numbers):
#     print(f'current num is {numbers[0]}')
#     yield numbers[0]
#     print(f'current num is {numbers[1]}')
#     yield
#     print(f'current num is {numbers[2]}')
#     yield
#
#
#
# gen_iter = iter(get_numbers([1, 2, 3]))
# el = next(gen_iter)
# print('--'*10)
# el = next(gen_iter)
# print('--'*10)
# el = next(gen_iter)


# iter gen vs list list


# def get_big_numbers():
#     for k in range(1000000000):
#         if k > 1000000000/2:
#             yield k
#         print(k)

# gen comprehension

# (k**2 for k in range(1000000000))

#
# sys.getsizeof

# import sys
#
# my_gen = (k**2 for k in range(10000))
# my_list = [k**2 for k in range(10000)]
#
# print(sys.getsizeof(my_gen))
# print(sys.getsizeof(my_list))

# example with [range()]