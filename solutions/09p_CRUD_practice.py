from helper_functions import clear_screen
clear_screen()

# =========================
# CRUD PRACTICE WITH PEEWEE
# =========================

# 1. Create a dog database
'''
Create a database for dogs using peewee

The dog table should include:
    id
    name
    age
    favorite food (make it so this field is optional by adding null=True)

Using peewee
    1. create a few dogs
    2. print out some of their info,
    2. update a specific dog's favorite food
    3. delete a dog
'''

from peewee import *

# Create a SQLite database
db = SqliteDatabase('dogs.db')

# Define the Dog model
class Dog(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    age = IntegerField()
    favorite_food = CharField(null=True)  # Optional field

    class Meta:
        database = db

# Connect to the database and create the table
db.connect()
db.create_tables([Dog])

# 1. Create a few dogs
dog1 = Dog.create(name='Buddy', age=3, favorite_food='Chicken')
dog2 = Dog.create(name='Luna', age=5)  # No favorite food
dog3 = Dog.create(name='Max', age=2, favorite_food='Beef')

# 2. Print out some info
print("\nAll dogs in the database:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

# 3. Update a specific dog's favorite food
dog_to_update = Dog.get(Dog.name == 'Luna')
dog_to_update.favorite_food = 'Salmon'
dog_to_update.save()

print("\nAfter updating Luna's favorite food:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

# 4. Delete a dog
dog_to_delete = Dog.get(Dog.name == 'Max')
dog_to_delete.delete_instance()

print("\nAfter deleting Max:")
for dog in Dog.select():
    print(f"{dog.id}. {dog.name} - {dog.age} years old - Favorite food: {dog.favorite_food}")

# Close the database
db.close()