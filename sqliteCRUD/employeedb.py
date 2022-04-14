import sqlite3
con=sqlite3.connect('employee.db')
print('Database created')
cur=con.cursor()

con.execute('CREATE TABLE Employees(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT,email TEXT,address TEXT)')

con.commit()
con.close()