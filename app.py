from flask import Flask
from extension import db

app = Flask(__name__)
app.config['SQLALCHEMEY_DATABASE_URI'] = 'sqlite:///books.sqlite'
app.config['SQLALCHEMEY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello_world(): #put application's code here
    return "Hellow World"


if __name__ == '__main__':
    app.run(debug=True)