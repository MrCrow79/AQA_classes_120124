# nested: nonlocal, global


user_name = 'Alex'


def say_hello():
    user_name = 'Viktor'
    print(f'Hello 1, {user_name}')

    def say_hi():
        # nonlocal user_name
        global user_name
        user_name = 'Ivan'

        print(f'Hi, {user_name}')

    say_hi()
    print(f'Hello 2, {user_name}')


say_hello()
print(f'Global {user_name}')
