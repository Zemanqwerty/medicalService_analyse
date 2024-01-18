from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class Tokens(db.Model):

    __tablename__ = 'tokens'
    __table_args__ = {
        'extend_existing': True
    }
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    refresh_token = db.Column(
        db.String
    )
    user = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id'
        )
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

    user_id = db.relationship("Users", foreign_keys=[user])


    def __repr__(self):
        return f'{self.refresh_token}'