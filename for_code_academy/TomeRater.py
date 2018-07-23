# User Class

class User(object):
    def __init__(self, name, email):
        self.name=name
        self.email=email
        self.books = {}
        

    def __repr__(self):
        return "User {name}, email: {email}, books read : ".format(name=self.name, email=self.email)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        else:
            return False
        
    def get_email(self):
        return self.email

    def change_email(self, address):
        self.address=address
        self.email=self.address
        return "The email {old_email} has been changed to {new_email} ".format(old_email=self.email, new_email=self.address)
    
    def read_book(self, book , rating=None):
        self.book = book
        self.rating=rating
        if self.rating!=None:
            self.rating=int(rating)
            self.rating_range_check = self.rating
            if self.rating_range_check < 0 or self.rating_range_check > 4:
                self.rating=0
                self.books.update({book:self.rating})
                return self.books
            else:
                #self.books.update({book.__hash__():self.rating})
                self.books.update({book:self.rating})
                return self.books 
        else:
            return self.books
        
    def get_average_rating(self):
        if len(self.books)==0:
            return None
        else:
            average_user_rating_total=0
            for var_book in self.books:
                average_user_rating_total+=self.books[var_book]
                self.result=average_user_rating_total/len(self.books)
            return self.result
        
        
# Book Class
class Book():
    ratings=[]
    def __init__(self,title,isbn):
        self.title = str(title)
        self.isbn = int(isbn)
        self.rating = []
    
    def __repr__(self):
        return "The book title is {title}, it ISBN : {isbn}".format(title=self.title,isbn=self.isbn )
        
    def __hash__(self):
        return hash((self.title, self.isbn))
    
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True
        else:
            return False
    
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self,updated_isbn):
        self.updated_isbn = updated_isbn
        self.isbn = self.updated_isbn
        return "The book {title} ISBN has been updated to {updated_isbn}".format(title=self.title,updated_isbn=self.updated_isbn)
        
    def add_rating(self,rating):
        self.rating = int(rating)
        self.rating_range_check = self.rating
        if self.rating_range_check < 0 or self.rating_range_check > 4:
            return str("Invalid Rating")
        else:
            self.ratings.append(self.rating)
            return self.ratings
    
    def get_average_rating(self):
            average_book_rating_total=0
            for var_book_rating in self.ratings:
                average_book_rating_total+=var_book_rating
            average_rating=average_book_rating_total/len(self.ratings)
            return average_rating

        
        
# Fiction Class inherited from Book Class
class Fiction(Book):
    def __init__(self,title,author,isbn):
        super().__init__(title,isbn)
        self.author = author
    
    def __repr__(self):
        return "{title} by {author}".format(title=self.title, author=self.author)
        
    def get_author(self):
        return self.author

# Non_Fiction Class inherited from Book Class
class Non_Fiction(Book):
    def __init__(self,title,subject,level,isbn):
        super().__init__(title, isbn)
        self.subject = str(subject).title()
        self.level = str(level).lower()
    
    def __repr__(self):
        return "{title}, a {level} manual on {subject}".format(title=self.title,level=self.level,subject=self.subject)
    
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level



# TomeRater Class
class TomeRater():
    def __init__(self):
        self.users={}
        self.books={}
    
    def create_book(self,title,isbn):
        return Book(title, isbn)
        
    def create_novel(self,title,author,isbn):
        return Fiction(title,author,isbn)
    
    def create_non_fiction(self,title,subject,level,isbn):
        return Non_Fiction(title,subject,level,isbn)

    def add_book_to_user(self,book, email,rating=None):
        pass
        
        
    def add_user(self,name,email,books=None):
        pass
        
    
    def print_catalog(self):
        print(self.books.keys())
    
    def print_users(self):
        print(self.users.values())
    
    def most_read_book(self):
        print(max(self.books.values()))
    
    def highest_rated_book(self):
        pass
    
    def most_positive_user(self):
        pass
    
    def get_n_most_read_books(self):
        pass
    
    def get_n_most_prolific_readers(self):
        pass
    
    def get_n_most_expensive_books(self, n):
        pass
    
    def get_worth_of_user(self, user_email):
        pass
    
    
    
    

# Objects 
user_1=User("Emad Alhaj-Salem" , "ealhajsalem@com.sa" )
user_2=User("Emad Alhaj-Salem","ealhajsalem@com.sa" )
user_3=User("Stephen Hawking","hawking@universe.edu" )

book_1=Book("Desert Solitaire" , "2020202020"  )
book_2=Book("Desert Solitaire" , "2020202020"  )
book_3=Book("Testing Book3" , "333333333"  )
book_4=Book("Testing Book4" , "444444444"  )
book_5=Book("Testing Book5" , "555555555"  )
book_6=Book("Testing Book6" , "666666666"  )

Fiction_book_1=Fiction("Alice In Wonderland"  , "Lewis Carroll" , 1515151515)

Non_Fiction_book_1=Non_Fiction("Society of Mind" , "Artificial Intelligence" ,  "beginner" ,1212121212 )


tome_rate_01=TomeRater()
print(tome_rate_01.create_book("Test01", "101010"))
print(tome_rate_01.create_novel("Test02",  "me" ,505050))
print(tome_rate_01.create_non_fiction("Test03", "Python", "Level1", 6666666))


################
# Testing area #
################
# print(repr(user_1))
# print(repr(user_2))
# print(repr(user_3))
# ###################
# print(repr(book_1))
# print(type(book_1.title))
# print(type(book_1.isbn))
# print(repr(Fiction_book_1))
# print(repr(Non_Fiction_book_1))
# ###################
# print(book_1.get_title())
# print(book_1.get_isbn())
# print(book_1.set_isbn(50505050))
# print(book_1.get_isbn())
# print(book_1.add_rating(4))
# print(book_1.__eq__(book_2))
# ###################  
# print(Fiction_book_1.title)
# print(Fiction_book_1.get_author())
# print(Fiction_book_1.get_isbn())
# ###################
# print(Non_Fiction_book_1.title)
# print(Non_Fiction_book_1.isbn)
# print(Non_Fiction_book_1.subject)
# print(Non_Fiction_book_1.level)
# print(Non_Fiction_book_1.get_subject())
# print(Non_Fiction_book_1.get_level())
# print(Non_Fiction_book_1.__repr__())
# ####################
# print(str(book_1.title) +" " + str(book_1.isbn))
# print(user_1.read_book(book_1,1))
# print(user_1.read_book(book_1))
# print(user_1.read_book(book_3,4))
# print(user_1.read_book(book_4,4))
# print(user_1.read_book(book_5,0))
# print(user_2.read_book(book_2,166))
# print(user_2.read_book(book_3))
# print(user_2.read_book(book_4,1))
# print(user_1.get_average_rating())
# print(user_2.get_average_rating())
# print(book_1.add_rating(6))
# print(book_1.add_rating(-1))
# print(book_1.add_rating(4))
# print(book_1.add_rating(3))
# print(book_1.add_rating(1))
# print(book_1.add_rating(0))
# print(book_1.ratings)
# print(book_1.get_average_rating())








