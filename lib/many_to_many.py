class Author:
    all = []  # Class-level list to keep track of all Author instances
    def __init__(self, name):
        self.name = name
        Author.all.append(self)  # Add this instance to the class-level list of all authors

class Book:
    all = []  # Class-level list to keep track of all Book instances
    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # Add this instance to the class-level list of all books

    def contracts(self):
        # This method would return a list of Contract instances associated with this book
        return [Contract() for _ in self.all_titles]  # Placeholder implementation
    
    def authors(self):
        # This method would return a list of author names for this book using Contract class as intermediary
        return [author.name for author in self.all_authors]  # Placeholder implementation

class Contract:
    pass