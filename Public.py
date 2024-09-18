import sys
# program to illustrate public access modifier in a class
class Geek:
    # constructor
    def __init__(self, name, age):
        # public data members
        self.geekName = name
        self.geekAge = age

    # public member function
    def displayAge(self):
        # accessing public data member
        print("Age: ", self.geekAge)

# creating object of the class
obj = Geek("R2J", 20)

# finding all the fields and methods which are present inside obj
print("List of fields and methods inside obj:", dir(obj))

# accessing public data member
print("Name:", obj.geekName)

# calling public member function of the class
obj.displayAge()

print(f"Size of object is: {sys.getsizeof(obj)}")

