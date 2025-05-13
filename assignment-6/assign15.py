class A:
    def show(self):
        print("A.show()")

class B(A):
    def show(self):
        print("B.show()")

class C(A):
    def show(self):
        print("C.show()")

class D(B, C):
    pass  # Inherits from both B and C

# Create instance of D
d = D()

# Call show() - which version gets called?
d.show()  # Output depends on MRO

# Display the Method Resolution Order
print(D.__mro__)
# or alternatively:
print(D.mro())