from sqlAlchemy import db, DateTime, datetime
from datetime import datetime
import json

class plateModel(db.Model):
    __tablename__ = 'plates'

    plate_id = db.Column(db.String, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
   

    def __init__(self, plate_id):
        self.plate_id = plate_id
        
    def json(self):
        return {
                'plate': self.plate_id,
                'timestamp': self.timestamp.isoformat()
            }
    
    @classmethod
    def checkExisting(cls, plate_id):
        plate = cls.query.filter_by(plate_id = plate_id).first()
        if plate:
            return plate
        return None
    
    def validatePlate(self, plate_id):
        try:
            prefix,sufix = plate_id.split("-")
            letters = ''.join([i for i in sufix if not i.isdigit()])
            numbers = ''.join([i for i in sufix if i.isdigit()])
            if (len(prefix) <= 3 and len(prefix) >= 1) and (len(letters) == 1 or len(letters) == 2) and (len(numbers) <= 4 and numbers[0] != "0"):
                    return 200
            else:
                return 422
        except:
            return 400
        
    def save_plate(self):
        db.session.add(self)
        db.session.commit()
    
   
 

