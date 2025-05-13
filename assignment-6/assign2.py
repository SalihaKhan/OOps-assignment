# Define a class named Counter
class Counter:
    # Class variable to keep track of the number of instances created
    count = 0

    # Constructor method called when a new object is created
    def __init__(self):
        # Increment the class variable 'count' by 1 every time a new object is instantiated
        Counter.count += 1

    # Class method to display the current value of 'count'
    @classmethod
    def display_counter(cls):
        # Print the total number of Counter objects created
        print(f"Total objects: {cls.count}")

# Create multiple instances of the Counter class
obj1 = Counter()
obj2 = Counter()
obj3 = Counter()
obj4 = Counter()

# Call the class method to display how many Counter objects have been created
Counter.display_counter()
