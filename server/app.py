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
    
# Chat CRUD Endpoints
@app.route('/chats', methods=['GET', 'POST'])
def chats():
    if request.method == 'GET':
        chats = []
        for chat in Chat.query.all():
            chat_dict = chat.to_dict()
            chats.append(chat_dict)
        response = make_response(
            jsonify(chats),
            200
        )
        return response
    elif request.method == 'POST':
        new_chat = Chat(
            user_id = request.form.get("user_id"),
            message = request.form.get("message"),
            time = request.form.get("time"),
            chat_id = request.form.get("chat_id"),
            channel_id = request.form.get("channel_id"),
        )
        db.session.add(new_chat)
        db.session.commit()
        chat_dict = new_chat.to_dict()

        response = make_response(
            jsonify(chat_dict),
            201
        )
        return response

@app.route("/chats/<int:id>", methods=["GET", "PATCH", "DELETE"])
def single_chat(id):
    chat = Chat.query.get(id)
    if request.method == "GET":
        chat_dict = chat.to_dict()
        response = make_response(
            jsonify(chat_dict),
            200
        )
        return response
    elif request.method == "PATCH":
        chat.user_id = request.form.get("user_id")
        chat.message = request.form.get("message")
        chat.time = request.form.get("time")
        chat.chat_id = request.form.get("chat_id")
        chat.channel_id = request.form.get("channel_id")
        db.session.commit()
        chat_dict = chat.to_dict()
        response = make_response(
            jsonify(chat_dict),
            200
        )
        return response
    elif request.method == "DELETE":
        db.session.delete(chat)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "chat deleted."
        }
        response = make_response(
            jsonify(response_body),
            200
        )
        return response
    

# Payment CRUD Endpoints

@app.route('/payments', methods=['GET', 'POST'])
def payments():
    if request.method == 'GET':
        payments = []
        for payment in Payment.query.all():
            payment_dict = payment.to_dict()
            payments.append(payment_dict)
        response = make_response(
            jsonify(payments),
            200
        )
        return response
    elif request.method == 'POST':
        new_payment = Payment(
            user_id = request.form.get("user_id"),
            amount = request.form.get("amount"),
            currency = request.form.get("currency"),
            payment_id = request.form.get("payment_id"),
            wallet_id = request.form.get("wallet_id"),
            payment_type = request.form.get("payment_type"),
            time = request.form.get("time"),
            status = request.form.get("status"),
        )
        db.session.add(new_payment)
        db.session.commit()
        payment_dict = new_payment.to_dict()

        response = make_response(
            jsonify(payment_dict),
            201
        )
        return response
        
@app.route('/payments/<int:id>', methods=['GET','PATCH','DELETE'])
def payment_by_id(id):
    payment =  Payment.query.filter_by(id=id).first() 
    if request.method == "DELETE":
        db.session.delete(payment)
        db.session.commit()
        response_body = {
            "delete_successful": True,
            "message": "payment deleted."
        }
        response = make_response(
            jsonify(response_body),
            200
        )
        return response
    elif request.method == 'PATCH':
        payment.user_id = request.form.get("user_id")
        payment.amount = request.form.get("amount")
        payment.currency = request.form.get("currency")
        payment.payment_id = request.form.get("payment_id")
        payment.wallet_id = request.form.get("wallet_id")
        payment.payment_type = request.form.get("payment_type")
        payment.time = request.form.get("time")
        payment.status = request.form.get("status")
        db.session.commit()
        payment_dict = payment.to_dict()
        response = make_response(
            jsonify(payment_dict),
            200
        )
        return response
    else: # GET method
        payment_dict = payment.to_dict()
        response = make_response(
            jsonify(payment_dict),
            200
        )
        return response
        
# Error handlers
@app.errorhandler(404)
def not_found_error(e):
    return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
    

        

    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)