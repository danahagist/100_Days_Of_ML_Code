# -------------------------------- Task ---------------------------------------------------
# Given a Book class and a Solution class, write a MyBook class that does the following:
#    Inherits from Book
#    Has a parameterized constructor taking these 3 parameters:
#        *string title
#        *string author
#        *int price
#    Implements the Book class' abstract display() method so it prints these 3 lines:
#        1. Title:, a space, and then the current instance's title.
#        2. Author, a space, and then the current instance's author.
#        3. Price, a space, and then the current instance's price.
#
# Note: Because these classes are being written in the same file, you must not use an access modifier
#  (e.g.: ) when declaring MyBook or your code will not execute.
#-----------------------------------------------------------------------------------------------------

#----------------------- HackerRank creates Book ABC (Abstract Base Class) ---------------------------

class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass
    
#------------------------------------------------------------------------------------------------------

#-------------------------------------- SOLUTION ------------------------------------------------------

#Write MyBook class
class MyBook(Book):
    # Initializing subclass
    def __init__(self,title,author,price):
        # Inheriting title and author definitions from Book class
        super().__init__(title,author)
        # Defining price
        self.price = price
     
    # Creating display method for the MyBook subclass
    def display(self):
        # Printing desired output
        print("Title:" , self.title)
        print("Author:" , self.author)
        print("Price:" , self.price)
        
# ------------------------------------ END SOLUTION ---------------------------------------------------

# ------------------------- HackerRank Input and MyBook instantiation ---------------------------------

title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

# -----------------------------------------------------------------------------------------------------
