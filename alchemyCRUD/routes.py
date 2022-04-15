
from flask import Flask, redirect,url_for,render_template,request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'   #students.sqlite3 is Database name

db = SQLAlchemy(app)    #will support everything, its inbuit module, just use db. before anything

class students(db.Model):    #students is table name
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    def __init__(self,name,city):
        self.name = name
        self.city = city


@app.route('/')
def show_all():
    return render_template('show.html',student=students.query.all())

@app.route('/createdb')       #this route creates new database with name provided on line 4 i.e students.sqlite3
def create():
    db.create_all()
    return redirect(url_for('show_all'))

@app.route('/new',methods=['POST','GET'])
def newStudent():
    if request.method=='POST':
        name = request.form['name']
        city = request.form['city']
        newstudent = students(name=name,city=city)
        db.session.add(newstudent)
        db.session.commit()
        return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/edit/<int:sid>', methods=['POST', 'GET'])
def edit_student(sid):
    if request.method =='POST':
        stud=students.query.get(sid)
        name=request.form['name']
        city=request.form['city']
        stud.name=name
        stud.city=city
        db.session.commit()
        return redirect(url_for('show_all'))
    return render_template('edit.html', s=students.query.filter_by(id=sid).first())

@app.route('/update/<int:id>', methods=['POST'])
def update_students(sid):
    name=db.session.query(students.name).filter_by(id=sid).first()
    city= db.session.query(students.city).filter_by(id=sid).first()

    return redirect(url_for('show_all'))

@app.route('/delete/<int:sid>')
def delete_student(sid):
    students.query.filter_by(id=sid).delete()
    db.session.commit()
    return redirect(url_for('show_all'))


if __name__ == '__main__':
    app.run(debug=True)