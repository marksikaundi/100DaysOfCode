# is that the static method doesn't have a mandatory argument like reference to the object − self or reference to the class − cls. Python's standard library fimction staticmethod() returns a static method.

# In the Employee class below, a method is converted into a static method. This static method can now be called by its object or reference of class itself.

class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

        # @staticmethod
        def showcount():
            print(Employee.empCount)
            return
        counter = staticmethod(showcount)


# Accessing static method
e1 = Employee("John", 10000)
e2 = Employee("Mary", 20000)
e3 = Employee("Bob", 30000)

e1.counter()  # 3
Employee.counter()  # 3

# Python also has @staticmethod decorator that conveniently returns a static method.


@staticmethod
def showcount():
    print(Employee.empCount)


e1.showcount()  # 3
Employee.showcount()  # 3
