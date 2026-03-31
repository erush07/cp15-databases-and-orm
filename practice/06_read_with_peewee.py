from helper_functions import clear_screen
clear_screen()

# =======================================================
# READING WITH PEEWEE - GETTING STUFF OUT OF THE DATABASE
# =======================================================

'''
OVERVIEW
--------
In CRUD, R stands for reading, meaning reading (or getting) data that already
exists out of your database.


'''


# Setup provided for you:
from peewee import *

db = SqliteDatabase('customers.db')

class Customer(Model):
    id_customer = AutoField(primary_key=True)
    name = CharField()
    email = CharField()
    birth_year = IntegerField()
    state = CharField()

    class Meta:
        database = db
    
    def get_info(self):
        return f"Customer {self.id_customer}'s data: Name: {self.name} | Email: {self.email} | Birth Year: {self.birth_year} | State: {self.state}"
    
db.connect()
db.create_tables([Customer])

customers = [
    {"name": "Alice", "email": "alice@example.com", "birth_year": 1990, "state": "CA"},
    {"name": "Bob", "email": "bob@example.com", "birth_year": 1985, "state": "NY"},
    {"name": "Charlie", "email": "charlie@example.com", "birth_year": 1978, "state": "TX"},
    {"name": "Diana", "email": "diana@example.com", "birth_year": 1992, "state": "FL"},
    {"name": "Ethan", "email": "ethan@example.com", "birth_year": 1980, "state": "WA"},
    {"name": "Fiona", "email": "fiona@example.com", "birth_year": 1995, "state": "OR"},
    {"name": "George", "email": "george@example.com", "birth_year": 1988, "state": "NV"},
    {"name": "Hannah", "email": "hannah@example.com", "birth_year": 1991, "state": "PA"},
    {"name": "Ian", "email": "ian@example.com", "birth_year": 1983, "state": "IL"},
    {"name": "Jane", "email": "jane@example.com", "birth_year": 1975, "state": "AZ"},
]

# 1. SET UP DATA
# To save time, delete your sqlite db file, and run this file. This will
# automatically create some customers for you the first time you run your code.

if Customer.select().count() == 0:
    Customer.insert_many(customers).execute()

# 2. GET ALL ROWS FROM THE DATABASE
# Use Customer.select() to get all the customers in your database. Then loop
# through them and print out their name and birth year

# .select gets you every row from a table
all_customers = Customer.select()

for cust_obj in all_customers:
    #print(f"{cust_obj.name}: {cust_obj.email}")
    print(cust_obj.get_info())


# 3. EXTEND YOUR CUSTOMER CLASS
# In your customer class, write a method called `get_info` that returns a
# string like this:
# Customer 1's data: Name: John | Email: example@gmail.com | Birth Year: 2000 | State: Utah
# then call that method on each of the customers in your table.


# 4. GET A SUBSET OF THE DATA
# Using .where() after .select() Get only those customers born after 1990
clear_screen()

subset_customers = Customer.select().where(Customer.birth_year > 1990)

for cust_obj in subset_customers:
    print(cust_obj.get_info())

# 5. ORDER THE RESULTS
# Use .order_by(table.column_name) to order the results in a specific way
# You can add .desc() to a column name if you want it in reverse order.
# Try getting the same results as #4, but order the results by birth year
# in descending order.

clear_screen()

subset_customers = Customer.select().where(Customer.birth_year > 1990).order_by(Customer.birth_year.desc())

for cust_obj in subset_customers:
    print(cust_obj.get_info())


# 6. GET A SUBSET OF THE DATA WITH MULTIPLE CONDITIONS
# Using .where() after .select() Get only those customers born after 1990 and
# from Pennsylvania (PA). In peewee, you need to put each condition in
# parentheses, with `&` instead of `and`. (| is used instead of or. ~ is used
# instead of not).

clear_screen()

subset_customers = Customer.select().where((Customer.birth_year > 1990) & (Customer.state == "PA")) # not working don't know why
for cust_obj in subset_customers:
    print(cust_obj.get_info())

# 7. GET A SINGLE RECORD USING .get
# .get() limits the result to a single row.
# Best used with ids (primary keys). Get customer with the id of 3 and print
# out their name
clear_screen()
single_customer = Customer.get(Customer.id_customer == 3)
print(single_customer.get_info())

# .first()
oldest_customer = Customer.select().order_by(Customer.birth_year.asc()).first()

'''
Other methods:

.get
.get_or_none
.raw
'''