from flask import Flask
from flask_restful import Api
from flask_migrate import Migrate
from models.db import db

from models.user import User
from models.unit import Unit
from models.building import Building

from resources import user, building, unit

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/affordwell_db"
app.config['SQLALCHEMY_ECHO'] = True # Set to false for prod

db.init_app(app)
migrate = Migrate(app, db)

api.add_resource(user.Users, '/users')
api.add_resource(building.Buildings, '/buildings')
api.add_resource(building.BuildingDetail, '/buildings/<int:building_id>')
api.add_resource(unit.Units, '/units')
api.add_resource(unit.UnitDetail, '/units/<int:unit_id>')

if __name__ == '__main__':
    app.run(debug=True)