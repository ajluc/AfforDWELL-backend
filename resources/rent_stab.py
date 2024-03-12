from flask_restful import Resource
from flask import request
from models.rent_stab import RentStab
from models.db import db
from sqlalchemy.orm import joinedload
from models.pluto import PLUTO

def json_rentstab(rent_stab):
    return {
        'id': rent_stab.id,
        'ucbbl': rent_stab.ucbbl,
        'uc2018': rent_stab.uc2018,
        'pdfsoa2018': rent_stab.pdfsoa2018,
        'uc2019': rent_stab.uc2019,
        'pdfsoa2019': rent_stab.pdfsoa2019,
        'uc2020': rent_stab.uc2020,
        'pdfsoa2020': rent_stab.pdfsoa2020,
        'uc2021': rent_stab.uc2021,
        'pdfsoa2021': rent_stab.pdfsoa2021,
    }

def json_pluto(pluto):
    if pluto:
        return {
            'unitsres': pluto.unitsres,
            'unitstotal': pluto.unitstotal,
            'yearbuilt': pluto.yearbuilt,
            'latitude': pluto.latitude,
            'longitude': pluto.longitude
        }
    return None

class RentStabs(Resource):
    def get(self):
        # data = RentStab.find_all()
        # return [rs.json() for rs in data]
        data = db.session.query(RentStab, PLUTO).outerjoin(PLUTO, RentStab.ucbbl == PLUTO.bbl).all()

        if data:
            results = [{**json_rentstab(rent_stab), **json_pluto(pluto)} for rent_stab, pluto in data]
            return results
        else:
            return {'message': 'No data found'}, 404
    
class RentStabDetails(Resource):
    def get(self, bbl):
        data = db.session.query(RentStab, PLUTO).outerjoin(PLUTO, RentStab.ucbbl == PLUTO.bbl).filter(RentStab.ucbbl == bbl).first()

        if data:
            rent_stab, pluto = data
            return {**json_rentstab(rent_stab), **json_pluto(pluto)}
        else:
            return {'message': 'No data found'}, 404
    
    def delete(self, bbl):
        data = RentStab.delete(bbl)
        return data