# 1. Create a program to create two class.
# 1.1. Create a constructor and a method for each class
# 1.2. Create a __init__.py for adding all packages
# 1.3. Import the respective packages
# 1.4. Call each class by creating an object to it
# 1.5. Create a program by all the above


# creating constructor and method
class Package:    
    class ClassOne:
        def __init__(self, name): # creation of __int__.py
            self.name = name  

        def show_message(self):
            print(f"Hello from ClassOne, {self.name}!")

    class ClassTwo:
        def __init__(self, age):
            self.age = age  

        def display_age(self):
            print(f"Your age is {self.age}.")

if __name__ == "__main__":
    # Creating objects and calling methods
    obj1 = Package.ClassOne("Alice")
    obj1.show_message()

    obj2 = Package.ClassTwo(25)
    obj2.display_age()