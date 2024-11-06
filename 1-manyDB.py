import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('example1-many.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE Authors (
                id INTEGER PRIMARY KEY,
                name TEXT
             )''')

c.execute('''CREATE TABLE Books (
                id INTEGER PRIMARY KEY,
                title TEXT,
                author_id INTEGER,
                FOREIGN KEY(author_id) REFERENCES Authors(id)
             )''')

# Insert data
c.execute("INSERT INTO Authors (name) VALUES ('George Orwell')")
c.execute("INSERT INTO Books (title, author_id) VALUES ('1984', 1)")
c.execute("INSERT INTO Books (title, author_id) VALUES ('Animal Farm', 1)")

c.execute("SELECT Books.title, Authors.name FROM Books JOIN Authors ON Books.author_id = Authors.id WHERE Authors.name = 'George Orwell'")
print("Books where the author is George Orwell:")
for row in c.fetchall():
    print(row)

c.execute("SELECT Books.title, Authors.name FROM Books JOIN Authors ON Books.author_id = Authors.id WHERE Books.title LIKE '%Farm%'")
print("Books with farm in the title:")
for row in c.fetchall():
    print(row)

c.execute("SELECT Authors.name, COUNT(Books.title) FROM Books JOIN Authors ON Books.author_id = Authors.id GROUP BY Books.author_id")
print("Authors and how many books they have written:")
for row in c.fetchall():
    print(row)

conn.commit()
conn.close()
# os.remove("example1-many.db")