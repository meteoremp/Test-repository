from multiprocessing import connection
import sqlite3
from unittest import result
from flask_restful import Resource, reqparse
from models.user import UserModel

# Signing up a user
class UserRegister(Resource):
    #obtain the json data and make sure that the argument contains username and password and required = true
    parser = reqparse.RequestParser()
    parser.add_argument('username', type = str , required = True, help ="This field cannot be left blank")
    parser.add_argument('password', type = str , required = True, help ="This field cannot be left blank")

    #defining the userregister post 
    def post(self):
        #store defined parse args in data variable
        data = UserRegister.parser.parse_args()
        
        
        if UserModel.find_by_username(data['username']):
            return{"message": "A user with that username already exists"}, 400
        
        user = UserModel(**data)
        user.save_to_db()
        
        # #make sure this part always is able to close the connection
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # #running the query to insert the data into DB
        # query = "INSERT INTO users VALUES (NULL,?,?)"
        # cursor.execute(query, (data['username'], data['password'],)) # this is a tuple argument # same as function(query, arguments)
        
        # #commit the changes
        # #close the connection
        # #return status code and message
        # connection.commit()
        # connection.close()
        
        return {"message":"User Created Successfully"}, 201
        