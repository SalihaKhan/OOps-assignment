class Book:
    total_books = 0  # Class variable to track total books
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()  # Call class method when new book is created
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1  # Increment the class variable
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books  # Class method to access the count

# Usage
print("Initial book count:", Book.get_total_books())  # 0

book1 = Book("The Great Gatsby")
book2 = Book("To Kill a Mockingbird")

print("Total books after creation:", Book.get_total_books())  # 2