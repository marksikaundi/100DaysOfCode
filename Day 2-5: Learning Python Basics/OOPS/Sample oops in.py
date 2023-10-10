# Define a class
class Car:
    # Define class variables
    wheels = 4
    doors = 4

    # Define class methods
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

# Create an object of the class
my_car = Car()

# Access class variables
print(my_car.wheels) # Output: 4
print(my_car.doors) # Output: 4

# Call class methods
my_car.start() # Output: Car started
my_car.stop() # Output: Car stopped
