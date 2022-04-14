from flask import Flask,redirect,url_for,request,abort
app = Flask(__name__)
@app.route('/hello/<name>')
def hello_world():
    return 'Hello'

@app.route('/post/<postid>')
def hello_post(postid):
    return postid

#app.add_url_rule('/hello',view_func=hello_world)

@app.route('/admin')
def hello_admin():
    return 'Hello admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as Guest' %guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user = request.form['nm']
        if request.form['nm']=='admin':
            return redirect(url_for('success',name=user))
        
    else:
       abort(404)

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' %name
    
@app.route('/userData')
def userData():
    user=request.args.get('nm')
    return redirect(url_for('success',name=user))
    
    

if __name__ == '__main__':
    app.run(debug=True)

