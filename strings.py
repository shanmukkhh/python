# 1. Different ways creating a string
str1 = 'Hello' #single quotes
print(str1)

str2 = "Hello" #Double Quotes
print(str2)

str3 = '''Hello 
World'''
print(str3) #Triple Single Quotes

str4 = """Hello
World"""
print(str4) #Triple Double Quotes


str5 = 'Hello' + ' ' + 'World' 
print(str5) #String Concatenation

str6 = 'Hello ' * 3  # Repeats the string 3 times
print(str6) #String Multiplication


str7 = 'It\'s a beautiful day' #Escape Characters
print(str7)


str8 = r'C:\Users\Name\Documents'
print(str8) #Raw String

str9 = u'Hello' #Unicode Strings
print(str9)


a = 'Hello' #Variables to Store Strings
b = 'World'
str10 = a + ' ' + b
print(str10)



# 2. Concatenating two strings using + operator
str1 = "Hello"
str2 = "World"

# Concatenation using +
result = str1 + " " + str2  

# Printing the concatenated string
print(result)



# 3. Finding the length of the string
str1 = "HelloWorld"
count = 0
# Counting characters using a loop
for char in str1:
    count += 1
# Printing the length of the string
print("Length of the string:", count)



# 4. Extract a string using Substring
string = "HelloWorld"
start = 2  # Starting index
end = 7    # Ending index (exclusive)

# Extracting substring manually
substring = ""
for i in range(start, end):
    substring += string[i]

# Printing the extracted substring
print("Extracted Substring:", substring)



# 5. Searching in strings using index()
string = "HelloWorld"
substring = "World"
found_index = -1  # Default to -1 if not found

# Searching for substring manually
for i in range(len(string) - len(substring) + 1):
    match = True
    for j in range(len(substring)):
        if string[i + j] != substring[j]:
            match = False
            break
    if match:
        found_index = i
        break

# Printing the index of the substring
if found_index != -1:
    print("Substring found at index:", found_index)
else:
    print("Substring not found")



# 6. Matching a String Against a Regular Expression With matches()
string = "hello123"
pattern = "hello[0-9]+"  # Regular expression equivalent

# Checking if the string matches the pattern manually
match = True
if len(string) < 5 or string[:5] != "hello":
    match = False
else:
    for i in range(5, len(string)):
        if not ('0' <= string[i] <= '9'):  # Check if it's a digit
            match = False
            break

# Printing result
if match:
    print("String matches the pattern!")
else:
    print("String does not match the pattern.")



# 7. Comparing strings
str1 = "apple"
str2 = "apple"

# Manual comparison
equal = True
if len(str1) != len(str2):
    equal = False
else:
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            equal = False
            break

# Printing the result
if equal:
    print("The strings are equal.")
else:
    print("The strings are not equal.")



# 8. startsWith(), endsWith() and compareTo()
#Implementing startsWith()
string = "hello world"
prefix = "hello"

# Check if the string starts with the prefix manually
starts_with = True
if len(prefix) > len(string):
    starts_with = False
else:
    for i in range(len(prefix)):
        if string[i] != prefix[i]:
            starts_with = False
            break

print("Starts with:", starts_with)  # Output: True


string = "hello world"
suffix = "world"

# Check if the string ends with the suffix manually
ends_with = True
if len(suffix) > len(string):
    ends_with = False
else:
    for i in range(1, len(suffix) + 1):  # Compare from the end
        if string[-i] != suffix[-i]:
            ends_with = False
            break

print("Ends with:", ends_with)  # Output: True


# Manual compareTo() implementation
str1 = "apple"
str2 = "banana"

result = 0
for i in range(min(len(str1), len(str2))):
    if str1[i] != str2[i]:
        result = ord(str1[i]) - ord(str2[i])  # ASCII difference
        break

# If no difference is found, compare lengths
if result == 0:
    result = len(str1) - len(str2)

print("Comparison result:", result)  # Output: Negative (apple < banana)



# 9. Trimming strings with strip()
string = "   Hello, World!   "
trimmed_string = ""

# Finding the first non-space character
start = 0
while start < len(string) and string[start] == " ":
    start += 1

# Finding the last non-space character
end = len(string) - 1
while end > start and string[end] == " ":
    end -= 1

# Extracting the trimmed part
for i in range(start, end + 1):
    trimmed_string += string[i]

print("Original String:", repr(string))
print("Trimmed String:", repr(trimmed_string))



# 10. Replacing characters in strings with replace()
string = "hello world"
old_char = "o"
new_char = "x"
new_string = ""

# Iterate through the string and replace characters manually
for char in string:
    if char == old_char:
        new_string += new_char  # Replace the character
    else:
        new_string += char  # Keep the character as is

print("Original String:", string)
print("Modified String:", new_string)



# 11. Splitting strings with split()
string = "hello world this is python"
delimiter = " "
words = []
word = ""

# Iterate through the string
for char in string:
    if char == delimiter:
        if word:  # Avoid adding empty words
            words.append(word)  # Store the word in the list
            word = ""  # Reset word
    else:
        word += char  # Append character to current word

# Add the last word if it exists
if word:
    words.append(word)

print("Original String:", string)
print("Splitted List:", words)



# 12. Converting integer objects to Strings
num = 12345
digits = "0123456789"
string_num = ""

# Handling negative numbers
if num < 0:
    num = -num
    string_num += "-"

# Extracting digits manually
temp = []
while num > 0:
    remainder = num % 10  # Get the last digit
    temp.append(digits[remainder])  # Convert digit to character
    num //= 10  # Remove the last digit

# Reverse the list to get the correct order
for i in range(len(temp) - 1, -1, -1):
    string_num += temp[i]

# Edge case: If num was 0
if not string_num or string_num == "-":
    string_num = "0"

print("Converted String:", string_num)
print("Type:", type(string_num))



# 13. Converting to uppercase and lowercase
  # Convert to uppercase
string = "Hello World"
uppercase_string = ""

for char in string:
    if 'a' <= char <= 'z':  # Check if lowercase
        uppercase_string += chr(ord(char) - 32)  # Convert to uppercase
    else:
        uppercase_string += char  # Keep non-alphabet characters unchanged

print("Uppercase:", uppercase_string)


# Convert to lowercase
string = "Hello World"
lowercase_string = ""

for char in string:
    if 'A' <= char <= 'Z':  # Check if uppercase
        lowercase_string += chr(ord(char) + 32)  # Convert to lowercase
    else:
        lowercase_string += char  # Keep non-alphabet characters unchanged

print("Lowercase:", lowercase_string)