class Countdown:
    def __init__(self, start):
        self.start = start + 1  # We add 1 because we decrement first in __next__

    def __iter__(self):
        return self  # The object is both the iterable and iterator

    def __next__(self):
        self.start -= 1
        if self.start < 0:
            raise StopIteration  # Signal the end of iteration
        return self.start


# Testing the Countdown class
print("Countdown from 5:")
for num in Countdown(5):
    print(num)

print("\nCountdown from 3:")
for num in Countdown(3):
    print(num)

print("\nCountdown from 0:")
for num in Countdown(0):
    print(num)  # Will print nothing