from multiprocessing import connection
import sqlite3
from turtle import update
from flask_restful import Resource, reqparse 
from flask_jwt import jwt_required
from models.item import ItemModel


#Creating class Item which inherits resource function
class Item(Resource):
    parser = reqparse.RequestParser()
    #only accept "price" and not any other argument such as "pric" etc...
    parser.add_argument('price', type =float, required=True, help ="This field cannot be left blank")
        
    parser.add_argument('store_id', type =int, required=True, help ="Every item needs a store id")
     
    #requires authentication
    @jwt_required()
    #for GET Request get(self, name) -> self is basic and it just takes itself as an argument, name which is the second argument
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'item not found'}, 404
    
   
    
    
    def post(self, name):
        if ItemModel.find_by_name(name):
            return{'message': " an item with '{}' already exists".format(name)}, 400
        
        
        #checking if the item already exists and returning a message that item already exists.
        #if next(filter(lambda x: x['name'] == name, items), None) is not None: 
        #    return{'message': " an item with '{}' already exists".format(name)}, 400
        
        data = Item.parser.parse_args()
        
       # data = request.get_json()   # force process all text using force= true or silient= true within get.json()
       # get data from the input json and then find the item variables
       # Append the item to the item list and return a variable created status code
        item = ItemModel(name, **data)
        #items.append(item)
        
        try:
            item.save_to_db()
        except:
            return{"message":"An error occured inserting the item"}, 500
        
        
        return item.json() , 201
   
    
    #defining the delete request
    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()
        
        return {'message':'Item Deleted'}
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "DELETE FROM items WHERE name=?"
        # cursor.execute(query, (name,))
        
        # connection.commit()
        # connection.close()
        
        #use the global item variable and not the in class variable, without this there will be an error with this function call
        #global items
        # item list is now all the elements except the element which has been passed, and the list is overwritten.
        # Overwrite the list with all elements except the passed element(to delete the element)
        #items = list(filter(lambda x : x['name']!= name, items))
        #return message to let the user know that function was executed
        
        return {'message': 'Item deleted'}
    
    #defining the put request
    def put(self, name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        #updated_item = ItemModel(name, data['price'])
        
        
        if item is None:
            try:
                #updated_item.insert()
                item = ItemModel(name, **data)
            except:
                return{"message":"An error occured updating the item"}, 500
                
        else:
            item.price = data['price']
            
        item.save_to_db()
            # try:
            #     updated_item.update()
            # except:
            #     return{"message":"An error occured updating the item"}, 500
        return item.json()
    
   
        
        
        
        

#get all items class
class ItemList(Resource):
   def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'id': row[0], 'name': row[1], 'price': row[2]})
        
        connection.close()
        return {'items': items}
    
    
    #defining the GET request for [Get all items]
   # def get(self):
   
        #return list of all items
    #    return{'items': items}