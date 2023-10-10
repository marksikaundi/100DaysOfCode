# Every Python class keeps the following built-in attributes and they can be accessed using dot operator like any other attribute −

# __dict__ − Dictionary containing the class's namespace.

# __doc__ − Class documentation string or none, if undefined.

# __name__ − Class name.

# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

# For the above class, let us try to access all these attributes −


class Employee:
    def __init__(self, name="Bhavana", age=24):
        self.name = name
        self.age = age

    def displayEmployee(self):
        print("Name : ", self.name, ", age: ", self.age)


print("Employee.__doc__:", Employee.__doc__)
print("Employee.__name__:", Employee.__name__)
print("Employee.__module__:", Employee.__module__)
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)
