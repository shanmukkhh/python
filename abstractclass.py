#1 Create an abstract class with abstract and non-abstract methods.
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):  
    def __init__(self, name):
        self.name = name  # Non-abstract data member

    @abstractmethod
    def fuel_type(self):  # Abstract method (must be overridden)
        pass  

    def show_info(self):  # Non-abstract method (default implementation)
        print(f"Vehicle Name: {self.name}")

# Subclass 1
class Car(Vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"

# Subclass 2
class ElectricCar(Vehicle):
    def fuel_type(self):
        return "Electric"

# Creating Objects
car = Car("Toyota")
ev = ElectricCar("Tesla")

# Calling methods
car.show_info()
print("Fuel Type:", car.fuel_type())

ev.show_info()
print("Fuel Type:", ev.fuel_type())



#2 Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name  # Non-abstract data member

    @abstractmethod
    def fuel_type(self):  # Abstract method (must be overridden)
        pass  

    def show_info(self):  # Non-abstract method
        print(f"Vehicle Name: {self.name}")

# Subclass (Concrete Class)
class Car(Vehicle):
    def fuel_type(self):
        return "Petrol or Diesel"

# Creating an object of the subclass
car = Car("Toyota")

# Accessing the non-abstract method from the abstract class
car.show_info()  # Calling non-abstract method



#3 Create an instance for the child class in child class and call abstract methods
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fuel_type(self):  # Abstract method
        pass  

    def show_info(self):  # Non-abstract method
        print(f"Vehicle Name: {self.name}")

# Child Class
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)  # Calling parent constructor
        self.instance = self  # Creating instance inside the child class

    def fuel_type(self):
        return "Petrol or Diesel"

    def call_methods(self):
        print(self.fuel_type())  # Calling abstract method
        self.show_info()  # Calling non-abstract method

# Creating an instance inside the child class
car = Car("Toyota")
car.call_methods()  # Calling methods using the instance



#4 Create an instance for the child class in child class and call non-abstract methods
from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fuel_type(self):  # Abstract method
        pass  

    def show_info(self):  # Non-abstract method
        print(f"Vehicle Name: {self.name}")

# Child Class
class Car(Vehicle):
    def __init__(self, name):
        super().__init__(name)  # Calling parent constructor
        self.instance = Car  # Storing class reference

    def fuel_type(self):
        return "Petrol or Diesel"

    def call_non_abstract_method(self):
        obj = self.instance("Honda")  # Creating instance inside the child class
        obj.show_info()  # Calling non-abstract method

# Creating an instance and calling non-abstract method
car = Car("Toyota")
car.call_non_abstract_method()