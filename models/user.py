import sqlite3
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    
    #initialise the init function with self, _id , username and password
    def __init__(self,username, password):
        #assign the self.variable with the respective passed variables
        self.username = username
        self.password = password
    
    
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    #only specific to this class
    @classmethod
    def find_by_username(cls,username): # same as function(self, variable)
        return cls.query.filter_by(username=username).first()
    
    #     #connect to the DB
    #     connection = sqlite3.connect('data.db')
    #     cursor = connection.cursor()
        
    #     query = "SELECT * FROM users WHERE username=?"
    #     result = cursor.execute(query, (username,)) # assigned the username variable to the correct query location and storing result
    #     row = result.fetchone()
    #     if row: # simplified version of [if row is not None:] , if there is a user return that user 
    #         user = cls(*row) #simplified version of cls(row[0], row[1], row[2])
    #     else:
    #         user = None
        
    #     connection.close()
    #     return user
    
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row: # simplified version of [if row is not None:]
        #     user = cls(*row) #simplified version of cls(row[0], row[1], row[2])
        # else:
        #     user = None
        
        # connection.close()
        # return user
    