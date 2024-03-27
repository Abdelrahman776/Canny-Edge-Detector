from flask import Flask

app=Flask(__name__)

@app.route('/')
def upload():
    return 'Upload'



@app.route('/result')
def result():
    return '<h1>result<h1>'



if __name__ == '__main__':
    app.run(port=64604)