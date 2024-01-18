import json
from flask import Flask, Response, current_app, render_template, request, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from flask_session import Session
from flask_pydantic import validate
from ..serivces import upload_services
from flask_sqlalchemy import SQLAlchemy
from app import app
from ..serivces.Auth_service import authenticate

# Маршрут добавления файла
@app.route('/upload', methods=['POST'])
@validate()
def create_message():
    print('---')
    print(request.files)
    print('---')
    print(request.files['file_1'])
    print('---')
    if 'file_1' not in request.files:
        print('full empty')
        return jsonify({'message': 'file is not selected'}), 401
    
    


    
    message_data = {
        "first_name": request.form.get('first_name'),
        "last_name": request.form.get('last_name'),
        "report": request.form.get('report'),
        "age": int(request.form.get('age')),
        "sex": request.form.get('sex'),
    }

    return upload_services.upload_file(files=request.files, message_data=message_data)
