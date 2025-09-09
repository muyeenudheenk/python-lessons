#Object-Oriented Programming (OOP) is a programming paradigm based on the concept of “objects”, which can contain data and code: data in the form of attributes, and code in the form of methods.classess(theoreis or frameworkObjects (Specific application of those theories methods (Calculations /actions we perform)A class is like a blueprint for creating objects. An object is an instance of a class.An object is a specific instance of a class. If "Consumer" is your class, then "John Smith buying groceries" is an object - a real example with actual data.
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


    def display(self):
        print(f"Name: {self.name}, Grade: {self.grade}")


# Create an object
student1 = Student("Alice", "A")
student1.display()

# Calculate THIS survey respondent's savings rate

def save(self):
      savings = self.income - self.spending
      savings_rate = (savings / self.income) * 100
      return savings_rate


print(f"Name: {self.name}, Grade: {self.grade},saving rate:{self.save():} ")


class Car:
    def __init__(self, brand, speed):
        self.brand = brand   # attribute
        self.speed = speed

    def accelerate(self):
        self.speed += 10  # method

# Child class
class SportsCar(Car):  # Inherits from Car
    def accelerate(self):
        self.speed += 20  # Overrides parent method

# Object creation and testing
car1 = Car("Toyota", 100)
car1.accelerate()
print(car1.brand, car1.speed)  # Toyota 110

car2 = SportsCar("Ferrari", 150)
car2.accelerate()
print(car2.brand, car2.speed)  # Ferrari 170

#Inheritance Inheritance is a core OOP principle that allows a new class (the subclass or child class) to inherit properties—attributes and methods—from an existing class (the superclass or parent class). This creates an "is-a" relationship, where the subclass is a more specialized version of the superclass. The primary benefit of inheritance is code reusability. You can write common functionalities in a parent class and have multiple child classes reuse that code without rewriting it. Child classes can also add their own unique methods and attributes or override the parent's methods to provide a more specific implementation.Animal class. A Dog class can inherit from Animal, gaining its attributes and methods, while also adding its own specific behavior.

#Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        # A generic implementation
        raise NotImplementedError("Subclass must implement this abstract method")

# Child class inheriting from Animal
class Dog(Animal):
    # Overriding the parent's speak method
    def speak(self):
        return f"{self.name} says Woof!"

# Another child class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances of the classes
my_dog = Dog("Buddy")
my_cat = Cat("Whiskers")

print(my_dog.speak()) # Output: Buddy says Woof!
print(my_cat.speak()) # Output: Whiskers says Meow!

