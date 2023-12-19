from models.db import db
from datetime import datetime

class Building(db.Model):
    # Set table name
    __tablename__ = 'buildings'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    # Set association columns 

    # Constructor for the model
    def __init__(self, address):
        self.address = address
