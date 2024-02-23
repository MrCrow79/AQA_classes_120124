from lesson_13.phone_practise.phones.iPhone import IPhone
from lesson_13.phone_practise.operators.life_operator import LifeOperator
from lesson_13.phone_practise.mobile_apps.candy_crash import CandyCrash


my_life_package = LifeOperator(package='lite', balance=200)
my_candy_crash = CandyCrash()

my_iphone_13 = IPhone(model='Iphone_13', mobile_operator=my_life_package, memory_quantity=8256)

my_iphone_14 = IPhone(model='Iphone_14', mobile_operator=my_life_package, memory_quantity=8256)
my_iphone_14_pro = IPhone(model='Iphone_14_pro', mobile_operator=my_life_package, memory_quantity=12256)


print(my_iphone_13 == my_iphone_14)
print(my_iphone_14 == my_iphone_14_pro)

print(my_iphone_13 >= my_iphone_14)
print(my_iphone_14 >= my_iphone_14_pro)


# my_iphone_13.install_application(my_candy_crash)
# print(my_iphone_13.free_memory)
# my_iphone_13.get_application(my_candy_crash.name).turn_on()
# print(my_iphone_13.free_memory)
# my_iphone_13.get_application(my_candy_crash.name).turn_off()
# print(my_iphone_13.free_memory)

