#1 Define a static variable and access that through a class
class MyClass:
    static_var = 100  # Static variable

# Accessing static variable using class name
print("Access using class name:", MyClass.static_var)

# Creating instances
obj1 = MyClass()
obj2 = MyClass()

# Accessing static variable using instances
print("Access using obj1:", obj1.static_var)
print("Access using obj2:", obj2.static_var)

# Modifying static variable through class
MyClass.static_var = 200

print("After modification:")
print("Access using class name:", MyClass.static_var)
print("Access using obj1:", obj1.static_var)
print("Access using obj2:", obj2.static_var)



#2 Define a static variable and access that through a instance
class MyClass:
    static_var = 100  # Static variable

# Creating an instance of the class
obj = MyClass()

# Accessing the static variable using the instance
print("Access through instance:", obj.static_var)

# Modifying the static variable using the class
MyClass.static_var = 200

# Accessing after modification
print("After modification, access through instance:", obj.static_var)



#3 Define a static variable and change within the instance
class MyClass:
    static_var = 100  # Static variable

# Creating an instance
obj = MyClass()

# Modifying static variable using the instance
obj.static_var = 200  # This creates an instance variable, not modifying the static variable

# Printing values
print("Access through instance:", obj.static_var)
print("Access through class:", MyClass.static_var)



#4 Define a static variable and change within the class
class MyClass:
    static_var = 100  # Static variable

# Modify the static variable directly within the class
MyClass.static_var = 200

# Print the modified value
print("Modified static variable:", MyClass.static_var)