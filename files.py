# 1 Write a program to read text file
# Open the file in read mode
file = open("sample.txt", "r")

# Read the entire content of the file
content = file.read()

# Print the file content
print(content)

# Close the file
file.close()



# 2 Write a program to write text to .txt file using InputStream
# Open a file in write mode ('w' will overwrite if the file exists)
file = open("output.txt", "w")

# Write content to the file
file.write("Hello, this is a sample text written to the file.\n")
file.write("This is another line in the text file.\n")

# Close the file
file.close()

print("Text written successfully to output.txt")



# 3 Write a program to read a file stream
# Open the file in read mode
file = open("sample.txt", "r")

# Read the contents of the file
content = file.read()

# Print the content
print("File Content:\n", content)

# Close the file
file.close()



# 4 Write a program to read a file stream supports random access
# Open the file in read mode
with open("sample.txt", "r") as file:
    # Move to the 10th byte in the file
    file.seek(10)
    
    # Read the next 20 bytes from the current position
    content = file.read(20)
    
    print("Random Access Read:", content)

# 5 Write a program to read a file a just to a particular index using seek()
# Open the file in read mode
with open("sample.txt", "r") as file:
    # Define the index up to which we want to read
    index = 15  # Change this as needed

    # Move the file pointer to the beginning
    file.seek(0)
    
    # Read only up to the specified index
    content = file.read(index)
    
    print(f"Content up to index {index}:")
    print(content)

# 6 Write a program to check whether a file is having read access and write access permissions
import os

# File to check
file_path = "sample.txt"  # Change this to your file name

# Check if the file exists
if os.path.exists(file_path):
    # Check for read permission
    if os.access(file_path, os.R_OK):
        print(f"The file '{file_path}' has READ access.")
    else:
        print(f"The file '{file_path}' does NOT have READ access.")

    # Check for write permission
    if os.access(file_path, os.W_OK):
        print(f"The file '{file_path}' has WRITE access.")
    else:
        print(f"The file '{file_path}' does NOT have WRITE access.")
else:
    print(f"The file '{file_path}' does NOT exist.")