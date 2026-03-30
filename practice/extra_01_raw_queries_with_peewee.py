from helper_functions import clear_screen
clear_screen()

# =========================
# BASIC QUERIES WITH PEEWEE
# =========================

'''
OVERVIEW
--------
You can connect to SQLite databases using peewee, just like you can using the
python standard sqlite3 library. 

The point of this file is to show that this is still possible, but this isn't
the main point of using an ORM like peewee.
'''


# 1. CONNECT TO SQLITE AND RUN A QUERY
# Use peewee.SqliteDatabase() to connect to the books.db database. Then use the
# .execute_sql() method to get all the data from the `author` table. Print it
# all out.
