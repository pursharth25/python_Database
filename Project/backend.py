import sqlite3

def connect():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS book(id INTEGER PRIMARY KEY,title TEXT ,author TEXT, year INTEGER, price INTEGER)')
    conn.commit()
    conn.close()

def backendInsert(title,author,year,price):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('INSERT INTO book values(null,?,?,?,?)',(title,author,year,price))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('SELECT * from book')
    row=cur.fetchall()
    conn.close()
    return row

def search(title='',author='',year='',price=''):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('select * from book where title=? OR author=? OR year=? OR price=?',(title,author,year,price))
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('delete from book where id=?',(id,))
    conn.commit()
    conn.close()

def update(title,author,year,price,id):
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('update book set title=?,author=?,year=?,price=? where id=?',(title,author,year,price,id))
    conn.commit()
    conn.close()

def drop():
    conn=sqlite3.connect('books.db')
    cur=conn.cursor()
    cur.execute('DROP TABLE book')
    conn.commit()
    conn.close()



# connect()
# insert('book1','abc',10,100)
# insert('book2','pqr',11,101)
print(view())

