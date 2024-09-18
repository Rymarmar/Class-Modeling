class Person:
    def __init__(this, fname, lname):
        this.firstname = fname
        this.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


#Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

class Student(Person):
    def __init__(self, fname, lname, year=2020):
        super().__init__(fname, lname)
        self.graduationYear = year

    def __str__(self):
        return f"({self.firstname}, {self.lastname}, {self.graduationYear})"

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationYear)


x = Student("Mike", "Olsen", 2019)
x.printname()
print(x)
x.welcome()