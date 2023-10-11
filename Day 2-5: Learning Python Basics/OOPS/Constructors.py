# In object-oriented programming, an object of a class is characterized by one or more instance variables or attributes, whose values are unique to each object. For example, if the Employee class has an instance attribute as name. Each of its objects e1 and e2 may have different value for the name variable.

# A constructor is an instance method in a class, that is automatically called whenever a new object of the class is declared. The constructor' role is to assign value to instance variables as soon as the object is declared.

# Python uses a special method called __init__() to initialize the instance variables for the object, as soon as it is declared.

# The __init__() method acts as a constructor. It needs a mandatory argument self, which the reference to the object.

def __init__(self):
# initialize instance variables

# In object-oriented programming, an object of a class is characterized by one or more instance variables or attributes, whose values are unique to each object. For example, if the Employee class has an instance attribute as name. Each of its objects e1 and e2 may have different value for the name variable.

# A constructor is an instance method in a class, that is automatically called whenever a new object of the class is declared. The constructor' role is to assign value to instance variables as soon as the object is declared.

# Python uses a special method called __init__() to initialize the instance variables for the object, as soon as it is declared.

# The __init__() method acts as a constructor. It needs a mandatory argument self, which the reference to the object.

# Example
class Employee:
   'Common base class for all employees'
   def __init__(self):
      self.name = "Bhavana"
      self.age = 24

e1 = Employee()
print ("Name: {}".format(e1.name))
print ("age: {}".format(e1.age))
# It will produce the following output −
# Name: Mark
# Age: 19








