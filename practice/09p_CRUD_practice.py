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

db = SqliteDatabase("dogs.db")

class Dog(Model):
    dog_id = AutoField(primary_key = True)
    name = CharField()
    age = IntegerField()
    fav_food = CharField(null = True)

    class Meta:
        database = db

db.connect()
db.create_tables([Dog])

# dog_1 = Dog.create(name = "Benny", age = 3, fav_food = "Scooby Snacks")
# dog_2 = Dog.create(name = "Lewi", age = 12, fav_food = "Tuna")
# dog_3 = Dog.create(name = "Todd", age = 5, fav_food = "Peanut Butter")

all_dogs = Dog.select()
for dog_obj in all_dogs:
    print(f"{dog_obj.name} is {dog_obj.age} years old")

youngest_dog_obj = Dog.select().order_by(Dog.age).first()

print(youngest_dog_obj.name, youngest_dog_obj.fav_food)


youngest_dog_obj.fav_food = "Spaghettios"
youngest_dog_obj.save()

#delete
try:
    first_dog = Dog.get(Dog.dog_id == 1)
    first_dog.delete_instance()
except:
    print("couldn't find this dog")