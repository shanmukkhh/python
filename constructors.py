#1 Write a class with a default constructor, one argument constructor and two argument
# constructors. Instantiate the class to call all the constructors of that class from a main
# class
class Example:
    # Default constructor
    def __init__(self, arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            print("Default Constructor Called")
        elif arg2 is None:
            print(f"One Argument Constructor Called: arg1 = {arg1}")
        else:
            print(f"Two Argument Constructor Called: arg1 = {arg1}, arg2 = {arg2}")

# Main class to instantiate objects
if __name__ == "__main__":
    obj1 = Example()          # Calls default constructor
    obj2 = Example(10)        # Calls one-argument constructor
    obj3 = Example(10, 20)    # Calls two-argument constructor



# 2. Call the constructors(both default and argument constructors) of super class from a child
# class
class Parent:
    # Default constructor
    def __init__(self, arg1=None):
        if arg1 is None:
            print("Parent Default Constructor Called")
        else:
            print(f"Parent Parameterized Constructor Called with arg1 = {arg1}")

class Child(Parent):
    def __init__(self, arg1=None):
        if arg1 is None:
            super().__init__()  # Calls Parent's default constructor
            print("Child Default Constructor Called")
        else:
            super().__init__(arg1)  # Calls Parent's parameterized constructor
            print(f"Child Parameterized Constructor Called with arg1 = {arg1}")

# Creating instances to call different constructors
print("Creating Child Object with Default Constructor:")
child1 = Child()  # Calls Parent's default constructor

print("\nCreating Child Object with Parameterized Constructor:")
child2 = Child(10)  # Calls Parent's parameterized constructor



# 3. Apply private, public, protected and default access modifiers to the constructor
class Example:
    # Public Constructor
    def __init__(self):
        print("Public Constructor Called")

    # Protected Constructor
    def _init_protected(self):
        print("Protected Constructor Called")

    # Private Constructor
    def __init_private(self):
        print("Private Constructor Called")

# Subclass to demonstrate protected constructor
class SubExample(Example):
    def __init__(self):
        super().__init__()  # Calls the public constructor
        super()._init_protected()  # Calls the protected constructor

# Creating object of the class
print("Creating Object of Example Class:")
obj = Example()  # Public constructor is called

print("\nCreating Object of SubExample Class:")
sub_obj = SubExample()  # Calls public and protected constructor

# Accessing protected constructor directly
print("\nAccessing Protected Constructor:")
obj._init_protected()  # Allowed, but not recommended

# Accessing private constructor will cause an error
print("\nTrying to Access Private Constructor:")
# obj.__init_private()  # This will cause an AttributeError



# 4. Write a program which illustrates the concept of attributes of a constructor.
class Student:
    # Constructor with attributes
    def __init__(self, name, age, grade):
        self.name = name       # Attribute 1
        self.age = age         # Attribute 2
        self.grade = grade     # Attribute 3

    # Method to display student details
    def display_info(self):
        print(f"Student Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")

# Creating an instance of Student
student1 = Student("Pavan", 22, "A")

# Accessing attributes
print("Accessing attributes directly:")
print(f"Name: {student1.name}, Age: {student1.age}, Grade: {student1.grade}")

# Calling method to display details
print("\nCalling display_info() method:")
student1.display_info()