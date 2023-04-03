from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def index():
    return 'Thanks 404 for all the Help'
 
if __name__ == '__main__':
    app.run(debug=True)