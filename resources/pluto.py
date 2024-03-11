from flask_restful import Resource
from flask import request
from models.pluto import PLUTO
from models.db import db
from sqlalchemy.orm import joinedload

class PLUTODetails(Resource):
    def get(self, bbl):
        data = PLUTO.find_by_bbl(bbl)
        if data:
            result = data.json()
            return result
        else:
            return {'message': 'Entry not found'}, 404