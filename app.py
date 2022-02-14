import resource
#import flask and create global variable request
from flask import Flask
#import resource, api and reqparse
from flask_restful import Api 
#import jwt and jwt required function
from flask_jwt import JWT
from resources.store import StoreList 


#from security file import function authenticate and identity
from security import authenticate, identity
#from user file import userregister function
from resources.user import UserRegister
from resources.item import Item,ItemList
from resources.store import Store, StoreModel

#Initialiser and app secret key and api assigning
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'jose'
api = Api(app)



@app.before_first_request
def create_tables():
    db.create_all()

#JWT (app, authentication handler, identity handler)
jwt = JWT(app, authenticate, identity) # creates /auth 

#initialization of array
#items = []



api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>') # http://127.0.0.1:5000/item/<item:name> # get specific item
api.add_resource(ItemList, '/items') #get all items
api.add_resource(UserRegister, '/register') # Sign up a user
api.add_resource(StoreList, '/stores')


if __name__ == '__main__':  
    from db import db
    db.init_app(app)
    app.run(port=4918, debug = True) # on which port should flask run



#PUT VERB is idempotent, calling it 10 times does not result in creating of 10 items.