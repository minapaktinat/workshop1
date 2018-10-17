from flask import Flask
app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
    return '<h1>Hello, World!</h1>'

@app.route('/contact', methods=["GET"])
def salam():
    return 'Contact us at mina@gmail.com!'

@app.route('/address', methods=["GET"])
def address():
    return 'Floor 3, No 16 , sixteen ave , Mosala street'

if __name__=="__main__":
    app.run()