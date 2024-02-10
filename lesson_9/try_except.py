

def my_math(num1, num2, operator):
    if operator == '+':
        try:
            return num1 + num2
        except TypeError as e:
            # 1 print('You have to inut 2 numbers')
            # 2 print(e)
            print('You have to inut 2 numbers')
            raise TypeError(e)


    elif operator == '/':
        return num1 / num2

my_math('asd', 0, '+')

