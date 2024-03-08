from flask_restful import Resource
from flask import request
from models.rent_stab import RentStab
from models.db import db
from sqlalchemy.orm import joinedload

class RentStabs(Resource):
    def get(self):
        data = RentStab.find_all()
        return [rs.json() for rs in data]
    
class RentStabDetails(Resource):
    def get(self, bbl):
        data = RentStab.find_by_bbl(ucbbl=bbl)
        result = data.json()
        return result
    
    def delete(self, bbl):
        data = RentStab.delete(bbl)
        return data