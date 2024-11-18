import sqlite3

try:
    conn = sqlite3.connect('example.db')
    c = conn.cursor()

    c.execute('''CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, date_of_birth DATETIME)''')
    c.execute('''CREATE TABLE Profiles (user_id INTEGER PRIMARY KEY, bio TEXT, profile_picture TEXT, joined_date DATETIME DEFAULT CURRENT_DATE, FOREIGN KEY(user_id) REFERENCES Users(id))''')

except:
    conn = sqlite3.connect('example.db')
    c = conn.cursor()


c.execute("INSERT INTO Users (name, email) VALUES ('Alice', 'alice@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Greg', 'greg@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Danny', 'danny@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Julia', 'julia@email.com')")
c.execute("INSERT INTO Profiles (user_id, bio) VALUES (1, 'Hello taxes, I am Alice')")
c.execute("INSERT INTO Profiles (user_id, bio) VALUES (2, 'Hello, I am Greg')")
c.execute("INSERT INTO Profiles (user_id, bio) VALUES (3, 'Hello taxes, I am Danny')")
c.execute("INSERT INTO Profiles (user_id, bio) VALUES (4, 'Hello, I am Julia')")

conn.commit()

c.execute("SELECT Users.name, Users.email, Profiles.bio, Profiles.profile_picture FROM Users JOIN Profiles ON Users.id = Profiles.user_id")
print("All users and their profiles:")
for row in c.fetchall():
    print(row)

c.execute("SELECT Users.name FROM Users JOIN Profiles ON Users.id = Profiles.user_id WHERE strftime('%Y', Profiles.joined_date) == strftime('%Y', CURRENT_DATE)")
print("All users who joined in the current year:")
for row in c.fetchall():
    print(row)

c.execute("SELECT Users.name FROM Users JOIN Profiles ON Users.id = Profiles.user_id WHERE Profiles.bio LIKE '%taxes%'")
print("All users with the keyword (taxes) in:")
for row in c.fetchall():
    print(row)

conn.close()