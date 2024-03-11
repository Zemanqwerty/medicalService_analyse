from app import app
from flask import request, jsonify
from ..schemas.user_schemas import LoginUser
from flask_pydantic import validate
from ..serivces import Auth_service
from ..serivces.Auth_service import authenticate


@app.route('/auth/sign-in', methods=['POST'])
@validate()
def login(body: LoginUser):
    try:
        res = Auth_service.login(user_data=body)
        response = jsonify(res)
        if 'refresh_token' in res:
            response.set_cookie('refresh_token', res['refresh_token'], max_age=30 * 24 * 60 * 60 * 1000, httponly=True)
            return response, 200
        return response, 401
    except Exception as e:
        print(e)


@app.route('/auth/refresh', methods=['GET'])
def refresh():
    try:
        res = Auth_service.refresh(refresh_token=request.cookies['refresh_token'])
        response = jsonify(res)
        if 'refresh_token' in res:
            response.set_cookie('refresh_token', res['refresh_token'], max_age=30 * 24 * 60 * 60 * 1000, httponly=True)
            return response, 200
        return response, 401
    except Exception as e:
        print('---')
        print(e)
        return jsonify(str(e)), 401

@app.route('/auth/logout', methods=['GET'])
def logout():
    try:
        response = jsonify(Auth_service.logout(refresh_token=request.cookies['refresh_token']))
        response.delete_cookie('refresh_token')
        return response
    except Exception as e:
        print(e)
        return jsonify(str(e)), 500