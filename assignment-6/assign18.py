class Product:
    def __init__(self, price):
        self._price = price  # Private attribute

    @property
    def price(self):
        """Getter for price"""
        print("Getting price...")
        return self._price

    @price.setter
    def price(self, value):
        """Setter for price"""
        if value < 0:
            raise ValueError("Price cannot be negative")
        print(f"Setting price to {value}...")
        self._price = value

    @price.deleter
    def price(self):
        """Deleter for price"""
        print("Deleting price...")
        del self._price


# Testing the Product class
product = Product(100.0)

# Using the getter
print(product.price)  # Output: Getting price... \n 100.0

# Using the setter
product.price = 150.0  # Output: Setting price to 150.0...

# Trying to set negative price
try:
    product.price = -50.0
except ValueError as e:
    print(e)  # Output: Price cannot be negative

# Using the deleter
del product.price  # Output: Deleting price...

# After deletion, accessing price will raise AttributeError
try:
    print(product.price)
except AttributeError:
    print("Price attribute doesn't exist")  # Output: Price attribute doesn't exist