from flask import Flask,render_template,request,redirect,url_for
app=Flask(__name__)

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method=='POST':
        name = request.form['nm1']
        physics = request.form['nm2']
        chemistry = request.form['nm3']
        maths = request.form['nm4']

        dict={'maths':maths,'chemistry':chemistry,'physics':physics,'name':name}
        return render_template('result.html',result=dict)

if __name__ =='__main__':
    app.run(host='127.0.0.1',port='5000',debug=True)