from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password@db/users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    age = db.Column(db.Integer)
    nationality = db.Column(db.String(50))

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    age = request.form['age']
    nationality = request.form['nationality']
    user = User(name, age, nationality)
    db.session.add(user)
    db.session.commit()
    return 'User registered successfully!'

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0')
