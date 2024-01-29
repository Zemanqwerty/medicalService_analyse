import re
from flask import jsonify, session
from app import ALLOWED_EXTENSIONS, UPLOAD_FOLDER, logger
import os
import app
from werkzeug.utils import secure_filename
import io
from array import array
from app import logger
from . import users_services, analyse_services, reference_result_service
import pandas as pd
import PyPDF2
from fuzzywuzzy import fuzz
from app import BASEDIR


# Функция загрузки файла (POST запрос)
def upload_file(files, message_data):
    try:
        # filename = secure_filename(file.filename)

        CSV_FOLDER = os.path.join(BASEDIR, 'CSV/TEST.csv')
        df = pd.read_csv(CSV_FOLDER)

        for file_index in range(len(files)):
            file = files[f'file_{str(file_index+1)}']
            if file.filename.endswith('.pdf'):
                content = ''
            
                pdf_reader = PyPDF2.PdfReader(file)
                text = ""
                text2 = ""
                for page in pdf_reader.pages:
                    text += page.extract_text() + "\n"
                    text2 += page.extract_text() + "|"
                
                pattern = r"(.*)\s(\d+.?\d+)\*"
                matches = re.findall(pattern, text)
                df1 = pd.DataFrame(matches, columns = ['Показатель', 'Значение'])

                CSV2_FOLDER = os.path.join(BASEDIR, 'CSV/TEST2.csv')
                df2 = pd.read_csv(CSV2_FOLDER)

                token = 90

                if text != "":
                    for i in range(len(df)):
                        a_name = df.iloc[i, 2]
                        if a_name in text:
                            content = df.iloc[i, 1]

                    users_services.create_user(message_data)
                    analyse_id = analyse_services.create_analyse_data(message_data=message_data, result_id=content, filename=file.filename)

                    res = ''

                    for i, row in df1.iterrows():
                        value_a = row['Показатель']
                        for j, row2 in df2.iterrows():
                            value_b = row2['Название']
                            if token > fuzz.token_sort_ratio(value_a, value_b):
                                token = fuzz.token_sort_ratio(value_a, value_b)
                                res = row2['Что означают результаты']
                               
                    reference_result_service.create_reference_result_data(analyse_id=analyse_id, result=res)
                    print(content)
                    if (content == ''):
                        return jsonify({'message': f'Анализ {file.filename} отсутствует в базе данных сервиса'}), 200
                    # else:
                    #     return jsonify({'message': 'Файл успешно загружен! Ознакомится с результатами можно в личном кабинете'}), 200
                else:
                    return jsonify({'message': f'не удаётся распознать файл {file.filename}'}), 200
            else:
                return jsonify({'message': 'выберите .PDF файл'}), 200
        return jsonify({'message': 'Файлы успешно загружены! Ознакомится с результатами можно в личном кабинете'}), 200
    except Exception as e:
        print(e)
        return jsonify({'message': 'Некоррекстный PDF файл. Попробуйте его пересохранить'}), 200