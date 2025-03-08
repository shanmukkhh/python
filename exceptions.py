# 1. Write a program to generate Arithmetic Exception without exception handling
# Arithmetic Exception (Division by Zero)
result = 10 / 0  # This will raise ZeroDivisionError
print("This line will not execute")  # This will never be printed



#2 Handle the Arithmetic exception using try-catch block
try:
    # Attempt to divide by zero
    result = 10 / 0  
    print("This will not be printed")  
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")  

print("Program continues after handling the exception.")



#3 Write a method which throws exception, Call that method in main class without try block
class Example:
    def throw_exception(self):
        raise Exception("This is a manually raised exception")

# Creating an object and calling the method without handling the exception
obj = Example()
obj.throw_exception()  # This will cause the program to crash



#4 Write a program with multiple catch blocks
try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b  # May cause ZeroDivisionError
    numbers = [1, 2, 3]
    print(numbers[5])  # May cause IndexError
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except IndexError:
    print("Error: Index out of range in the list.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")



#5 Write a program to throw exception with your own message
# Asking user for age input
age = int(input("Enter your age: "))

# Check if the age is valid
if age < 0:
    raise ValueError("Age cannot be negative. Please enter a valid age.")
elif age < 18:
    raise Exception("You must be at least 18 years old to register.")

# If age is valid
print("You are eligible to register.")



#6 Write a program to create your own exception
# Creating a custom exception class
class InvalidAgeError(Exception):
    """Custom exception for invalid age input."""
    def __init__(self, age, message="Age must be 18 or above."):
        self.age = age
        self.message = message
        super().__init__(self.message)

# Function to check age eligibility
def check_age(age):
    if age < 18:
        raise InvalidAgeError(age, f"Invalid Age: {age}. You must be at least 18 years old.")
    else:
        print("Access granted!")

# Taking user input
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print("Custom Exception:", e)
except ValueError:
    print("Please enter a valid number.")



#7 Write a program with finally block
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2  # May raise ZeroDivisionError
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter valid numbers.")
finally:
    print("Execution completed. Cleaning up resources if any.")



#8 Write a program to generate Arithmetic Exception
# Division by zero will cause an Arithmetic Exception
num1 = 10
num2 = 0
result = num1 / num2  # This line will raise a ZeroDivisionError
print("Result:", result)  # This line won't be executed



#9 Write a program to generate FileNotFoundException
# Attempting to open a non-existent file
file = open("non_existent_file.txt", "r")  # This will raise FileNotFoundError
content = file.read()
print(content)
file.close()



#10. Write a program to generate ClassNotFoundException
class TestClass:
    pass

# Trying to access a non-existent class
classname = "NonExistentClass"
cls = globals()[classname]  # This will raise KeyError



#11. Write a program to generate IOException
try:
    # Trying to open a file that does not exist
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except IOError as e:
    print(f"IOException occurred: {e}")



#12. Write a program to generate NoSuchFieldException
class Example:
    def __init__(self):
        self.existing_field = 10

try:
    obj = Example()
    print(obj.non_existent_field)  # This attribute does not exist
except AttributeError as e:
    print(f"AttributeError occurred: {e}")