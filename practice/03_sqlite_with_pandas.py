from helper_functions import clear_screen
clear_screen()

# ============================
# SQLITE WITH PANDAS
# ============================

import sqlite3
import pandas as pd


db = sqlite3.connect('books.db')

# 1. Given the above connection, get a dataframe of the whole book table

df = pd.read_sql("select * from book", db)
print(df)