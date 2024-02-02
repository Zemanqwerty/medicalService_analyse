import json
from flask import jsonify
from . import users_services
from ..models.AnalyseData import AnalyseData
from ..models.Data import Data
from ..models.ReferenceResultData import ReferenceResultData
from app import db


def get_analyse_data(user_id):
    analyse_data = db.session.query(AnalyseData).filter(AnalyseData.user==user_id).all()
    result_list = []

    for analyse in analyse_data:
        result = db.session.query(Data).filter(
            Data.site_ID==analyse.analyse_id
        ).all()

        reference_results = db.session.query(ReferenceResultData).filter(
            ReferenceResultData.analyse_data==analyse.id
        ).all()

        print(reference_results)

        for res in result:
            data = {
                'info_1': res.What_do_the_results_mean,
                'info_2': res.General_information_about_the_study,
                'filename': analyse.file_title,
                'main_frame': analyse.main_dataframe,
                'reference_results': list(map(str, reference_results))
            }
            result_list.append(data)

    return result_list




def create_analyse_data(message_data, result_id, filename, main_dataframe):
    user_id = users_services.get_user_by_fio(first_name=message_data["first_name"],
                                             last_name=message_data["last_name"],
                                             report=message_data["report"])
    
    analyse_data = AnalyseData(user=user_id.id,
                               analyse_id=result_id,
                               file_title=filename,
                               main_dataframe=main_dataframe)
    
    db.session.add(analyse_data)
    db.session.commit()
    return analyse_data.id