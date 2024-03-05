from models.db import db
from datetime import datetime

class RentStab(db.Model):
    # Set table name
    __tablename__ = 'rent_stab'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    ucbbl = db.Column(db.Integer)
    uc2018 = db.Column(db.Integer)
    pdfsoa2018 = db.Column(db.String(255))
    uc2019 = db.Column(db.Integer)
    pdfsoa2019 = db.Column(db.String(255))
    uc2020 = db.Column(db.Integer)
    pdfsoa2020 = db.Column(db.String(255))
    uc2021 = db.Column(db.Integer)
    pdfsoa2021 = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())

    # Queries
    # View JSON data
    def json(self):
        return {"id": self.id,
                "ucbbl": self.ucbbl,
                "uc2018": self.uc2018,
                "pdfsoa2018": self.pdfsoa2018,
                "uc2019": self.uc2019,
                "pdfsoa2019": self.pdfsoa2019,
                "uc2020": self.uc2020,
                "pdfsoa2020": self.pdfsoa2020,
                "uc2021": self.uc2021,
                "pdfsoa2021": self.pdfsoa2021,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}