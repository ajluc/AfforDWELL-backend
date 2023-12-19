from models.db import db
from datetime import datetime

class Unit(db.Model):
    # Set table name
    __tablename__ = 'units'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    unit_number = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    # Set association columns 

    # Constructor for the model
    def __init__(self, unit_number):
        self.unit_number = unit_number
