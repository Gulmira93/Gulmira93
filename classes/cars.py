# Chapter 9(cont)
# Working with classes and instances
# Defining classes here

# create Car class with following state and behavior
# make , model, year, max_speed argument/attribute
# implement the logic for mileage:
# 1. should not be visible to user (object), so object can not set
# the value
# 2. create function to set mileage() only when new mileage is
# greater than value and not negative
# get_description (), get_mileage(), add_mileage(mile)


class Car:
    """ This is a general model for all cars  """

    def __init__(self, make: str, model: str, year: str):
        """construction of car class"""
        self.make = make
        self.model = model
        self.year = year
        self.__mileage = 0  # encapsulation : hiding data, it is private
        # java example of the same encapsulation
        # public String make = make;
        # private Int mileage = 0;

    def get_description(self):
        """printing detailed description of the car"""
        print(f"This is {self.make.title()} {self.model.title()} {self.year}.")

    def get_mileage(self):
        """prints the odometer reader mileage"""
        print(f"Car has {self.__mileage} miles on it")

    def set_mileage(self, new_mileage):
        """Updating the value of odometer reader."""
        if new_mileage > self.__mileage:
            print("odometer reader updated.")
        else:
            print('odometer reader was not updated')

    def increment_odometer(self, miles):
        if miles > 0:
            # self. __mileage += miles
            self.__mileage += miles
            print("odometer can not be updated with the given value.")

    def fill_gas_tank(self):
        print(f"filling the tank for {self.model} ...... Done!")


class ElectricCar(Car):  # inheritance happens here
    """Model of electric cars  based on regular car
    features. Car is parent class"""

    pass

    def __init__(self, make: str, model: str, year: str):
        # everything from parent class
        super().__init__(make, model, year)  # calling the constructor from parent class
        self.battery_size = 70  # 70kWh

    def fill_gas_tank(self):
        """Polymorphism: Method overriding - overrides the same
        method from parent class"""
        print(f"This is {self.model} gas not used")

    def measure_battery(self):
        print(f"hey, measure car's battery . it must be {self.battery_size} ")

    # not good in python , in java it is called method overloading
    # def fill_gas_tank(self, battery):
    # polymorphism: Method overloading - overrides
    # the same method from parent class
    # print (f"this is {self.model}, gas is not used.")


print(" ######################Practice in class ############")


def get_description ():
    print(f"This house is {type.title()} !")


class House:

    pass

    def __init__(self, type: str, rnum: str, year: str):

        self.type = type
        self.rnum = rnum
        self.year = year



    def get_information(self):
        print(f"This house is {self.type} !")

    def get_size(self):
            print(f"it contains {self.rnum}.")


    def get_time(self):
        print(f'it was built in {self.year}. ')







