from db import db


class ItemModel(db.Model):
    __tablename__ = 'items'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))
    
    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')
    
    def __init__(self,name,price, store_id):
        
        self.name = name
        self.price = price
        self.store_id = store_id
        
    def json(self):
        return {'name': self.name, 'price': self.price}
    
    
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
        
        
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "SELECT * FROM items WHERE name=?"
        # result = cursor.execute(query,(name,))
        # row = result.fetchone()
        
        # connection.close()
        # if row:
        #     return cls(*row)
        
        #lambda is for not naming a function i.e 1 line function
        #item = next(filter(lambda x: x['name'] == name, items), None) 
        # next will get the next item in the filter list
        # next will break the function if there is not next item in the list or is empty. which is why None is required
        
        
        # for item in items:
        #     if item['name'] == name:
        #         return item
        #return {'item': item}, 200 if item else 404 # shorthand for [if item is not None] return 200 else return 400
        
     
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "INSERT INTO items VALUES(?,?)"
        # cursor.execute(query, (self.name, self.price))
        
        # connection.commit()
        # connection.close()
        
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        
        # query = "UPDATE items SET price=? WHERE name=?"
        # cursor.execute(query, (self.price, self.name))
        
        # connection.commit()
        # connection.close()
        
        
        
        #get the data passed from the parser
        #data = Item.parser.parse_args()
        #get the data passed from the json
        #data = request.get_json()
        #item = next(filter(lambda x: x['name'] == name, items), None)
        #if there is no item then create item
        #if item is None:
        #    item = {'name': name, 'price': data['price']}
        #    items.append(item)
        #if there is already an item
        #else:
            #update using dictionary update method
        #    item.update(data)
        #return the item to show that the update/ PUT request has been executed