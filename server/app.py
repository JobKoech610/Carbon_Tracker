#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db, Company, Class, Wallet, Chat, Payment, User, Resource, Channel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# api = Api(app)

@app.route('/')
def index():
    return "carbon  emmision"

@app.route('/companies', methods=['GET', 'POST', 'DELETE'])
def companies():
    if request.method == 'GET':
        companies = []
        for company in Company.query.all():
            # company_dict = company.to_dict()
            company_dict = {
                "company_name": company.company_name,
                "class_type": company.class_type,
                "location": company.location,
                "size": company.size,
                "account": company.account,

            }
            companies.append(company_dict)
        response = make_response(
            jsonify(companies),
            200
        )    
        return response
    elif request.method == 'POST':
        new_company = Company(
            company_name = request.form.get("company_name"),
            class_type = request.form.get("class_type"),
            location = request.form.get("location"),
            size = request.form.get("size"),
            account = request.form.get("account"),
        )    
        db.session.add(new_company)
        db.session.commit()
        review_dict = new_company.to_dict()

        response = make_response(
            jsonify(review_dict),
            201
        )
        return response

@app.route('/companies/<int:id>', methods=['GET','PATCH','DELETE'])
def companies_by_id(id):
    company =  Company.query.filter_by(id=id).first() 
    if request.method == "DELETE":
        db.session.delete(company)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "company deleted."
        }
        response = make_response(
            jsonify(response_body),
            200
        )
        return response

# Wallet CRUD Endpoints
@app.route('/wallets', methods=['GET', 'POST'])
def wallets():
    if request.method == 'GET':
        wallets = []
        for wallet in Wallet.query.all():
            wallet_dict = wallet.to_dict()
            wallets.append(wallet_dict)
        response = make_response(
            jsonify(wallets),
            200
        )
        return response
    elif request.method == 'POST':
        new_wallet = Wallet(
            user_id = request.form.get("user_id"),
            balance = request.form.get("balance"),
            bonus = request.form.get("bonus"),
            carbon_credits= request.form.get("carbon_credits"),
            pricing= request.form.get("pricing"),
            currency=request.form.get("currency"),
            buy= request.form.get("buy"),
            deposit= request.form.get("deposit"),
            withdraw= request.form.get("withdraw"),
            transfer= request.form.get("transfer"),
            payment= request.form.get("payment"),
            account= request.form.get("account"),
            wallet_id= request.form.get("wallet_id"),
        )
        db.session.add(new_wallet)
        db.session.commit()
        wallet_dict = new_wallet.to_dict()

        response = make_response(
            jsonify(wallet_dict),
            201
        )
        return response
    
@app.route('/wallets/<int:id>', methods=['GET','PATCH','DELETE'])
def wallets_by_id(id):
    wallet =  Wallet.query.filter_by(id=id).first() 
    if request.method == "DELETE":
        db.session.delete(wallet)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "wallet deleted."
        }
        response = make_response(
            jsonify(response_body),
            200
        )
        return response
    elif request.method == 'PATCH':
        wallet.user_id = request.form.get("user_id")
        wallet.balance = request.form.get("balance")
        wallet.bonus = request.form.get("bonus")
        wallet.carbon_credits = request.form.get("carbon_credits")
        wallet.pricing = request.form.get("pricing")
        wallet.currency = request.form.get("currency")
        wallet.buy = request.form.get("buy")
        wallet.deposit = request.form.get("deposit")
        wallet.withdraw = request.form.get("withdraw")
        wallet.transfer = request.form.get("transfer")
        wallet.payment = request.form.get("payment")
        wallet.account = request.form.get("account")
        wallet.wallet_id = request.form.get("wallet_id")
        db.session.commit()
        wallet_dict = wallet.to_dict()
        response = make_response(
            jsonify(wallet_dict),
            200
        )
        return response
    

        

    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)