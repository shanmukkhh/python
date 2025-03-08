# 1 Write two methods with the same name but different number of parameters of same type
# and call the methods
class Example:
    def add(self, a, b=0):  # Default value for second parameter
        print("Sum:", a + b)

# Creating an instance
obj = Example()

# Calling the method with one argument
obj.add(5)

# Calling the method with two arguments
obj.add(5, 10)



#2 Write two methods with the same name but different number of parameters of different
# data type and call the methods
class Example:
    def display(self, a, b=None):  
        if isinstance(a, int) and b is None:
            print("Single integer argument:", a)
        elif isinstance(a, str) and isinstance(b, int):
            print("String and integer arguments:", a, b)
        else:
            print("Invalid argument types")

# Creating an instance
obj = Example()

# Calling method with different types
obj.display(10)          # Single integer argument
obj.display("Hello", 5)  # String and integer argument



#3 Write two methods with the same name and same number of parameters of same type
class Example:
    def show(self, a=None):  # Single method handling different cases
        if a is None:
            print("No argument provided")
        else:
            print("Argument provided:", a)

obj = Example()
obj.show()     # No argument provided
obj.show(10)   # Argument provided: 10