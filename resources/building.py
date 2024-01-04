from flask_restful import Resource
from flask import request
from models.building import Building
from models.db import db
from sqlalchemy.orm import joinedload

class Buildings(Resource):
    def get(self):
        buildings = Building.find_all()
        return [b.json() for b in buildings]
    
    def post(self):
        data = request.get_json()
        building = Building(**data)
        building.create()
        return building.json(), 201
    
class BuildingDetail(Resource):
    def get(self, building_id):
        building = Building.query.options(joinedload(Building.units)).filter_by(id=building_id).first()
        units = [u.json() for u in building.units]
        return {**building.json(), 'units': units}
