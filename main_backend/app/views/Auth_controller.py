from app import app
from flask import request, jsonify
from ..schemas.user_schemas import LoginUser
from flask_pydantic import validate
from ..serivces import Auth_service
from ..serivces.Auth_service import authenticate


@app.route('/auth/sign-in', methods=['POST'])
@validate()
def login(body: LoginUser):
    res = Auth_service.login(user_data=body)
    response = jsonify(res)
    if 'refresh_token' in res:
        response.set_cookie('refresh_token', res['refresh_token'], max_age=30 * 24 * 60 * 60 * 1000, httponly=True)
        return response, 200
    return response, 401


@app.route('/auth/refresh', methods=['GET'])
def refresh():
    res = Auth_service.refresh(refresh_token=request.cookies['refresh_token'])
    response = jsonify(res)
    if 'refresh_token' in res:
        response.set_cookie('refresh_token', res['refresh_token'], max_age=30 * 24 * 60 * 60 * 1000, httponly=True)
        return response, 200
    return response, 401


@app.route('/auth_check', methods=['GET'])
@authenticate()
def auth_check(user_data):
    return jsonify({
        'res': user_data
    })
