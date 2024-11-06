import sqlite3
import os

# Connect to the database
conn = sqlite3.connect('examplemany-many.db')
c = conn.cursor()

# Create tables
c.execute('''CREATE TABLE Employees (
                id INTEGER PRIMARY KEY,
                name TEXT
             )''')

c.execute('''CREATE TABLE Projects (
                id INTEGER PRIMARY KEY,
                title TEXT
             )''')

c.execute('''CREATE TABLE EmployeeProjects (
                employee_id INTEGER,
                project_id INTEGER,
                PRIMARY KEY (employee_id, project_id),
                FOREIGN KEY(employee_id) REFERENCES Employees(id),
                FOREIGN KEY(project_id) REFERENCES Projects(id)
             )''')

# Insert data
c.execute("INSERT INTO Employees (name) VALUES ('John Doe'), ('Jane Doe')")
c.execute("INSERT INTO Projects (title) VALUES ('Project Alpha'), ('Project Beta')")
c.execute("INSERT INTO EmployeeProjects (employee_id, project_id) VALUES (1, 1), (1,2), (2,2)")

c.execute("SELECT Projects.title, Employees.name  FROM Projects, Employees JOIN EmployeeProjects ON EmployeeProjects.project_id = Projects.id JOIN EmployeeProjects ON EmployeeProjects.employee_id = Employees.id WHERE Employees.id")
print("All projects an employee is assigned to:")
for row in c.fetchall():
    print(row)

conn.commit()
conn.close()
# os.remove("examplemany-many.db")