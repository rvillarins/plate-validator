from flask import Flask
from flask_restful import  Api
from resources.plate import getPlates, postPlates

#app setup instructions
app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#app routing
@app.before_first_request
def dbCreate():
    db.create_all()

api.add_resource(getPlates, '/plates')
api.add_resource(postPlates, '/plates/<string:plate_id>')

#activates debug mode and other specs
if __name__ == '__main__':
    from sqlAlchemy import db 
    db.init_app(app)
    app.run(debug=True)