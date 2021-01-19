#File that describes the plate object
from sqlAlchemy import db, DateTime, datetime
from datetime import datetime
import json

class plateModel(db.Model):
    __tablename__ = 'plates'

    plate_id = db.Column(db.String, primary_key=True)#defines the plate data as the primary key
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)#defines the timestamp as the current time value
   

    def __init__(self, plate_id):
        self.plate_id = plate_id
        
    def json(self):#Serializing the object in JSON format
        return {
                'plate': self.plate_id,
                'timestamp': self.timestamp.isoformat()
            }
    #Object's methods
    @classmethod
    def checkExisting(cls, plate_id):#function to check if a plate already exists in the database
        plate = cls.query.filter_by(plate_id = plate_id).first()#query for the given plate_id
        if plate:
            return plate
        return None
    
    def validatePlate(self, plate_id):#method to validate the plate
        try:
            prefix,suffix = plate_id.split("-")#split the original strings into two strings(variable prefix and suffix), before and after the hyphen
            letters = ''.join([i for i in suffix if not i.isdigit()])#saves only the letter from the suffix of the plate into the variable
            numbers = ''.join([i for i in suffix if i.isdigit()])#saves only the numbers from the sufix of the plate into the variable
            if (len(prefix) <= 3 and len(prefix) >= 1) and (len(letters) == 1 or len(letters) == 2) and (len(numbers) <= 4 and numbers[0] != "0"):
                return 200#return 200 if the plate is valid according the given parametters
            else:
                return 422#return 422 if the plate is not valid 
        except:
            return 400#return 422 if the plate wasn't provided
        
    def save_plate(self):#method that saves the plate inside the database
        db.session.add(self)
        db.session.commit()
    
   
 

