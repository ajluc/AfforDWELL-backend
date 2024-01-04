from flask_restful import Resource
from flask import request
from models.unit import Unit
from models.db import db
from sqlalchemy.orm import joinedload

class Units(Resource):
    def get(self):
        units = Unit.find_all()
        return [u.json() for u in units]
    
    def post(self):
        data = request.get_json()
        unit = Unit(**data)
        unit.create()
        return unit.json(), 201
    
    