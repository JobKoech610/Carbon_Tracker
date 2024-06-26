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
        }

class Class(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    green_carbon = db.Column(db.String)
    carbon_emmision = db.Column(db.String)
    blue_carbon = db.Column(db.String)
    def to_dict(self):
        return {
            'id': self.id,
            'green_carbon': self.green_carbon,
            'carbon_emmision': self.carbon_emmision,
            'blue_carbon': self.blue_carbon,
            
        }

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
    
    def to_dict(self):
        return {
            'id': self.id,
            'ammount': self.ammount,
            'to_us': self.to_us,
            'company_id': self.company_id,
        }   

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String)
    phoneNumber = db.Column(db.Integer)
    email = db.Column(db.String)
    password = db.Column(db.Integer)
    company_id =db.Column(db.Integer, db.ForeignKey("company.id"))    
    resouces = db.relationship("Resource", backref="user")
    channel= db.relationship("Channel", backref="user")
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phoneNumber': self.phoneNumber,
            'email': self.email,
            'password': self.password,
        }

class Resource(db.Model):
    id = db.Column(db.Integer, primary_key = True)    
    articles = db.Column(db.String)
    events = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    chan = db.relationship("Channel", secondary=resouces_channel, backref="channels")
    def to_dict(self):
        return {
            'id': self.id,
            'articles': self.articles,
            'events': self.events,
        }
      

# class Resources_channel(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     channel_id = db.Column(db.Integer)
#     resouces_id = db.Column(db.Integer)

class Channel(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    partners  = db.Column(db.String)
    soultions = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    def to_dict(self):
        return {
            'id': self.id,
            'partners': self.partners,
            'solutions': self.soultions,
        }
    
class Home_calculator(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    Electricty = db.Column(db.String)
    Cooking_gas = db.Column(db.String)
    Diesel = db.Column(db.String)
    Coal = db.Column(db.String)
    Biomass = db.Column(db.String)
    Total = db.Column(db.Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'Electricty': self.Electricty,
            'Cooking_gas': self.Cooking_gas,
            'Diesel': self.Diesel,
            'Coal': self.Coal,
            'Biomass': self.Biomass,
            'Total': self.Total,
        }


class Factory_calculator(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    type  = db.Column(db.String)
    Electricty = db.Column(db.Integer)
    vehicles = db.Column(db.Integer)
    Distance = db.Column(db.Integer)
    Diesel = db.Column(db.Integer)
    Natural_gas = db.Column(db.Integer)
    Total = db.Column(db.Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type ,
            'Electricty': self.Electricty,
            'vehicles': self.vehicles,
            'Distance': self.Distance,
            'Diesel': self.Diesel,
            'Natural_gas': self.Natural_gas,
            'Total': self.Total,
        }
