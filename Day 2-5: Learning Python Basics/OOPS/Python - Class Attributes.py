# Every Python class keeps the following built-in attributes and they can be accessed using dot operator like any other attribute −

# __dict__ − Dictionary containing the class's namespace.

# __doc__ − Class documentation string or none, if undefined.

# __name__ − Class name.

# __module__ − Module name in which the class is defined. This attribute is "__main__" in interactive mode.

# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.

# For the above class, let us try to access all these attributes −


class Intern:
    def __init__(self, name="Sikaundi", age=50):
        self.name = name
        self.age = age

    def displayIntern(self):
        print("Name : ", self.name, ", age: ", self.age)


print("Intern.__doc__:", Intern.__doc__)
print("Intern.__name__:", Intern.__name__)
print("Intern.__module__:", Intern.__module__)
print("Intern.__bases__:", Intern.__bases__)
print("Intern.__dict__:", Intern.__dict__)
