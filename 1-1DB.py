import sqlite3
import datetime



try:
    table = sqlite3.connect("example1-1.db")
    c = table.cursor()

    c.execute('''CREATE TABLE Users (id INTEGER PRIMARY KEY, name TEXT, email TEXT UNIQUE, dob DATETIME)''')
    c.execute('''CREATE TABLE Profiles (user_id INTEGER PRIMARY KEY, bio TEXT, profile_pic TEXT, date_joined TEXT DEFAULT CURRENT_DATE, FOREIGN KEY(user_id) REFERENCES Users(id))''')

except:
    table = sqlite3.connect("example.db")
    c = table.cursor()

c.execute("INSERT INTO Users (name, email) VALUES ('Alice' , 'Alice@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Martin' , 'Martin@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Jonathan' , 'Johnny@email.com')")
c.execute("INSERT INTO Users (name, email) VALUES ('Jennifer' , 'Jenny@email.com')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_pic) VALUES (1, 'Hello, I am Alice', 'https://www.alamy.com/stock-photo-portrait-of-a-young-woman-79768994.html')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_pic) VALUES (2, 'Hello, I am Martin', 'https://stock.adobe.com/uk/search/images?k=mens&asset_id=224869519')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_pic) VALUES (3, 'Hello, I am Johnny, I HATE taxes', 'https://www.pexels.com/search/man/')")
c.execute("INSERT INTO Profiles (user_id, bio, profile_pic) VALUES (4, 'Hello, I am Taxes', 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pixsy.com%2Fphotography%2Fwhere-do-all-those-wtf-stock-photos-come-from&psig=AOvVaw0XBIwD5kzuw1eS1D_-1axW&ust=1730802652142000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJjViby8wokDFQAAAAAdAAAAABA6')")

c.execute('''SELECT Users.name, Users.email, Profiles.bio, Profiles.profile_pic FROM Users JOIN Profiles ON Users.id = Profiles.user_id''')
print("Here are the rows in Users , Profiles:")
for row in c.fetchall():
    print(row)

c.execute('''SELECT Users.name, Profiles.date_joined FROM Users JOIN Profiles ON Users.id = Profiles.user_id WHERE strftime("%Y", Profiles.date_joined) == strftime("%Y", CURRENT_DATE)''')
print("Here are the rows of user who joined in 2024:")
for row in c.fetchall():
    print(row)

c.execute('''SELECT Users.name, Profiles.bio FROM Users JOIN Profiles ON Users.id = Profiles.user_id WHERE Profiles.bio LIKE "%taxes%"''')
print("Here are the rows of user who joined in 2024:")
for row in c.fetchall():
    print(row)

table.commit()
table.close()
