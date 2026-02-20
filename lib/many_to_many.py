class Author:
    all = []  # Class-level list to keep track of all Author instances
    def __init__(self, name):
        self.name = name
        Author.all.append(self)  # Add this instance to the class-level list of all authors

    def contracts(self):
        # This method would return a list of contracts associated with this author
        return [contract for contract in Contract.all if contract.author == self]  # Placeholder implementation

    def books(self):
        # This method would return a list of Book instances associated with this author using Contract class as intermediary
        # use contracts method to get unique books
        return list(set(contract.book for contract in self.contracts()))  # Placeholder implementation
    
    def sign_contract(self, book, date, royalties):
        # This method would create a new Contract instance and add it to the appropriate lists
        new_contract = Contract(self, book, date, royalties)
        return new_contract

    def total_royalties(self):
        # This method would sum up all royalties for this author's contracts
        return sum(contract.royalties for contract in self.contracts())  # Placeholder implementation

class Book:
    all = []  # Class-level list to keep track of all Book instances
    def __init__(self, title):
        self.title = title
        Book.all.append(self)  # Add this instance to the class-level list of all books

    def contracts(self):
        # This method would return a list of Contract instances associated with this book
        return [contract for contract in Contract.all if contract.book == self]  # Placeholder implementation
    
    def authors(self):
        # This method would return a list of author names for this book using Contract class as intermediary
        return list(set(contract.author for contract in self.contracts()))  # Placeholder implementation
class Contract:
    all = []  # Class-level list to keep track of all Contract instances
    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("Author must be an instance of Author class")
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of Book class") 
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int):
            raise Exception("Royalties must be a number")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
        # Here you would also add this contract to the appropriate lists in Author and Book instances

    @classmethod
    def all_contracts(cls):
        return sorted(cls.all, key=lambda contract: contract.date)  # This method would return a list of all Contract instances sorted by date