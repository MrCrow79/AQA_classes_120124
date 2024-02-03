# functions, для чого

# def my_functions():
#     print('asd')
#
# my_functions()


# arguments
# return none, multiple objects
# def sum_and_multiply_3_numbers(num1, num2, num3):
#     sum_ = num1 + num2 + num3
#     multiply = num1 * num2 * num3
#     return sum_, multiply



#
# var1 = sum_and_multiply_3_numbers(1, 2, 4)
# print(var1)
# print(var2)

# if __name__


#
# if __name__ == '__main__':
#     pass
#
# current_file = __file__
# order of arguments, call with name


# def print_user_info(user_name, user_bd, user_position, user_country='Ukraine'):
#     print('user_name', user_name)
#     print('user_bd', user_bd)
#     print("user_position", user_position)
#     print("user_country", user_country)
#
#
# print_user_info('denys', 'qa', user_bd='20.08', user_country='Ukraine')


# args, kwargs
# def user_info(user_name, *args, user_position='QA'):
#     print(user_name)
#     print(user_position)
#
#     for item in args:
#         print(item)
#
# user_info('Denys', 1,2,3)

def user_info(user_name, **kwargs):

    print(user_name)
    for k in kwargs:
        print(k, kwargs[k])

# user_info('Denys', user_position='QA', user_age=30, user_country='Ukraine')

#
# url_base = 'https://exmaple.com/'
# apu_url_1 = 'v1/companies'
# apu_url_2 = 'v1/companies/:company_id'
#
#
# def get_full_path(url, **kwargs):
#     for k in kwargs:
#         if k in url:
#             url = url.replace(f':{k}', kwargs[k])
#     return f'{url_base}{url}'
#
#
# print(get_full_path(apu_url_2, company_id='001/'))

# list and dict as default value


# def append_1_to_list(input_dict=None):
#     if input_dict is None:
#         input_dict = dict()
#     import datetime
#     import time
#
#     input_dict[datetime.datetime.now()] = None
#     time.sleep(1)
#
#     print(input_dict)
#
# append_1_to_list()
# append_1_to_list()
# append_1_to_list()