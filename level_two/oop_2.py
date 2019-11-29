
# INHERITANCE

class Animal():
    def __int__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")
    
    def eat(self):
        print("Eating")

class Dog(Animal):
    def __int__(self):
        #Animal.__init__(self)
        print("Dog crated")
    def eat(self): # overriding
        print("Dog Eating")

# SPECIAL METHODS

class Book():
    def __init__(self, title, author, pages):
        self.author = author
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return "Title: {}, Author: {}, Pages: {}".format( self.title, self.author,self.pages)
    
    def __len__(self):
        return self.pages
    
    def __del__(self):
        print("A book was destroyed")

book = Book("Dance", "Jean", 852)
print(book)
print(len(book))
del book
