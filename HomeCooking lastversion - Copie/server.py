from flask import Flask,render_template, request ,redirect, url_for,session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, HiddenField
from flask_wtf.file import FileField , FileAllowed


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///stock.db'
app.config['DEBUG'] = True

db = SQLAlchemy(app)

#  ************les tables ************

class Meals(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categorie=db.Column(db.String(100))
    nom = db.Column(db.String(100), unique=True)
    prix = db.Column(db.Integer) 
    stock = db.Column(db.Integer)
    description = db.Column(db.String(500))
    image = db.Column(db.String(100))

# ************Clients************
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return  render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/basket")
def basket():
    return render_template("basket.html")
@app.route("/meals")
def meals():
    return render_template("meals.html")
@app.route("/login_client")
def login_client():
    return render_template("login_client.html")

# ************Admin************
@app.route("/admin")
def admin():
    return render_template("admin/admin.html")

@app.route("/admin/orders")
def orders():
    return render_template("admin/orders.html")

@app.route("/admin/message")
def message():
    return render_template("/admin/message.html")
@app.route("/admin/addmeals")
def addmeals():
    return render_template("/admin/addmeals.html")
@app.route("/login_admin")
def login_admin():
    return render_template("login_admin.html")


if __name__=="__main__":
    app.run(debug=True)