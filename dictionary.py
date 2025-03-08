# 1. Create a Dictionary with at least 5 key-value pairs of Student ID and Name
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Emma"
}

# 1.1 Adding values to the dictionary
students[106] = "Frank"
print("After Adding:", students)

# 1.2 Updating values in the dictionary
students[102] = "Benjamin"
print("After Updating:", students)

# 1.3 Accessing values in the dictionary
print("Accessing Student with ID 103:", students[103])

# 1.4 Create a nested loop dictionary
nested_students = {
    "Class A": {201: "Grace", 202: "Henry"},
    "Class B": {203: "Ivy", 204: "Jack"}
}
print("Nested Dictionary:", nested_students)

# 1.5 Access values of a nested loop dictionary
print("Accessing Class A Students:", nested_students["Class A"])
print("Accessing Student with ID 202 in Class A:", nested_students["Class A"][202])

# 1.6 Print the keys present in a particular dictionary
print("Keys in students dictionary:", students.keys())

# 1.7 Delete a value from a dictionary
del students[104]
print("After Deletion:", students)