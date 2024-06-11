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
        new_user= User(
            name = request.form.get("name"),
            phoneNumber = request.form.get("phoneNumber"),
            email = request.form.get("email"),
            password = request.form.get("password"),
        )
        db.session.add(new_user)
        db.session.commit()
        user_dict = new_user.to_dict()

        response = make_response(
            jsonify(user_dict), 201
        )
        return response
    
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
        
# @product_routes.route('/api/v1/User', methods=['GET'])
# def view_all_user():
#     page = int(request.args.get('page', 1))
#     per_page = int(request.args.get('per_page', 10))

#     # Query the products using pagination
#     user = User.query.paginate(page=page, per_page=per_page, error_out=False)
#     user_list= []
#     for user in user.items:
#         user_data= {
#                 'id': user.id,
#                 'username': user.username,
#                 'phone number': user.phone_number,
#                 'email': user.email,
#                 'user_type' : user.user_type,
#                 'status': user.status,
#                 'password': user.password
#             }
#         user_list.append(user_data)

#     return jsonify({
#         'status': 'success',
#         'data': user_list
#     })


# @product_routes.route('/api/v1/User/create', methods=['POST'])
# def create_user():
#     data = request.json

#     username=data['username']
#     phone_number=data['phone_number']
#     password=data['password']
#     email=data['email']                    
#     user_type=data['user_type']
#     status='Active'
#     password_harsh= generate_password_hash(password)
#     if User.query.filter_by(username=username).first():
#         return jsonify({'error': 'Username already exist'}), 409
#     if User.query.filter_by(email=email).first():
#         return jsonify({'error': 'Email already exist'}), 409
#     user= User(username=username, email=email, password=password_harsh, 
#                user_type=user_type,status=status,phone_number=phone_number)

#     db.session.add(user)
#     db.session.commit()
#     return jsonify({'message': 'User created successfully'}), 201



# @product_routes.route('/api/v1/Login', methods=['POST'])
# def login():
#     username =request.json["username"]
#     password =request.json["password"]
#     user=User.query.filter_by(username=username).first()
#     if  user and check_password_hash(user.password, password):
#         access_token=generate_token(user)
#         return jsonify({
#             "access-token" : access_token
#         }), 200
#     else:
#         return jsonify({
#             'error' :"Invalid credentials",
#         }),401



# def generate_token(user):
#     secret_key=current_app.config['JWT_SECRET_KEY']
#     expiration= datetime.utcnow()+timedelta(days=1)
#     payload={
#         "sub":user.id,
#         "user_id":user.id,
#         "exp":expiration,
#         "username":user.username,
#         "email":user.email,
#         "usertype":user.user_type
#     }
#     token=jwt.encode(payload, secret_key, algorithm= 'HS256')
#     return token
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)