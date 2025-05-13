# Define the Car class
class Car:
    # Public variable
    def __init__(self, brand):
        self.brand = brand

    # Public method
    def start(self):
        print(f"The {self.brand} car is starting.")

# Instantiate the class
my_car = Car("Toyota")

# Access the public variable
print("Car Brand:", my_car.brand)

# Call the public method
my_car.start()
