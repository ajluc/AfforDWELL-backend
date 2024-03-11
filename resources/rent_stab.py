from flask_restful import Resource
from flask import request
from models.rent_stab import RentStab
from models.db import db
from sqlalchemy.orm import joinedload
from flask import jsonify
from models.pluto import PLUTO


class RentStabs(Resource):
    def get(self):
        data = RentStab.find_all()
        return [rs.json() for rs in data]
        # result = [row._asdict() for row in data]
        # return jsonify(result)
    
class RentStabDetails(Resource):
    def get(self, bbl):
        # data = RentStab.find_by_bbl(ucbbl=bbl)
        # result = data.json()
        # return result
        result = db.session.query(RentStab, PLUTO).outerjoin(PLUTO, RentStab.ucbbl == PLUTO.bbl).filter(RentStab.ucbbl == bbl).first()

        if result:
            rent_stab, pluto = result
            return jsonify({
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
                'pluto': {
                    'unitsres': pluto.unitsres if pluto else None,
                    'unitstotal': pluto.unitstotal if pluto else None,
                    'yearbuilt': pluto.yearbuilt if pluto else None,
                    'latitude': pluto.latitude if pluto else None,
                    'longitude': pluto.longitude if pluto else None,
                }
            })
        else:
            return {'message': 'No data found'}, 404
    
    def delete(self, bbl):
        data = RentStab.delete(bbl)
        return data