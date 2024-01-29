from flask import jsonify
from . import users_services
from ..models.ReferenceResultData import ReferenceResultData
from ..models.Data import Data
from app import db


def create_reference_result_data(analyse_id, result):
    reference_result = ReferenceResultData(
        analyse_data=analyse_id,
        result_text=result
    )
    
    db.session.add(reference_result)
    db.session.commit()
    return reference_result.id