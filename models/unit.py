from models.db import db
from datetime import datetime
from flask import request

class Unit(db.Model):
    # Set table name
    __tablename__ = 'units'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    # Set association columns 
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.id'), nullable=False)
    building = db.relationship("Building", back_populates="units")

    # Constructor for the model
    def __init__(self, unit_number, building_id):
        self.unit_number = unit_number
        self.building_id = building_id

    # Queries
    # View JSON data
    def json(self):
        return {"id": self.id,
                "unit_number": self.unit_number,
                "building_id": self.building_id,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}
    
    # Create unit
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    # Find all units
    @classmethod
    def find_all(cls):
        return Unit.query.all()
    
    # Find unit by id
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
    
    # Delete unit
    @classmethod
    def delete(cls, unit_id):
        unit = Unit.query.filter_by(id=unit_id).first()
        db.session.delete(unit)
        db.session.commit()
        return ''
    
    # Update unit
    @classmethod
    def update(cls, unit_id):
        unit = Unit.query.filter_by(id=unit_id).first()
        request_data = request.get_json()
        unit.unit_number = request_data['unit_number']
        db.session.commit()
        return unit.json()