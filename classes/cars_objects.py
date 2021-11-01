# Chapter 9 (cont)
# Working with classes and Intances
# Instantiating the classes (executing)
from classes.cars import *
car1 = Car('toyota', 'camry', 2021)
print(car1.make)
print(car1.model)
car1.get_description()
#car1.mileage = 25
car1.get_mileage()
#car1.__mileage = -25
car1.get_mileage()
car1.set_mileage(-5)
car1.get_mileage()
car1.set_mileage(24)
car1.get_mileage()
print('-------------------------------------')
car1.increment_odometer(50)
car1.get_mileage()
car1.increment_odometer(-10) # not possible real world
car1.get_mileage()



car2 = Car('tesla', 'Model X', 2022)


print('--------------Electric car-------------')

car2 = ElectricCar('Tesla', 'Model X', 2022)
car2.get_description()
print(car2.model)
car1.fill_gas_tank()
car2.fill_gas_tank()
car2.battery_size()
# H/W : www.indeed.com/career/-advice/career-development/what-is-object-oriented-programming
# 9-4, 9-5, 9-6, 9-7,9-8, 9-9
# Agenda:
#chapter 10: high level

house1 = House('single', 3, 2000)
house1.get_information()
house1.get_size()
house1.get_time()
print(house1.type)
print(house1.rnum)
print(house1.year)
















