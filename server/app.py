#!/usr/bin/env python3

from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, JWTManager
from sqlalchemy.exc import IntegrityError
from datetime import datetime, timedelta
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from models import db, Company, Class, Wallet, Chat, Payment, User, Resource, Channel, Home_calculator, Factory_calculator

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '{~T<B#c&Y@oP}"C}pc7ajYR},Etow+Sc'

migrate = Migrate(app, db)

db.init_app(app)
jwt= JWTManager(app)
CORS(app)
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
        
@app.route('/users', methods=['GET', 'POST', 'DELETE'])
def users():
    if request.method == 'GET':
        users=[]
        for user in User.query.all():
            user_dict = {
                "name": user.name,
                "phoneNumber": user.phoneNumber,
                "email": user.email,
                "password": user.password,
            }
            users.append(user_dict)
        response = make_response(
            jsonify(users), 200
        )
        return response
    elif request.method == 'POST':
        data = request.get_json()
        try:
            hashed_password = generate_password_hash(data.get('password'), method='pbkdf2:sha256', salt_length=16)
            new_user = User(
                name=data.get('name'),
                phoneNumber=data.get('phoneNumber'),
                email=data.get('email'),
                password=hashed_password,
            )
            db.session.add(new_user)
            db.session.commit()
            user_dict = new_user.to_dict()
            response = make_response(
                jsonify(user_dict), 201
            )
            return response
        except IntegrityError as e:
            db.session.rollback()
            if "duplicate key value violates unique constraint" in str(e.orig):
                return jsonify({"error": "Email already exists"}), 400
            return jsonify({"error": str(e.orig)}), 400
        except Exception as e:
            return jsonify({"error": str(e)}), 500


    
@app.route('/users/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def users_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user == None:
        response_body ={
            "message": "This user doesn't exist"
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else: 
        if response.method == "GET":
            user_dict = user.to_dict()
            response = make_response(
                jsonify(user.to_dict()), 200
            )
            return response
        elif request.method == 'PATCH':
            user = User.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(user, attr, request.form.get(attr))
            
            db.session.add(user)
            db.session.commit()

            user_dict = user.to_dict()
            response = make_response(
                jsonify(user_dict)
            )
            return response
        elif request.method == 'DELETE':
            db.session.delete(user)
            db.session.commit()
            response_body ={
                "delete_successful" :True,
                "message" : "User Deleted"
            }
            response = make_response(
                jsonify(response_body), 200
            )
            return response
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
            return response
        
@app.route('/resource', methods=['GET', 'POST', 'DELETE'])
def resources():
    if request.method == 'GET':
        resources = []
        for resource in Resource.query.all():
            # company_dict = company.to_dict()
            resource_dict = {
                "articles": resource.articles,
                "events": resource.events,
                
            }
            resources.append(resource_dict)
        response = make_response(
            jsonify(resources),
            200
        )    
        return response
    elif request.method == 'POST':
        new_resource = Resource(
            articles = request.form.get("articles"),
            events= request.form.get("events"),           
        )    
        db.session.add(new_resource)
        db.session.commit()
        resource_dict= new_resource.to_dict()

        response = make_response(
            jsonify(resource_dict),
            201
        )
        return response
@app.route('/resource/<int:id>', methods=['GET','PATCH','DELETE'])
def resource_by_id(id):
    resourc=  Resource.query.filter_by(id=id).first() 
    if resourc == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)
        return response
    else:
        if request.method == "DELETE":
            db.session.delete(resourc)
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
            resourc_dict = resourc.to_dict()
            response = make_response(
                jsonify(resourc_dict),
                200
            )
            return response 
        elif request.method == 'PATCH':
            resourc = Resource.query.filter_by(id=id).first()
            for attr in request.form:
                setattr(resourc, attr, request.form.get(attr))
            db.session.add(resourc)
            db.session.commit()
            resourc_dict = resourc.to_dict()
            response = make_response(
                jsonify(resourc_dict),
                200
            )
            return response  
        else:
            # Handle unsupported methods
            response_body = {
                "message": "Method not allowed for this endpoint."
            }
            response = make_response(jsonify(response_body), 405)
            return response\

@app.route('/channel', methods=['GET', 'POST', 'DELETE'])
def channel():
    if request.method == 'GET':
        channel= []
        for channel in Channel.query.all():
            channel_dict = {
                "partners": channel.partners,
                "resources_id": channel.resources_id,
                "solutions": channel.solutions,
                "user_id": channel.user_id,
            }
            channel.append(channel_dict)
        response = make_response(
            jsonify(channel),
            200
        )    
        return response
    elif request.method == 'POST':
        new_channel = Channel(
            partners = request.form.get("partners"),
            resources_id = request.form.get("resources_id"),
            solutions = request.form.get("solutions"),
            user_id= request.form.get("user_id"),
        )    
        db.session.add(new_channel)
        db.session.commit()
        channel_dict = new_channel.to_dict()

        response = make_response(
            jsonify(channel_dict),
            201
        )
        return response

@app.route('/channel/<int:id>', methods=['GET','PATCH','DELETE'])
def channel_by_id(id):
    channels =  Channel.query.filter_by(id=id).first() 
    if channels == None:
        response_body = {
            "message": "This record does not exist in our database. Please try again."
        }
        response = make_response(jsonify(response_body), 404)

        return response
    else:
        if request.method == "DELETE":
            db.session.delete(channels)
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
            channels_dict = channels.to_dict()

            response = make_response(
                jsonify(channels_dict),
                200
            )

            return response
        elif request.method == 'PATCH':
            channels = Channel.query.filter_by(id=id).first()

            for attr in request.form:
                setattr(channels, attr, request.form.get(attr))

            db.session.add(channels)
            db.session.commit()

            channels_dict = channels.to_dict()

            response = make_response(
                jsonify(channels_dict),
                200
            )

            return response
        

# Error handlers
@app.errorhandler(404)
def not_found_error(e):
    return make_response(jsonify({"error": "Not found"}), 404)


@app.route('/home-calc', methods=['GET', 'POST', 'DELETE'])
def homecalc():
    if request.method == 'GET':
        home = []
        for data in Home_calculator.query.all():
            home_dict = {
                "Electricty": data.Electricty,
                "Cooking_gas": data.Cooking_gas,
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
def factorycalc():
    if request.method == 'GET':
        factory = []
        for data in Factory_calculator.query.all():
            fact_dict = {
                "type": data.type,
                "Electricty": data.Electricty,
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

@app.route('/login', methods = ['POST'])
def login():
    auth = request.get_json()
    if not auth or not auth.get("email") or not auth.get("password"):
        return make_response({
            "message":"please ensure you have entered the correct details"
        }), 401

    user = User.query.filter_by(email=auth.get("email")).first()
    if not user:
        return make_response({
            "message":"User not found"
        }), 401

    if user and check_password_hash(user.password, auth.get("password")):
        expiration = timedelta(minutes = 30)
        metadata = {
            'id': user.id,
            'name': user.name,
            'phoneNumber': user.phoneNumber,
            'email': user.email,
            'password': user.password,
        }
        token = create_access_token(identity = user.id, additional_claims=metadata, expires_delta=expiration)
        # return make_response(jsonify({
        #     "token": token, "user_id":user.id, "metadata": metadata
        # })), 201
        return make_response(jsonify({
            "token": token,
            "user_id": user.id,
            "name": user.name,
            "email": user.email,
            "metadata": metadata,
        })), 201
    return make_response({
        "message": "Invalid email or password"
    }), 401

@app.route('/signup', methods = ['POST'])
def signup():
    data = request.get_json()

    name = data.get('name')
    phoneNumber = data.get('phoneNumber')
    email = data.get('email')
    password = data.get('password')
    company_id=data.get('company_id')

    # Check if all required fields are present
    if not (name and phoneNumber and email and password):
        return make_response({'error': 'Missing required fields'}, 400)

    # Hash the password
    hashed_password = generate_password_hash(password)

    # Check if the email is already registered
    # if User.query.filter_by(email=email).first():
    #     return make_response({'error': 'Email already registered'}, 409)

    # Create a new user
    new_user = User(
        name=name,
        phoneNumber=phoneNumber,
        email=email,
        password=hashed_password,
        company_id=company_id,
    )
    try:
        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # Return a success response
        return make_response({'message': 'User created successfully'}, 201)
    except IntegrityError:
        return {
            "error":"422"
        }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)