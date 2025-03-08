# 1. Write a function to add integer values of an array
# Define the array
numbers = [1, 2, 3, 4, 5]

# Initialize sum variable
total = 0

# Loop through the array and add elements
for num in numbers:
    total += num

# Print the sum
print("Sum of array elements:", total)



# 2. Write a function to calculate the average value of an array of integers
# Define the array
numbers = [10, 20, 30, 40, 50]

# Initialize sum variable
total = 0

# Get the length of the array
count = len(numbers)

# Loop through the array to calculate the sum
for num in numbers:
    total += num
    
# Calculate the average
average = total / count if count != 0 else 0  # Avoid division by zero
# Print the average
print("Average value of array:", average)



# 3. Write a program to find the index of an array element
# Define the array
numbers = [10, 20, 30, 40, 50]

# Input the element to search
target = int(input("Enter the number to find its index: "))

# Initialize a variable to store the index
index = -1  

# Loop through the array to find the element
for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break  # Stop once we find the element

# Print the index if found, otherwise print not found
if index != -1:
    print("Index of", target, "is:", index)
else:
    print(target, "is not in the array")



# 4. Write a function to test if array contains a specific value
# Define the array
numbers = [10, 20, 30, 40, 50]

# Input the number to search
target = int(input("Enter the number to search: "))

# Initialize a flag to check if the number is found
found = False  

# Loop through the array to search for the target
for num in numbers:
    if num == target:
        found = True
        break  # Stop searching once found

# Print the result
if found:
    print(target, "is present in the array.")
else:
    print(target, "is not in the array.")



# 5. Write a function to remove a specific element from an array
# Define the array
numbers = [10, 20, 30, 40, 50]

# Input the number to remove
target = int(input("Enter the number to remove: "))

# Create a new list to store updated elements
new_numbers = []

# Loop through the array and add only elements that are not the target
for num in numbers:
    if num != target:
        new_numbers.append(num)

# Print the updated array
print("Updated array:", new_numbers)



# 6. Write a function to copy an array to another array
# Define the original array
original_array = [10, 20, 30, 40, 50]

# Create an empty list for the copied array
copied_array = []

# Loop through the original array and copy each element
for num in original_array:
    copied_array.append(num)

# Print both arrays
print("Original Array:", original_array)
print("Copied Array:", copied_array)



# 7. Write a function to insert an element at a specific position in the array
# Define the original array
numbers = [10, 20, 30, 40, 50]

# Input the element to insert
element = int(input("Enter the element to insert: "))

# Input the position (0-based index)
position = int(input("Enter the position to insert at (0-based index): "))

# Create a new list for the updated array
new_numbers = []

# Loop through the original array and insert the new element at the correct position
for i in range(len(numbers) + 1):
    if i < position:
        new_numbers.append(numbers[i])  # Copy elements before the position
    elif i == position:
        new_numbers.append(element)  # Insert the new element
    else:
        new_numbers.append(numbers[i - 1])  # Copy the remaining elements

# Print the updated array
print("Updated Array:", new_numbers)



# 8. Write a function to find the minimum and maximum value of an array
# Define the array
numbers = [15, 3, 22, 7, 9, 34, 2, 18]

# Initialize min and max with the first element
minimum = numbers[0]
maximum = numbers[0]

# Loop through the array to find min and max
for num in numbers:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num

# Print the results
print("Minimum value:", minimum)
print("Maximum value:", maximum)



# 9. Write a function to reverse an array of integer values
# Define the original array
numbers = [10, 20, 30, 40, 50]

# Create an empty list for the reversed array
reversed_array = []

# Loop through the array in reverse order and store elements
for i in range(len(numbers) - 1, -1, -1):
    reversed_array.append(numbers[i])

# Print the reversed array
print("Reversed Array:", reversed_array)



# 10. Write a function to find the duplicate values of an array
# Define the array
numbers = [10, 20, 30, 10, 40, 50, 20, 60, 30]

# Create an empty list to store duplicates
duplicates = []

# Loop through the array to check for duplicates
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):  # Compare with the next elements
        if numbers[i] == numbers[j] and numbers[i] not in duplicates:
            duplicates.append(numbers[i])  # Store only unique duplicates

# Print the duplicate values
print("Duplicate values:", duplicates)



# 11. Write a program to find the common values between two arrays
# Define two arrays
array1 = [10, 20, 30, 40, 50, 60]
array2 = [30, 50, 70, 90, 20]

# Create an empty list to store common values
common_values = []

# Loop through both arrays to find common elements
for i in range(len(array1)):
    for j in range(len(array2)):
        if array1[i] == array2[j] and array1[i] not in common_values:
            common_values.append(array1[i])  # Store only unique common values

# Print the common values
print("Common values:", common_values)



# 12. Write a method to remove duplicate elements from an array
# Define the original array
numbers = [10, 20, 30, 10, 40, 50, 20, 60, 30]

# Create an empty list to store unique elements
unique_numbers = []

# Loop through the array and add only unique elements
for i in range(len(numbers)):
    is_duplicate = False  # Flag to check if the element is a duplicate
    for j in range(i):  # Check previous elements
        if numbers[i] == numbers[j]:
            is_duplicate = True
            break  # Stop checking once a duplicate is found
    if not is_duplicate:
        unique_numbers.append(numbers[i])  # Add only non-duplicates

# Print the array after removing duplicates
print("Array after removing duplicates:", unique_numbers)



# 13. Write a method to find the second largest number in an array
# Define the array
numbers = [10, 20, 30, 40, 50, 60]

# Initialize largest and second largest
largest = numbers[0]
second_largest = None

# Loop through the array to find the largest number
for i in range(1, len(numbers)):
    if numbers[i] > largest:
        second_largest = largest  # Update second largest
        largest = numbers[i]  # Update largest
    elif second_largest is None or (numbers[i] > second_largest and numbers[i] != largest):
        second_largest = numbers[i]  # Update second largest if needed

# Print the second largest number
print("Second largest number:", second_largest)



# 14. Write a method to find the second largest number in an array
# Define the array
numbers = [10, 20, 30, 40, 50, 60]

# Initialize largest and second largest
largest = numbers[0]
second_largest = None

# Loop through the array to find the largest number
for i in range(1, len(numbers)):
    if numbers[i] > largest:
        second_largest = largest  # Update second largest
        largest = numbers[i]  # Update largest
    elif second_largest is None or (numbers[i] > second_largest and numbers[i] != largest):
        second_largest = numbers[i]  # Update second largest if needed

# Print the second largest number
print("Second largest number:", second_largest)


# 15. Write a method to find number of even number and odd numbers in an array
# Define the array
numbers = [10, 23, 45, 66, 78, 99, 100, 35, 50]

# Initialize counters
even_count = 0
odd_count = 0

# Loop through the array to count even and odd numbers
for i in range(len(numbers)):
    if numbers[i] % 2 == 0:  # Check if the number is even
        even_count += 1
    else:  # Otherwise, it's odd
        odd_count += 1

# Print the counts
print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)



# 16. Write a function to get the difference of largest and smallest value
# Define the array
numbers = [12, 45, 2, 67, 34, 89, 5]

# Initialize variables
largest = numbers[0]
smallest = numbers[0]

# Loop through the array to find the largest and smallest numbers
for i in range(1, len(numbers)):
    if numbers[i] > largest:
        largest = numbers[i]
    elif numbers[i] < smallest:
        smallest = numbers[i]

# Calculate and print the difference
difference = largest - smallest
print("Difference between largest and smallest value:", difference)



# 17. Write a method to verify if the array contains two specified elements(12,23)
numbers = [5, 12, 7, 23, 9, 18]

element1 = 12
element2 = 23

if element1 in numbers and element2 in numbers:
    print(f"The array contains both {element1} and {element2}.")
else:
    print(f"The array does not contain both {element1} and {element2}.")





# 18. Write a program to remove the duplicate elements and return the new array
# Define the array with duplicates
numbers = [10, 20, 30, 10, 40, 50, 20, 60, 50]

# Create an empty array to store unique elements
unique_numbers = []

# Loop through the original array
for i in range(len(numbers)):
    duplicate = False  # Flag to check if the element already exists in unique_numbers
    for j in range(len(unique_numbers)):  # Check existing unique elements
        if numbers[i] == unique_numbers[j]:
            duplicate = True
            break  # Stop checking further if duplicate is found
    if not duplicate:  # If it's not a duplicate, add it to unique_numbers
        unique_numbers.append(numbers[i])

# Print the new array without duplicates
print("Array after removing duplicates:", unique_numbers)