from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid
from sqlalchemy.sql import func
from app import db


class ReferenceResultData(db.Model):

    __tablename__ = 'reference_result_data'
    __table_args__ = {
        'extend_existing': True
    }
    
    id = db.Column(
        db.Integer,
        primary_key=True
    )
    analyse_data = db.Column(
        db.Integer,
        db.ForeignKey(
            'analyse_data.id'
        )
    )
    result_text = db.Column(
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

    analyse_data_id = db.relationship("AnalyseData", foreign_keys=[analyse_data])

    def __repr__(self):
        return f'{self.result_text}'