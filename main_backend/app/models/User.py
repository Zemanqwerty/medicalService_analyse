from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class Users(db.Model):

    __tablename__ = 'users'
    __table_args__ = {
        'extend_existing': True
    }
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    first_name = db.Column(
        db.String
    )
    last_name = db.Column(
        db.String
    )
    report = db.Column(
        db.String
    )
    age = db.Column(
        db.Integer
    )
    sex = db.Column(
        db.String
    )
    password = db.Column(
        db.String
    )
    created_at = db.Column(
        db.DateTime(timezone=True),
        server_default=func.now()
    )
    modified_at = db.Column(
        db.DateTime,
        server_default=db.func.now(),
        server_onupdate=db.func.now()
    )


    def __repr__(self):
        return f'{self.first_name} {self.last_name} {self.report}'