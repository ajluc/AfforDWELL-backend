from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db

from models.user import User
from models.unit import Unit
from models.building import Building
from models.rent_stab import RentStab
from models.pluto import PLUTO

from resources import user, building, unit, rent_stab, pluto

application = Flask(__name__)
# @application.route("/")
# def hello_world():
#     return "Hello, World!"
api = Api(application)

application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
application.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/affordwell_db"
application.config['SQLALCHEMY_ECHO'] = True # Set to false for prod

db.init_app(application)
migrate = Migrate(application, db)

api.add_resource(rent_stab.RentStabs, '/rentstabs')
api.add_resource(rent_stab.RentStabDetails, '/rentstabs/<int:bbl>')
api.add_resource(pluto.PLUTODetails, '/plutos/<int:bbl>')
api.add_resource(user.Users, '/users')
api.add_resource(building.Buildings, '/buildings')
api.add_resource(building.BuildingDetail, '/buildings/<int:building_id>')
api.add_resource(unit.Units, '/units')
api.add_resource(unit.UnitDetail, '/units/<int:unit_id>')

if __name__ == '__main__':
    # application.run(debug=True)
    application.run(host='0.0.0.0', port=8000)