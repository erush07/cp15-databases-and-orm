from helper_functions import clear_screen
clear_screen()

# ================
# SQLITE IN PYTHON
# ================

# 1. Import the books.db datbase by importing the sqlite3 library and using the
# .connect function. Then use .execute() to get the data from it. Loop through
# the result and print out each row.

import sqlite3

conn = sqlite3.connect("books.db")

result = conn.execute("select * from author")

for row in result:
    print(row)