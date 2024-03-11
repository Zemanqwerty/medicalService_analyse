import re
from flask import jsonify, session
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, logger
import os
import app
from werkzeug.utils import secure_filename
import io
from array import array
from app import logger
from . import users_services, analyse_services, reference_result_service, gigiachat_request_service
import pandas as pd
import PyPDF2
from fuzzywuzzy import fuzz
from app import BASEDIR


def upload_file(files, message_data):
    try:
        CSV_FOLDER = os.path.join(BASEDIR, 'CSV/TEST.csv')
        df = pd.read_csv(CSV_FOLDER)

        for file_index in range(len(files)):
            file = files[f'file_{str(file_index+1)}']
            if file.filename.endswith('.pdf'):
                content = ''
            
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""

                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"

                if text != "":
                    for i in range(len(df)):
                        a_name = df.iloc[i, 2]
                        if a_name in text:
                            content = df.iloc[i, 1]

                    users_services.create_user(message_data)

                    df_for_save = df

                    what_means_value = df.loc[df['id'] == content, 'Что означают результаты'].values[0]

                    analyse_id = analyse_services.create_analyse_data(message_data=message_data, result_id=content, filename=file.filename, main_dataframe=str(df_for_save))

                    reference_result_service.create_reference_result_data(analyse_id=analyse_id, result=gigiachat_request_service.api_text_generation(text, what_means_value))
                    if (content == ''):
                        return jsonify({'message': f'Анализ {file.filename} отсутствует в базе данных сервиса'}), 200
                else:
                    return jsonify({'message': f'не удаётся распознать файл {file.filename}'}), 200
            else:
                return jsonify({'message': 'выберите .PDF файл'}), 200
        return jsonify({'message': 'Файлы успешно загружены! Ознакомится с результатами можно в личном кабинете'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Некоррекстный PDF файл. Попробуйте его пересохранить'}), 200