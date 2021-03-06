# models.py
from project import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(64),unique=True,index=True)
    username = db.Column(db.String(64),unique=True,index=True)
    password_hash = db.Column(db.String(128))
    number = db.Column(db.String(64))
    posts = db.relationship('BlogPost',backref='author',lazy=True)

    def __init__(self,email,username,password):
        self.email = email
        self.username = username
        self.password_hash = generate_password_hash(password)

    def check_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return "Username {}".format(self.username)

class BlogPost(db.Model):
    
    users = db.relationship(User)
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
    number = db.Column(db.String(64))

    def __init__(self,number,user_id,username):
        self.user_id = user_id
        self.number = number
        self.username = username

    def __repr__(self):
        return "Post ID: {} Post Number: {} Username:{}".format(self.id,self.number,self.username)
 
