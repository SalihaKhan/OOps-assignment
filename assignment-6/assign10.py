class Dog:
    def __init__(self, name, breed):
        self.name = name    # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):         # Instance method
        print(f"{self.name} the {self.breed} says: Woof!")

# Create instances
dog1 = Dog("Max", "Golden Retriever")
dog2 = Dog("Bella", "Beagle")

# Call the instance method
dog1.bark()  # Output: Max the Golden Retriever says: Woof!
dog2.bark()  # Output: Bella the Beagle says: Woof!