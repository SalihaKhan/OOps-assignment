class Logger:
    def __init__(self, name):
        print(f"Logger '{name}' created!")
        self.name = name
    
    def __del__(self):
        print(f"Logger '{self.name}' destroyed!")

# Demonstration
def test_logger():
    print("Creating loggers...")
    logger1 = Logger("System")
    logger2 = Logger("App")
    print("About to exit function...")

print("Starting program...")
test_logger()
print("End of program")