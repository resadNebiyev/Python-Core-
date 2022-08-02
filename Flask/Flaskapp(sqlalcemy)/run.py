
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
class Customers(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    name = db.Column(db.String(100))
    mess = db.Column(db.String(200))

class Extra(db.Model):
    id = db.Column(db.Integer,primary_key=True,)
    e_name = db.Column(db.String(100))
    e_mess = db.Column(db.String(200))
@app.route('/')
def home():
    name = request.args.get('u_name')
    mess = request.args.get('u_message')
    # mymail = request.args.get('mymail')
    customer = Customers(name=name,mess=mess)
    db.session.add(customer)
    db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)