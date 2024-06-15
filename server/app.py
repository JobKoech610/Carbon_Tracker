#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
import jwt

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
    if company == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
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
        elif request.method == 'GET':
            company_dict = company.to_dict()

            response = make_response(
                jsonify(company_dict),
                200
            )

            return response
        elif request.method == 'PATCH':
            company = Company.query.filter_by(id=id).first()

            for attr in request.form:
                setattr(company, attr, request.form.get(attr))

            db.session.add(company)
            db.session.commit()

            company_dict = company.to_dict()

            response = make_response(
                jsonify(company_dict),
                200
            )

            return response



#class endpoint
@app.route('/classes', methods=['GET', 'POST', 'DELETE'])
def classes():
    if request.method == 'GET':
        classes = []
        for clas in Class.query.all():
            # company_dict = company.to_dict()
            class_dict = {
                "green_carbon": clas.green_carbon,
                "carbon_emmision": clas.carbon_emmision,
                "blue_carbon": clas.blue_carbon,
                
            }
            classes.append(class_dict)
        response = make_response(
            jsonify(classes),
            200
        )    
        return response
    elif request.method == 'POST':
        new_class = Class(
            green_carbon = request.form.get("green_carbon"),
            carbon_emmision = request.form.get("carbon_emmision"),
            blue_carbon = request.form.get("blue_carbon"),            
        )    
        db.session.add(new_class)
        db.session.commit()
        class_dict = new_class.to_dict()

        response = make_response(
            jsonify(class_dict),
            201
        )
        return response
@app.route('/classes/<int:id>', methods=['GET','PATCH','DELETE'])
def classes_by_id(id):
    clas =  Class.query.filter_by(id=id).first() 
    if clas == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else:
        if request.method == "DELETE":
            db.session.delete(clas)
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
        elif request.method == 'GET':
            clas_dict = clas.to_dict()
            response = make_response(
                jsonify(clas_dict),
                200
            )
            return response 
        elif request.method == 'PATCH':
            clas = Class.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(clas, attr, request.form.get(attr))
            db.session.add(clas)
            db.session.commit()
            clas_dict = clas.to_dict()
            response = make_response(
                jsonify(clas_dict),
                200
            )
            return response  
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
            return response

@app.route('/home-calc', methods=['GET', 'POST', 'DELETE'])
def classes():
    if request.method == 'GET':
        home = []
        for data in Home_calculator.query.all():
            home_dict = {
                "Electricty": data.Electricty,
                "Cooking_gas": data.Cooking_gas
                "Diesel": data.Diesel,
                "Coal": data.Coal,
                "Biomass": data.Biomass,
                "Total": data.Total                
            }
            home.append(home_dict)
        response = make_response(
            jsonify(home),
            200
        )
        return response
    elif request.method == 'POST':
        new_home = Home_calculator(
            Electricty = request.form.get("Electricty"),
            Cooking_gas = request.form.get("Cooking_gas"),
            Diesel = request.form.get("Diesel"),
            Coal = request.form.get("Coal"),
            Biomass = request.form.get("Biomass"),
            Total= request.form.get("Total"),          
        )    
        db.session.add(new_home)
        db.session.commit()
        home_dict = new_home.to_dict()

        response = make_response(
            jsonify(home_dict),
            201
        )
        return response

@app.route('/fact-calc', methods=['GET', 'POST', 'DELETE'])
def classes():
    if request.method == 'GET':
        factory = []
        for data in Factory_calculator.query.all():
            fact_dict = {
                "type": data.type,
                "Electricty": data.Electricty
                "vehicles": data.vehicles,
                "Distance": data.Distance,
                "Diesel": data.Diesel,
                "Natural_gas": data.Natural_gas,
                "Total": data.Total                
            }
            factory.append(fact_dict)
        response = make_response(
            jsonify(factory),
            200
        )
        return response
    elif request.method == 'POST':
        new_fact = Factory_calculator(
            type = request.form.get("type"),
            Electricty = request.form.get("Electricty"),
            vehicles = request.form.get("vehicles"),
            Distance = request.form.get("Distance"),
            Diesel = request.form.get("Diesel"),
            Natural_gas = request.form.get("Natural_gas"),
            Total= request.form.get("Total"),          
        )    
        db.session.add(new_fact)
        db.session.commit()
        fact_dict = new_fact.to_dict()

        response = make_response(
            jsonify(fact_dict),
            201
        )
        return response        
  



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)