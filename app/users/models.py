from marshmallow_jsonapi import Schema, fields
from marshmallow import validate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

db = SQLAlchemy()


class CRUD():   

    def add(self, resource):
        db.session.add(resource)
        return db.session.commit()   

    def update(self):
        return db.session.commit()

    def delete(self, resource):
        db.session.delete(resource)
        return db.session.commit()

class tbl_users(db.Model, CRUD):
    id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String(250), nullable=False)
    email = db.Column(db.String(250), nullable=False)
    password = db.Column(db.String(35), nullable=False)
    firstname = db.Column(db.String(150), default=True)
    lastname = db.Column(db.String(150), nullable=False)
    birthdate = db.Column(db.DATE, nullable=False)
    registerdate = db.Column(db.TIMESTAMP, default=func.now(), nullable=False)
    isactive = db.Column(db.Boolean, default=False, nullable=False)
    def __init__(self, userid, email, password, firstname, lastname, birthdate):
        self.userid = userid
        self.email = email
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        # self.registerdate = registerdate
        # self.isactive = isactive


class user_schema(Schema):
    # not_blank = validate.Length(min=1, error='Field cannot be blank')
    id = fields.Integer(dump_only=True)
    userid = fields.String()    
    email = fields.String()
    password = fields.String()
    firstname = fields.String()
    lastname = fields.String()
    birthdate = fields.Date()       

    class Meta:
        type_ = 'users'
    
