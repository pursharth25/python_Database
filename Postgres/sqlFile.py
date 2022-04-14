import psycopg2

def create():
    conn=psycopg2.connect("dbname='python_test' user='pursharth' password='Puru2507@' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users(id SERIAL PRIMARY KEY,first_name TEXT,last_name TEXT, age INTEGER)")
    conn.commit()
    conn.close()


create()

def insert(first_name,last_name,age):
    conn=psycopg2.connect("dbname='python_test' user='pursharth' password='Puru2507@' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("INSERT INTO users(first_name,last_name,age) VALUES(%s,%s,%s)",(first_name,last_name,age))
    conn.commit()
    conn.close()


def view():
    conn=psycopg2.connect("dbname='python_test' user='pursharth' password='Puru2507@' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('select * from users')
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=psycopg2.connect("dbname='python_test' user='pursharth' password='Puru2507@' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute('delete from users where id=%s',(id,))
    conn.commit()
    conn.close()


delete(1)
print(view())
