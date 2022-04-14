import sqlite3
conn = sqlite3.connect('lite.db')    #connecting to db
cur = conn.cursor()       #creating a cursor
cur.execute("UPDATE customer SET gender='other'")
    #in getting data you dont commit, because we are just viewing 

conn.commit()

conn.close() 
