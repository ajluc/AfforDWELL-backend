from models.db import db
from datetime import datetime

class PLUTO(db.Model):
    # Set table name
    __tablename__ = 'pluto_info'
    # Set columns in table. Data comes in as strings -> want to convert bbl to int in script
    id = db.Column(db.Integer, primary_key=True)
    zipcode = db.Column(db.String(255))
    address = db.Column(db.String(255))
    unitsres = db.Column(db.String(255))
    unitstotal = db.Column(db.String(255))
    yearbuilt = db.Column(db.String(255))
    bbl = db.Column(db.BigInteger, unique=True)
    latitude = db.Column(db.String(255))
    longitude = db.Column(db.String(255))
    version = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

    # Constructor for the model
    def __init__(self, zipcode, address, unitsres, unitstotal, yearbuilt, bbl, latitude, longitude, version):
        self.zipcode = zipcode
        self.address = address
        self.unitsres = unitsres
        self.unitstotal = unitstotal
        self.yearbuilt = yearbuilt
        self.bbl = bbl
        self.latitude = latitude
        self.longitude = longitude
        self.version = version
    
    # Queries
    # View JSON data
    def json(self):
        # return {c.name: getattr(self, c.name) for c in self.__table__.columns}
        return {"id": self.id,
                "zipcode": self.zipcode,
                "address": self.address,
                "unitsres": self.unitsres,
                "unitstotal": self.unitstotal,
                "yearbuilt": self.yearbuilt,
                "bbl": self.bbl,
                "latitude": self.latitude,
                "longitude": self.longitude,
                "version": self.version,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}
    
    # Find by BBL
    @classmethod
    def find_by_bbl(cls, bbl):
        pluto = PLUTO.query.filter_by(bbl=bbl).first()
        return pluto
