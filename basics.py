#1 Write a program to print your name.
name=input("Enter your name: ") #This is to take input from the user
print(name) #This line prints the output from input


#2 Write a program for a Single line comment and multi-line comments
# This is a single-line comment in Python

"""
This is a multi-line comment.
It can span multiple lines.
Used for documentation or explanations.
"""


#3  Define variables for different Data Types int, Boolean, char, float, double and print on the console
# Global variable
var = "I am a Global Variable"
print("Global variable before block:", var)
# Local variable inside a block
if True:
    var_local = "I am a Local Variable"
    print("Inside block (Local Variable):", var_local)
# Printing the global variable again
print("Global variable after block:", var)



#4 Define the local and Global variables with the same name and print both variables and understand the scope of the variables
# Defining variables of different data types
integer_var = 10          # Integer
boolean_var = True        # Boolean
char_var = 'A'            # Character (In Python, characters are just strings of length 1)
float_var = 10.5          # Float
double_var = 20.123456789 # Double (Python does not have a separate double type, float covers both)

# Printing variables on the console
print("Integer Value:", integer_var)
print("Boolean Value:", boolean_var)
print("Character Value:", char_var)
print("Float Value:", float_var)
print("Double Value:", double_var)  # Same as float in Python


