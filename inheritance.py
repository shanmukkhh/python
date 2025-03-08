# A, B and C are classes
# A is a super class. B is a sub class of A. C is a sub class of B.


#1 Create three methods in each class, 2 methods are specific to each class and third
# method (override method) should be in all three Classes A, B and C
class A:
    def method_a1(self):
        print("Method A1: Unique to Class A")

    def method_a2(self):
        print("Method A2: Unique to Class A")

    def show(self):
        print("Show Method from Class A (Overridden)")

class B(A):  # B inherits from A
    def method_b1(self):
        print("Method B1: Unique to Class B")

    def method_b2(self):
        print("Method B2: Unique to Class B")

    def show(self):
        print("Show Method from Class B (Overridden)")

class C(B):  # C inherits from B
    def method_c1(self):
        print("Method C1: Unique to Class C")

    def method_c2(self):
        print("Method C2: Unique to Class C")

    def show(self):
        print("Show Method from Class C (Overridden)")

# Creating an instance of Class C
obj = C()

# Calling methods from Class C, B, and A
obj.method_a1()  # Inherited from A
obj.method_a2()  # Inherited from A
obj.method_b1()  # Inherited from B
obj.method_b2()  # Inherited from B
obj.method_c1()  # Defined in C
obj.method_c2()  # Defined in C

# Calling overridden method
obj.show()  # Calls C's version of show()



#2 Create a class with main method. Create an object for each class A, B and C in main
# method and call every method of each class using its own object/instance.
class A:
    def method_a1(self):
        print("Method A1: Unique to Class A")

    def method_a2(self):
        print("Method A2: Unique to Class A")

    def show(self):
        print("Show Method from Class A (Overridden in subclasses)")

class B(A):  # B inherits from A
    def method_b1(self):
        print("Method B1: Unique to Class B")

    def method_b2(self):
        print("Method B2: Unique to Class B")

    def show(self):
        print("Show Method from Class B (Overridden in subclasses)")

class C(B):  # C inherits from B
    def method_c1(self):
        print("Method C1: Unique to Class C")

    def method_c2(self):
        print("Method C2: Unique to Class C")

    def show(self):
        print("Show Method from Class C")

# Main method
if __name__ == "__main__":
    # Object of Class A
    objA = A()
    print("Calling methods from Class A:")
    objA.method_a1()
    objA.method_a2()
    objA.show()
    
    print("\nCalling methods from Class B:")
    # Object of Class B
    objB = B()
    objB.method_a1()  # Inherited from A
    objB.method_a2()  # Inherited from A
    objB.method_b1()
    objB.method_b2()
    objB.show()

    print("\nCalling methods from Class C:")
    # Object of Class C
    objC = C()
    objC.method_a1()  # Inherited from A
    objC.method_a2()  # Inherited from A
    objC.method_b1()  # Inherited from B
    objC.method_b2()  # Inherited from B
    objC.method_c1()
    objC.method_c2()
    objC.show()



#3 Call an overridden method with super class reference to B and C class’s objects
class A:
    def show(self):
        print("Show Method from Class A")

class B(A):
    def show(self):
        print("Show Method from Class B")

class C(B):
    def show(self):
        print("Show Method from Class C")

# Creating superclass reference
obj1 = A()  # Reference to Class A
obj2 = B()  # Reference to Class B
obj3 = C()  # Reference to Class C

print("Calling show() using Superclass Reference:")
ref = obj2  # Superclass reference to B object
ref.show()  # Calls show() of B

ref = obj3  # Superclass reference to C object
ref.show()  # Calls show() of C



#4 Runtime Polymorphism with Data Members/Instance variables, Repeat the above
# process only for data members
class A:
    def __init__(self):
        self.value = "Value from Class A"

class B(A):
    def __init__(self):
        super().__init__()  # Calls A's constructor
        self.value = "Value from Class B"  # Overrides value in B

class C(B):
    def __init__(self):
        super().__init__()  # Calls B's constructor
        self.value = "Value from Class C"  # Overrides value in C

# Superclass reference pointing to subclass objects
ref = A()
print("Using A object:", ref.value)  # Value from Class A

ref = B()
print("Using B object:", ref.value)  # Value from Class B

ref = C()
print("Using C object:", ref.value)  # Value from Class C