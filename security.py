# importing a specific library for a specific function
from werkzeug.security import safe_str_cmp
#from user page import USER class
from models.user import UserModel


# users = [
#     User(1,'bob','asdf')
# ]

# username_mapping = {u.username: u for u in users}
# userid_mapping = {u.id: u for u in users}



#username_mapping = {'bob': {
#        'id' : 1,
#        'username' : 'bob',
#        'password' : 'asdf'
#    } }

# userid_mapping = {1 : {
#         'id' : 1,
#         'username' : 'bob',
#         'password' : 'asdf'
#     }}

#authenticate function takes in two arguments
def authenticate(username, password):
    #access the user file and send username argument and store the return value in user
    user = UserModel.find_by_username(username)
    # short hand [If user is not None] safe_str_cmp
    #compare the two strings, user.password with password in the safe_str_cmp
    #return the user
    #if user exists compare database password with provided password
    if user and safe_str_cmp(user.password, password): # secure way of comparing strings
        return user

#Unique to flask JWT, accept the JWT string in the identity function
def identity(payload):
    # extract the user id from the payload
    # confirm user by id using the user file function
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)