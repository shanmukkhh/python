#1 Write a program to print “Bright IT Career” ten times using for loop
# Using a for loop to print the message 10 times
for i in range(10):
    print("Bright IT Career")



#2 Write a java program to print 1 to 20 numbers using the while loop.
public class PrintNumbers {
    public static void main(String[] args) {
        int num = 1; // Initialize the starting number
        
        while (num <= 20) { // Loop runs until num reaches 20
            System.out.println(num); // Print the current number
            num++; // Increment the number by 1
        }
    }
}



#3 Program to equal operator and not equal operators
a = 10
b = 20

# Using equal operator
if a == b:
    print("a is equal to b")
else:
    print("a is not equal to b")

# Using not equal operator
if a != b:
    print("a is not equal to b")
else:
    print("a is equal to b")



#4 Write a program to print the odd and even numbers.
# Get the range from the user
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

# Lists to store odd and even numbers
even_numbers = []
odd_numbers = []

# Loop through the range
for num in range(start, end + 1):
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Print the results
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)



#5 Write a program to print largest number among three numbers.
# Take three numbers as input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Determine the largest number
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3

# Print the result
print("The largest number is:", largest)



#6 Write a program to print even number between 10 and 20 using while
# Initialize the starting number
num = 10

# Loop until 20
while num <= 20:
    if num % 2 == 0:
        print(num, end=" ")  # Print even number
    num += 1  # Increment number



#7 Write a program to print 1 to 10 using the do-while loop statement.
# Initialize the number
num = 1

while True:  # Simulating a do-while loop
    print(num, end=" ")  # Print the number
    num += 1  # Increment the number
    
    if num > 10:  # Exit condition
        break



#8 Write a program to find Armstrong number or not
# Get input from the user
num = int(input("Enter a number: "))

# Find the number of digits
order = len(str(num))

# Initialize sum
sum = 0

# Store the original number
temp = num

# Calculate the sum of the power of digits
while temp > 0:
    digit = temp % 10  # Get the last digit
    sum += digit ** order  # Raise it to the power of number of digits
    temp //= 10  # Remove the last digit

# Check if the sum is equal to the original number
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")



#9 Write a program to find the prime or not.
# Get input from the user
num = int(input("Enter a number: "))

# A prime number is greater than 1
if num > 1:
    for i in range(2, int(num ** 0.5) + 1):  # Check divisibility up to sqrt(num)
        if num % i == 0:  # If divisible, it's not prime
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")  # If loop completes, it's prime
else:
    print(num, "is not a prime number")  # Numbers <= 1 are not prime



#10 Write a program to palindrome or not.
# Get input from the user
num = int(input("Enter a number: "))

# Convert the number to string and check if it's the same when reversed
if str(num) == str(num)[::-1]:
    print(num, "is a palindrome")
else:
    print(num, "is not a palindrome")



#11 Program to check whether a number is EVEN or ODD using switch
a = int(input('Enter Number to check is EVEN or ODD: '))
if a % 2 == 0:
    print("{0} is Even ".format(a))
else:
    print("{0} is Odd ".format(a))



#12 Print gender (Male/Female) program according to given M/F using switch
# Get input from the user
gender = input("Enter gender (M/F): ").strip().upper()  # Convert to uppercase to handle lowercase input

# Using match-case (Python 3.10+)
match gender:
    case "M":
        print("Gender: Male")
    case "F":
        print("Gender: Female")
    case _:
        print("Invalid input")