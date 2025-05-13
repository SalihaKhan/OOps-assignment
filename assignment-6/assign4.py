class Bank:
    bank_name = "Bank of Pakistan"

    def __init__(self, branch_name):
        self.branch_name = branch_name

    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    def bank_info(self):
        print(f"{self.branch_name} of {self.bank_name}")

# Create an instance
obj = Bank("Main Branch")
obj.bank_info()  # Output: "Main Branch of Bank of Pakistan"

# Change bank name (affects all instances)
Bank.change_bank_name("National Bank of Pakistan")

# Check existing instance
obj.bank_info()  # Now: "Main Branch of National Bank of Pakistan"

# New instance also uses updated name
obj2 = Bank("Lahore Branch")
obj2.bank_info()  # Output: "Lahore Branch of National Bank of Pakistan"