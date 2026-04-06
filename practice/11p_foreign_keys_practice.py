from helper_functions import clear_screen
clear_screen()

# ==============================
# PRACTICE - USING FOREIGN KEYS WITH PEEWEE
# ==============================

# 1. Adding a foreign key field
'''
Using the Customer class that you've already written previously,
add an Order Class. Orders should have
    - an id
    - item_name
    - quantity
    - a foreign key that corresponds to Customers

Try hardcoding some new orders in. After that, try getting user inputs
to get specific customers and create orders for them.
'''

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
    # create a class method, so you do cls as the first argument 
    # and you need to tell python that it is a special class method
    # by adding @classmethod above it
    # this changed the behavior of the method to let you run it without an object first
    @classmethod
    def create(cls, **query):
        email_value = query.get('email')
        if "@" in email_value:
            # validated, actually create it, so run the original version of .create
            return super().create(**query) # run the original one, return whatever it returns
        else:
            print("you need to provide a valid email. row not created.")

class Order(Model):
    id = AutoField()
    item_name = CharField()
    quantity = IntegerField()
    customer_id = ForeignKeyField(Customer, backref = "orders", on_delete = "CASCADE")
    
    class Meta:
        database = db

db.connect()
db.create_tables([Customer, Order])
