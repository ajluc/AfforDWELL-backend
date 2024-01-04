from models.db import db
from datetime import datetime

class Building(db.Model):
    # Set table name
    __tablename__ = 'buildings'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    zip = db.Column(db.Integer)
    bldgno1 = db.Column(db.String(255))
    street1 = db.Column(db.String(255))
    stsufx1 = db.Column(db.String(255))
    bldgno2 = db.Column(db.String(255))
    street2 = db.Column(db.String(255))
    stsufx2 = db.Column(db.String(255))
    city = db.Column(db.String(255))
    county = db.Column(db.Integer)
    status1 = db.Column(db.String(255))
    status2 = db.Column(db.String(255))
    status3 = db.Column(db.String(255))
    block = db.Column(db.Integer)
    lot = db.Column(db.Integer)
    address = db.Column(db.String(255))
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    # Set association columns 
    units = db.relationship("Unit", cascade="all", back_populates="building")

    # Constructor for the model
    def __init__(self, bldgno1, bldgno2, **kwargs):
        self.bldgno1 = str(bldgno1)
        self.bldgno2 = str(bldgno2)
        super(Building, self).__init__(**kwargs)

    # Queries
    # View (relevant) JSON data
    def json(self):
        return {"id": self.id,
                "zip": self.zip,
                "bldgno1": self.bldgno1,
                "street1": self.street1,
                "stsufx1": self.stsufx1,
                "city": self.city,
                "address": self.address,
                "latitude": self.latitude,
                "longitude": self.longitude,
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
