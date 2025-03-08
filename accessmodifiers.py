# 1. Create a class with PRIVATE fields, private method and a main method. Print the fields
# in main method. Call the private method in main method.
# Create a sub class and try to access the private fields and methods from sub class.
class Parent:
    def __init__(self):
        self.__private_field = "I am Private"  # Private field

    def __private_method(self):
        return "This is a private method."

    def access_private_method(self):  # Public method to access private method
        return self.__private_method()

    def access_private_field(self):  # Public method to access private field
        return self.__private_field


# Main Method - Accessing Private Fields and Methods within the Class
obj = Parent()
print("Accessing Private Field in Main Method:", obj.access_private_field())  # Allowed
print("Accessing Private Method in Main Method:", obj.access_private_method())  # Allowed


# Creating a Subclass
class Child(Parent):
    def access_parent_private(self):
        try:
            return self.__private_field  # Trying to access private field (Will raise an error)
        except AttributeError:
            return "Cannot access private field from subclass."

    def access_parent_private_method(self):
        try:
            return self.__private_method()  # Trying to access private method (Will raise an error)
        except AttributeError:
            return "Cannot access private method from subclass."


# Testing Private Field and Method Access in Subclass
child_obj = Child()
print(child_obj.access_parent_private())  # Not allowed
print(child_obj.access_parent_private_method())  # Not allowed



# 2. Create a class with PROTECTED fields and methods. Access these fields and methods
# from any other class in the same package.
# Also, Access the PROTECTED fields and methods from child class located in a different
# package
# Access the PROTECTED fields and methods from any class in different package
# Defining the Parent class with protected fields and methods
class Parent:
    def __init__(self):
        self._name = "Protected Variable"

    def _display(self):
        print("Protected Method Called")

# Accessing protected members within the same module
class SamePackageAccess:
    def access(self):
        obj = Parent()
        print("Same Package Access:", obj._name)  # Accessing protected variable
        obj._display()    # Calling protected method

# Accessing protected members from a subclass in a different module (simulated)
class Child(Parent):
    def access_protected(self):
        print("Child Class Access:", self._name)  # Accessing protected variable
        self._display()    # Calling protected method

# Accessing protected members from a non-subclass in a different module (simulated)
class DifferentPackageAccess:
    def access(self):
        obj = Parent()
        print("Different Package Access:", obj._name)  # Accessing protected variable
        obj._display()    # Calling protected method

# Main block to test all accesses
if __name__ == "__main__":
    print("Access from Same Package:")
    test1 = SamePackageAccess()
    test1.access()

    print("\nAccess from Child Class:")
    test2 = Child()
    test2.access_protected()

    print("\nAccess from Non-Subclass in Different Package:")
    test3 = DifferentPackageAccess()
    test3.access()



# 3. Create a class with PUBLIC fields and methods.
# Access the public methods and fields from any class in the same package or different
# package.
# Defining a class with public fields and methods
class PublicClass:
    def __init__(self):
        self.name = "Public Variable"  # Public field

    def display(self):
        print("Public Method Called")  # Public method

# Accessing the public members from the same module
class SameModuleAccess:
    def access(self):
        obj = PublicClass()
        print("Same Module Access:", obj.name)  # Accessing public field
        obj.display()  # Calling public method

# Accessing the public members from a different module (simulated)
class DifferentModuleAccess:
    def access(self):
        obj = PublicClass()
        print("Different Module Access:", obj.name)  # Accessing public field
        obj.display()  # Calling public method

# Main block to test all accesses
if __name__ == "__main__":
    print("Access from Same Module:")
    test1 = SameModuleAccess()
    test1.access()

    print("\nAccess from Another Module:")
    test2 = DifferentModuleAccess()
    test2.access()
