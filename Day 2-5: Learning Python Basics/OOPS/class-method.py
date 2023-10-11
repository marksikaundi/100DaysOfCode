# Python has a built-in function classmethod() which transforms an instance method to a class method which can be called with the reference to the class only and not the object.

# Syntax
classmethod(instance_method) # returns a class method for given instance method

# Example:
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_age(cls):
        print("The age is:",cls.age)
    print_age = classmethod(print_age)
    
    
    
# Example
# In the Employee class, define a showcount() instance method with the "self" argument (reference to calling object). It prints the value of empCount. Next, transform the method to class method counter() that can be accessed through the class reference.

class Employee:
    emptyCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emptyCount += 1
    def showcount(self):
        print(self.emptyCount)
    counter = classmethod(showcount)
    
# Accessing class method
e1 = Employee("John", 10000)
e2 = Employee("Mary", 20000)
e3 = Employee("Bob", 30000)

e1.showcount() # 3
Employee.showcount() # 3

# Output
# Call showcount() with object and call count() with class, both show the value of employee count.

# Using @classmethod() decorator is the prescribed way to define a class method as it is more convenient than first declaring an instance method and then transforming to a class method.
@classmethod
def showcount(cls):
    print(cls.emptyCount)
    
Employee.showcount() # 3

# The class method acts as an alternate constructor. Define a newemployee() class method with arguments required to construct a new object. It returns the constructed object, something that the __init__() method does.

@classmethod
def showcount(cls):
    print (cls.empCount)
    return
@classmethod
def newemployee(cls, name, age):
    return cls(name, age)

e1 = Employee.newemployee("John", 10000)
e2 = Employee.newemployee("Mary", 20000)    
e3 = Employee.newemployee("Bob", 30000)
e4 = Employee.newemployee("Alice", 40000)

Employee.showcount() # 4





