class Multiplier:
    def __init__(self, factor):
        """Initialize with a multiplication factor"""
        self.factor = factor
    
    def __call__(self, x):
        """Make the instance callable like a function"""
        return x * self.factor


# Testing the Multiplier class
multiply_by_5 = Multiplier(5)

# 1. Test with callable()
print("Is multiply_by_5 callable?", callable(multiply_by_5))  # Output: True

# 2. Call the object like a function
result = multiply_by_5(10)
print("10 multiplied by 5:", result)  # Output: 50

# 3. Create another multiplier and test it
double = Multiplier(2)
print("7 doubled:", double(7))  # Output: 14
print("Is double callable?", callable(double))  # Output: True