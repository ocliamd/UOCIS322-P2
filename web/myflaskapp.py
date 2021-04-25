from flask import Flask
app = Flask(__name__)

@app.route('/')
def display():
    return "Looks like it works!"

@app.route('/alpha')
def alpha():
    return "This is the alpha version"

@app.route('/beta')
def beta():
    return "This is the beta version"


if __name__=='__main__':
    app.run()
