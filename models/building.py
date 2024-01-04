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
    units = db.relationship("Unit", cascade="all", back_populates="building")

    # Constructor for the model
    def __init__(self, address, units):
        self.address = address,
        # self.units = units

    # Queries
    # View JSON data
    def json(self):
        return {"id": self.id,
                "address": self.address,
                # "units": self.units,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}
    
    # Create building
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    # Find all buildings
    @classmethod
    def find_all(cls):
        return Building.query.all()
    
    # Find building by id
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')
