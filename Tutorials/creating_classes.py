"""
    Date: 1-18-2025
    Description: Creating objects and classes in python.
"""

# 1. Define a Class
#  Treat it like a blueprint for objects. It defines the structure and behavior of the objects created from it.


class MyClass:
    # Constructor (initializes attributes)
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Instance variable
        self.attribute2 = attribute2

    # Method (function within a class)
    def display_attributes(self):
        print(f"Attribute 1: {self.attribute1}, Attribute 2: {self.attribute2}")


# 2. Create an Object
# They are an instance of a class. Use the class name followed by parentheses to create one.

# Create an instance of MyClass
my_object = MyClass("value1", "value2")

# Access object attributes and methods
print(my_object.attribute1)  # Output: value1
my_object.display_attributes()  # Output: Attribute 1: value1, Attribute 2: value2


"""
                                    Key Concepts: 
Attributes
    Attributes are variables that belong to an object.
    Defined using self inside the class.
    
Methods
    Methods are functions defined inside a class and are used to define the behavior of the objects.
    The first parameter of a method is always self, which represents the instance of the class.
"""

# 4. Example with Multiple Objects


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")


# Create multiple objects
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes and methods
person1.greet()  # Output: Hello, my name is Alice, and I am 30 years old.
person2.greet()  # Output: Hello, my name is Bob, and I am 25 years old.

# 5. Inheritance
# Classes can inherit from other classes to reuse or extend functionality.


class Animal:
    def __init__(self, species):
        self.species = species

    def sound(self):
        print("This animal makes a sound.")


class Dog(Animal):
    def __init__(self, species, breed):
        super().__init__(species)
        self.breed = breed

    def sound(self):
        print("Woof! Woof!")


# Create an object of the subclass
dog = Dog("Mammal", "Golden Retriever")
print(dog.species)  # Output: Mammal
print(dog.breed)    # Output: Golden Retriever
dog.sound()         # Output: Woof! Woof!
