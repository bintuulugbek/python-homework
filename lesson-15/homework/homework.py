# Review Exercises
# Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3
with sqlite3.connect('sqlite_1.db') as connection:
    cursor = connection.cursor()
    create_table = """create table Roster(
        Name TEXT ,
        Species TEXT,
        Age INTEGER
    )"""
    results = cursor.execute(create_table)

# Populate your new table with the following values:
iterables = [('Benjamin Sisko', 'Human', 40), ('Jadzia Dax', 'Trill', 300), ('Kira Nerys', 'Bajoran', 29)]

with sqlite3.connect('sqlite_1.db') as connection:
    conn = connection.cursor()
    results = conn.executemany("insert into Roster(Name, Species, Age) values (?, ?, ?)", iterables) 

# Update the Name of Jadzia Dax to be Ezri Dax
connection = sqlite3.connect('sqlite_1.db')
with sqlite3.connect('sqlite_1.db') as connection:
    conn = connection.cursor()
    conn.execute("""update Roster
                set name = 'Ezri Dax'
                where name = 'Jadzia Dax'""")
    
# Display the Name and Age of everyone in the table classified as Bajoran.
with sqlite3.connect('sqlite_1.db') as connection:
    conn = connection.cursor()
    results = conn.execute("select Name, Age from Roster where Species = 'Bajoran'")
    all = results.fetchall()
    print(all)
