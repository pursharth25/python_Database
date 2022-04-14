from crypt import methods
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def upload():
    return render_template('upload.html')

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        fileData = request.files['file']
        print(fileData)
        fileData.save(fileData.filename)
        return render_template('success.html',name=fileData.filename)

if __name__ == '__main__':
    app.run(host='127.0.0.1',port='5005',debug=True)
