from models.db import db
from datetime import datetime

class User(db.Model):
    # Set table name
    __tablename__ = 'users'
    # Set columns in table
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(255))
    password_digest = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False, onupdate=datetime.now())
    # Set association columns 

    # Constructor for the model
    def __init__(self, name, email, password_digest):
        self.name = name
        self.email = email
        self.password_digest = password_digest

    # Queries
    # View JSON data
    def json(self):
        return {"id": self.id,
                "name": self.name,
                "email": self.email,
                "password_digest": self.password_digest,
                "created_at": str(self.created_at),
                "updated_at": str(self.updated_at)}
    
    # Create user
    def create(self):
        db.session.add(self)
        db.session.commit()
        return self
    
    # Find all users
    @classmethod
    def find_all(cls):
        return User.query.all()
    
    # Find user by id
    @classmethod
    def find_by_id(cls, id):
        return db.get_or_404(cls, id, description=f'Record with id:{id} is not available')