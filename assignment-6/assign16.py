# Function Decorator Implementation
def log_function_call(func):
    """Decorator that logs when a function is called"""
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

# Applying the decorator
@log_function_call
def say_hello(name):
    """Greets the specified person"""
    print(f"Hello, {name}!")

# Test cases
def main():
    # First call
    print("Test 1:")
    say_hello("Alice")
    
    # Second call
    print("\nTest 2:")
    say_hello("Bob")

if __name__ == "__main__":
    main()