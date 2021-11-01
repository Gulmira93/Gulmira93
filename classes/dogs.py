"""
Chapter 9
Object oriented programming - modeling the real world object and using them in program
Class - model of smth ; generic state(description) and behavior of object(car, toy, dog, tree, human, etc...)
object - instance of a class; one of the sample of model;
instanciation - creating an object from class


"""
HOME = 'C/dev/basics'


class Dog():
    """
    This is the model for generic dog.
    """

    # state/property/instance variable : name, color, breed, age
    # state/property: number_of_leg = 4

    def __init__(self, name, color, breed, age):
        """Constructor: Initialize variables name,color, breed, age     """

        self.name = name
        self.color = color
        self.breed = breed
        self.age = age

    # behavior : run(), sit(), bark()
    def run(self):
        print(f"{self.name.title()}  is running.")

    def sit(self):
        print(f"{self.name.title()} is sitting  :) ")

    def bark(self):
        print(f"{self.name.title()} is barking woof, woof!!!!!!!!")
    def description (self):
        print(f"Hi this is {self.name} and I am beautiful with {self.color} colored dog. I am {self.age} years old and I am a {self.breed}")

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

class Cat():
    def __init__(self):
        pass # do nothing in python
    # in this case constructor is optional since python creates automatically
    def sit (self):
        print("cats don't like to sit, so I will lay down. ")



















