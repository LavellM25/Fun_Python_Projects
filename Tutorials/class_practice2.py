"""
    Date: 1-18-2025
    Description: Demonstrates the concept of object-oriented programming (OOP) in Python by modeling real-life
    entities using classes. It showcases:
    1. Inheritance (a CarOwner is a type of Person).
    2. Attributes and methods shared between base and subclass.
    3. How to create and use objects in Python.

    The specific example uses a Person class to represent general human attributes (e.g., name, age, hobby) and extends
    it into a CarOwner class to represent individuals who own cars, adding relevant attributes and behaviors.
"""

# Step 1: Define a base class to represent a general person


class Person:
    # Step 2: The constructor method initializes attributes common to all people
    def __init__(self, name, age, hobby):
        self.name = name  # Assigns the name attribute
        self.age = age    # Assigns the age attribute
        self.hobby = hobby  # Assigns the hobby attribute

    # Step 3: Define a method to introduce the person
    def introduce(self):
        # This method prints a simple introduction message using the object's attributes
        print(f"Hi, my name is {self.name}. I am {self.age} years old, and I enjoy {self.hobby}.")

# Step 4: Define a subclass to represent car owners, inheriting from Person


class CarOwner(Person):
    # Step 5: Extend the constructor to include additional attributes for car ownership
    def __init__(self, name, age, hobby, car):
        # Step 6: Use `super()` to call the constructor of the base class (Person)
        super().__init__(name, age, hobby)  # Inherit name, age, and hobby from Person
        self.car = car  # Add a new attribute for the car

    # Step 7: Define a new method to display car details
    def car_details(self):
        # This method prints a message about the car owned by the individual
        print(f"{self.name} drives a {self.car}.")


# Step 8: Create an object of the Person class
person = Person("Lavell", 21, "programming")
# Step 9: Call the introduce method on the person object
person.introduce()
# Output: Hi, my name is Lavell. I am 21 years old, and I enjoy programming.

# Step 10: Create an object of the CarOwner subclass
car_owner = CarOwner("Lavell", 21, "programming", "Honda Accord")
# Step 11: Call the introduce method (inherited from Person) on the car_owner object
car_owner.introduce()
# Output: Hi, my name is Lavell. I am 21 years old, and I enjoy programming.

# Step 12: Call the car_details method on the car_owner object
car_owner.car_details()
# Output: Lavell drives a Honda Accord.
