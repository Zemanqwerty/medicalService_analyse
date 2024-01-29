import json
from flask import Flask, Response, current_app, render_template, request, redirect, url_for, session, jsonify
from flask_cors import cross_origin
from flask_session import Session
from flask_pydantic import validate
from ..serivces import analyse_services
from ..schemas.user_schemas import LoginUser
from flask_sqlalchemy import SQLAlchemy
from app import app
from ..serivces.Auth_service import authenticate

# Маршрут добавления файла
@app.route('/lk', methods=['GET'])
@authenticate()
def get_analyse(user_data):
    return jsonify(analyse_services.get_analyse_data(user_id=user_data['public_id']))