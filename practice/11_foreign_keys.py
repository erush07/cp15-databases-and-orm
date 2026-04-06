from helper_functions import clear_screen
clear_screen()

# ==============================
# USING FOREIGN KEYS WITH PEEWEE
# ==============================

'''
OVERVIEW
--------
In a database, foreign keys are IDs that refer to the primary key of another
table. For example, if a Customer has a primary key of customer_id, that 
customer_id might also appear in an order table so that we can associate
specific orders with a specific customer.

Peewee makes working with foreign keys pretty convenient.

Structure:
field_name = ForeignKeyField(Customer, backref='appointments', on_delete='CASCADE')

'''

# 1. CREATE CLASSES FOR books.db
# Using the existing books.db database, create classes for Author and Book
# When you create your SqliteDatabase connection, add pragmas for foreign key
# db = SqliteDatabase('books.db', pragmas={'foreign_keys': 1})

from peewee import *

db = SqliteDatabase("books.db", pragmas={'foreign_keys': 1})

class Author(Model):
    author_id = AutoField(primary_key = True)
    name = CharField()
    birth_year = IntegerField()

    class Meta:
        database = db

class Book(Model):
    book_id = AutoField(primary_key = True)
    title = CharField()
    pages = IntegerField()
    year_published = IntegerField()
    author_id = ForeignKeyField(Author, backref = "books", on_delete = "CASCADE")

    class Meta:
        database = db

db.connect()
db.create_tables([Author, Book])

all_books = Book.select()

for book_obj in all_books:
    print(book_obj.title, book_obj.author_id.name, book_obj.author_id.birth_year)




# 2. READ FROM THE DATABASE
# Print out the titles of all the books.



'''
Foreign Key Field Structure
---------------------------
field_name = ForeignKeyField(Customer, backref='appointments', on_delete='CASCADE')
'''

clear_screen()

author_id_input = int(input("Enter and author id number: "))

author_obj = Author.get(Author.author_id == author_id_input)

print(f"{author_obj.name} has published the following books:")
for book_obj in author_obj.books:
    print(f"\t{book_obj.title}")


# 3. ADDING A FOREIGNKEYFIELD
# In the Book class, make author_id a ForeignKeyField
# Now print out the books, and their author's name


# 4. ACCESSING THROUGH BACK REFERENCE
# Ask the user for an Author's ID. Get that author, print out their data, and
# then print out the title of every book they've written.