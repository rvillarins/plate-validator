import json, datetime
from flask_restful import Resource, reqparse
from models.Plate import plateModel

# GET /plates
class getPlates(Resource):
    def get(self):
        return {'plates': [plate.json() for plate in plateModel.query.all()]}

# GET /plates/<string:plate_id>
class postPlates(Resource):
    def post(self, plate_id):                                                                    
            if plateModel.checkExisting(plate_id):
                return{'message':'Plate {} already exists.'.format(plate_id)}, 400
            newPlate = plateModel(plate_id)
            testPlate = newPlate.validatePlate(plate_id)
            try:
                if testPlate == 200:
                    newPlate.save_plate(), 200
                    return {'plate':'{}'.format(plate_id)}
                elif testPlate == 422:
                    return {'message':'{} is not a valid German Plate.'.format(plate_id)}, 422
                else:
                    return 400

            except:
                return {'message':'an internal error ocurred trying to save the plate.'}, 500
            
            
            

   