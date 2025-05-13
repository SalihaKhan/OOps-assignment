# 1. Create the custom exception
class InvalidAgeError(Exception):
    """Raised when age is below 18"""
    pass


# 2. Function that raises the custom exception
def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below minimum required age (18)")
    print(f"Age {age} is valid")


# 3. Test with try-except block
def test_age_checker():
    test_ages = [15, 20, 17, 25]
    
    for age in test_ages:
        try:
            check_age(age)
        except InvalidAgeError as e:
            print(f"Error for age {age}: {e}")


# Run the test
test_age_checker()