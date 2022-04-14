
from crypt import methods
from flask import Flask,redirect,url_for,request,abort,render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/savedetails',methods=['POST'])
def saveDetails():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        con =  sqlite3.connect('employee.db') 
        cur = con.cursor()
        cur.execute('INSERT INTO Employees values (NULL,?,?,?)',(name,email,address))
        con.commit()
        msg = 'Data added successfully'
        con.close()
        return render_template('success.html',msg=msg)


@app.route('/view')
def view():
     con =  sqlite3.connect('employee.db') 
     cur = con.cursor()
     cur.execute('select * from Employees')
     rows = cur.fetchall()
     print(rows)
     con.close()
     return render_template('view.html',rows=rows)


@app.route('/delete/<int:id>')
def delete(id):
    con =  sqlite3.connect('employee.db') 
    cur = con.cursor()
    cur.execute('DELETE FROM Employees where id=?',(id,))
    con.commit()
    con.close()
    return redirect(url_for('view'))



@app.route('/edit/<int:id>')
def edit(id):
     con =  sqlite3.connect('employee.db') 
     cur = con.cursor()
     cur.execute('select * from Employees where id=?',(id,))
     rows = cur.fetchall()
     print(rows)
     con.close()
     return render_template('edit.html',rows=rows)


@app.route('/updatedetails/<int:id>', methods=['POST'])
def update(id):
    msg = 'msg'
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        con = sqlite3.connect('employee.db') 
        cur = con.cursor()
        cur.execute(
                'UPDATE Employees set name=?, email=?, address=? where id=?', (name, email, address, id))
        con.commit()
        msg = 'DATA changed successfully'
            # con.close()
        return render_template('success.html', msg=msg)



@app.route('/deletehome')
def deletehome():
    return render_template('delete.html')
    


@app.route('/deletedetails', methods=['POST'])
def deleteDetails():
    msg = 'msg'
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        con = sqlite3.connect('employee.db') 
        cur = con.cursor()
        cur.execute(
                'DELETE FROM Employees where name=? AND email=? AND address=?', (name, email, address))
        con.commit()
        msg = 'User Deleted Successfully'
            # con.close()
        return render_template('success.html', msg=msg)
    


if __name__ == '__main__':
    app.run(debug=True)