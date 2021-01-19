import json, datetime
from flask_restful import Resource, reqparse
from models.Plate import plateModel

# GET /plates
class getPlates(Resource):
    def get(self):
        return {'plates': [plate.json() for plate in plateModel.query.all()]}#query and displays all the saved data from the database as JSON

# GET /plates/<string:plate_id>
class postPlates(Resource):
    def post(self, plate_id):                                                                    
            if plateModel.checkExisting(plate_id):#avoid the same plate to be saved more than once
                return{'message':'Plate {} already exists.'.format(plate_id)}, 400
            newPlate = plateModel(plate_id)
            testPlate = newPlate.validatePlate(plate_id)#calls the validate method
            #error handling
            try:
                if testPlate == 200:#if the return is a valid plate
                    newPlate.save_plate(), 200#saves inside the database
                    return {'plate':'{}'.format(plate_id)}#return the provided JSON data
                elif testPlate == 422:#if returns an invalid plate
                    return {'message':'{} is not a valid German Plate.'.format(plate_id)}, 422
                else:#if the plate wasn't provided
                    return 400

            except:#in case of any other circumstance
                return {'message':'an internal error ocurred trying to save the plate.'}, 500
            
            
            

   