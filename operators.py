#1 Write a function for arithmetic operators(+,-,*,/)
# Taking input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Performing arithmetic operations
addition = a + b
subtraction = a - b
multiplication = a * b
division = a / b if b != 0 else "Cannot divide by zero"  # Handling division by zero
# Printing the results
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)


#2 Write a method for increment and decrement operators(++, --)
# Initializing a variable
num = 10
print("Initial value:", num)

# Increment operation
num += 1  # Equivalent to num = num + 1
print("After increment:", num)

# Decrement operation
num -= 1  # Equivalent to num = num - 1
print("After decrement:", num)


#3 Write a program to find the two numbers equal or not.
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
# Checking if the numbers are equal
if num1 == num2:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")


#4 Program for relational operators (<,<==, >, >==)
# Taking input from the user
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Performing relational operations
print("a < b  :", a < b)   # Less than
print("a <= b :", a <= b)  # Less than or equal to
print("a > b  :", a > b)   # Greater than
print("a >= b :", a >= b)  # Greater than or equal to


#5 Print the smaller and larger number
# Taking input from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Finding the larger and smaller number
if num1 > num2:
    print("Larger number:", num1)
    print("Smaller number:", num2)
elif num1 < num2:
    print("Larger number:", num2)
    print("Smaller number:", num1)
else:
    print("Both numbers are equal:", num1)