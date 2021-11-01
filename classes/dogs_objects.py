# from classes.dogs import *
from classes.dogs import Dog, Cat

dog1 = Dog('krish', 'white', 'American Eskimo', 6)  # instantiation
# __init__functions is automatically called (executed)
print(" # Accesing the variables of the object based on the model")
# dog1 - object. krish, american eskimo, 6 - instance variables
print('name of the dog: ', dog1.name)
print('color of the dog: ', dog1.color)
print('breed of the dog: ', dog1.breed)
print(' age of the dog: ', dog1.age)

print("########## accesing the methods of functions Dog1#####################")
dog1.run()
dog1.sit()
dog1.bark()
dog1.description()
print('#####Accessing of Dog2')
dog2 = Dog(age=6, breed='French Bulldog', color='brown', name='Avni')
dog2.run()
dog2.sit()
dog2.bark()
dog2.description()
dog3 = Dog('POP', 'black', 'boerbol', 8)

print("########## accesing the methods of functions Dog3##############")
dog3.run()
dog3.sit()
dog3.bark()
dog3.description()

cat1 = Cat()
print("######### 9-1 ######")




class Restaurant():
    pass

    # restaurant_name, cuisine_type
    def __init__(self, restaurant_name: str, cuisine_type: str) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):

        print(f"We are '{self.restaurant_name.upper()}' and we are {self.cuisine_type} restaurant ")
# describe_restaurant() - use 2 variables above
# open_restaurant() - print("we are open")
    def open_restaurant(self):
     print(f"{self.restaurant_name.title()} are open!")

restaurant = Restaurant("Taco bell", "Mexican")
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.open_restaurant()
restaurant.describe_restaurant()

    def __init__(self, res_name:str, res_type:str):
          self.res_name = res_name
          self.res_type = res_type



     def describe_restaurant(self):
         print(f'{self.res_name} is good place for dinner !')

restaurant1 = Restaurant('suzanna', 'uzbek-russian')
restaurant1.describe_restaurant()


    def __init__(self, rst_name: str, rst_type: str):
        self.rst_name = rst_name
        self.rst_type = rst_type

    def describe_restaurant(self):
        print(f"{self.rst_name.title()} is most crowded in the weekends.")

restaurant2 = Restaurant ('istanbul', 'turkish')
restaurant2.describe_restaurant()

print(f"Best restaurant for me is {self.rst_name.title()} " )




    def __init__(self,restaurant3_name:str, cuisine: str)
        self.restaurant3_name = restaurant3_name
        self.cuisine = cuisine

    def describe_restaurant(self):
        print(f"Cheapest restaurant is {self.restaurant3_name}  and cuisine type is {self.cuisine}")

restaurant3 =Restaurant("Istanbul", "turkish")
restaurant3.describe_restaurant()



    class User():
        pass

    def __init__(self,first_name: str,last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
            print(f"{self.first_name.title()}  {self.last_name.title()} is experienced doctor.")

doctor = User ('anna', 'petrovskiy')

    def greet_user(self):
        print(f"HELLO doctor {self.first_name.title()} {self.last_name.title()} ! Did you finish the homework?")










