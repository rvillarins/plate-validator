import json, datetime
from flask_restful import Resource, reqparse
from models.Plate import plateModel

#class that returns all initial json data from the list to the routing: /plates
class getPlates(Resource):
    def get(self):
        return {'plates': [plate.json() for plate in plateModel.query.all()]}

class postPlates(Resource):
    def post(self, plate_id):                                  
        if plateModel.checkExisting(plate_id):
            return{'message':'Plate {} already exists.'.format(plate_id)}, 400
        newPlate = plateModel(plate_id)
        
        try:
            newPlate.save_plate(), 201
        except:
            return {'message':'an internal error ocurred trying to save the plate.'}, 500
        
        return{
                'plate': newPlate 
              }, 201 # return the new variable and de 201 created code

   