#!/usr/bin/env python3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
db =SQLAlchemy()



#association tables for many-to-many relationship
company_class = db.Table("company_class",
db.Column("company_id", db.Integer, db.ForeignKey("company.id")),
db.Column("class_id", db.Integer, db.ForeignKey("class.id"))

)

resouces_channel = db.Table("resouces_channel",
db.Column("resource_id", db.Integer, db.ForeignKey("resource.id")),
db.Column("channel_id", db.Integer, db.ForeignKey("channel.id"))
)



# class Company_class(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     company_id = db.Column(db.Integer)
#     class_id =  db.Column(db.Integer)


class Company(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    company_name = db.Column(db.String)
    class_type =db.Column(db.String)
    location = db.Column(db.String)
    size = db.Column(db.Integer)
    account = db.Column(db.String)
    wallet = db.relationship("Wallet", backref="company", uselist = False)
    chats = db.relationship("Chat", backref="company")
    payments = db.relationship("Payment", backref="company")
    users = db.relationship("User", backref="company")

    #many-to-many
    class_association = db.relationship("Class", secondary=company_class, backref="classes")
    def to_dict(self):
        return {
            'id': self.id,
            'company_name': self.company_name,
            'class_type': self.class_type,
            'location': self.location,
            'size': self.size,
            'account': self.account,
            # Add more attributes as needed
        }

class Class(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    green_carbon = db.Column(db.String)
    carbon_emmision = db.Column(db.String)
    blue_carbon = db.Column(db.String)

class Wallet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    bonus = db.Column(db.Integer)
    carbon_credits = db.Column(db.Integer)
    pricing = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    buy = db.Column(db.Integer)
    deposit = db.Column(db.Integer)
    transfer = db.Column(db.Integer)
    company_id =db.Column(db.Integer, db.ForeignKey("company.id")) 
    
def to_dict(self):
    return {
        'id': self.id,
        'balance': self.balance,
        'bonus': self.bonus,
        'carbon_credits': self.carbon_credits,
        'pricing': self.pricing,
        'currency': self.currency,
        'buy': self.buy,
        'deposit': self.deposit,
        'withdraw': self.withdraw,
        'transfer': self.transfer,
        
    }   

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    class_id = db.Column(db.Integer)
    company_id =db.Column(db.Integer, db.ForeignKey("company.id")) 
    
    def to_dict(self):
        return {
            'id': self.id,
            'class_id': self.class_id,
            'company_id': self.company_id,
        }  
        


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    ammount =  db.Column(db.Integer)
    to_us = db.Column(db.String)
    company_id =db.Column(db.Integer, db.ForeignKey("company.id"))    

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    phoneNumber = db.Column(db.Integer)
    email = db.Column(db.String)
    password = db.Column(db.Integer)
    companyName = db.Column(db.String)
    company_id =db.Column(db.Integer, db.ForeignKey("company.id"))    
    resouces = db.relationship("Resource", backref="user")

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key = True)    
    articles = db.Column(db.String)
    events = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    chan = db.relationship("Channel", secondary=resouces_channel, backref="channels")
      

# class Resources_channel(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     channel_id = db.Column(db.Integer)
#     resouces_id = db.Column(db.Integer)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    partners  = db.Column(db.String)
    resouces_id = db.Column(db.Integer)
    soultions = db.Column(db.String)
    user_id = db.Column(db.Integer)  
    


