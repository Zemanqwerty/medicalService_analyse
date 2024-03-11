from flask import make_response, jsonify, request
from . import users_services
import jwt
import datetime
from app import app, logger
from functools import wraps
from . import tokens_services


def login(user_data):
    check_user = users_services.get_user_by_fio(first_name=user_data.first_name,
                                                last_name=user_data.last_name,
                                                report=user_data.report)

    if not check_user:
        return {
            'res': 'user does not exist'
        }

    if check_user.password != user_data.password:
        logger.info(f'USER - {check_user.first_name} {check_user.last_name} HAS ENTERED INCORRECT PASSWORD')
        return {
            'res': 'incorrect password'
        }
    
    access_token = jwt.encode({
                'public_id': check_user.id,
                'public_last_name': check_user.last_name,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)
            }, app.config['SECRET_KEY'])
    
    refresh_token = jwt.encode({
                'public_id': check_user.id,
                'public_lastname': check_user.last_name,
                'exp' : datetime.datetime.utcnow() + datetime.timedelta(days = 30)
            }, app.config['SECRET_KEY'])
    

    tokens = tokens_services.get_tokens_by_user_id(user_id=check_user.id)

    if tokens:
        tokens_services.update_token(new_refresh_token=refresh_token,
                                user_id=check_user.id)
    else:
        tokens_services.save_token(new_refresh_token=refresh_token,
                              user_id=check_user.id)

    logger.info(f'USER - {check_user.first_name} {check_user.last_name} HAS LOGGED IN')

    res = {
        'access_token': access_token,
        'refresh_token': refresh_token,
        'user': {
            'firstname': check_user.first_name,
            'lastname': check_user.last_name,
            'report': check_user.report,
            'user_id': check_user.id
        }
    }

    return res


def validate_access_token(access_token):
    try:
        user_data = jwt.decode(access_token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return user_data
    except Exception as e:
        print(e)
        return None
    

def validate_refresh_token(refresh_token):
    try:
        user_data = jwt.decode(refresh_token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return user_data
    except Exception as e:
        return None


def refresh(refresh_token):
    try:
        if not refresh_token or refresh_token is None:
            return jsonify({'message': 'Unauthorized'}), 401
    
        payload_user_data = validate_refresh_token(refresh_token=refresh_token)

        token_in_db = tokens_services.get_tokens_by_token(refresh_token=refresh_token)

        if payload_user_data is None or not token_in_db:
            return jsonify({'message': 'Unauthorized'}), 401
        
        check_user = users_services.get_user_by_id(payload_user_data['public_id'])
        
        new_access_token = jwt.encode({
                    'public_id': payload_user_data['public_id'],
                    'public_lastname': payload_user_data['public_lastname'],
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes = 30)
                }, app.config['SECRET_KEY'])
        
        new_refresh_token = jwt.encode({
                    'public_id': payload_user_data['public_id'],
                    'public_lastname': payload_user_data['public_lastname'],
                    'exp' : datetime.datetime.utcnow() + datetime.timedelta(days = 30)
                }, app.config['SECRET_KEY'])
        

        tokens = tokens_services.get_tokens_by_user_id(user_id=payload_user_data['public_id'])

        if tokens:
            tokens_services.update_token(new_refresh_token=new_refresh_token,
                                    user_id=payload_user_data['public_id'])
        else:
            tokens_services.save_token(new_refresh_token=new_refresh_token,
                                user_id=payload_user_data['public_id'])

        
        new_tokens = {
            'access_token': new_access_token,
            'refresh_token': new_refresh_token,
            'user': {
                'firstname': check_user.first_name,
                'lastname': check_user.last_name,
                'report': check_user.report,
                'user_id': check_user.id
            }
        }

        return new_tokens
    except Exception as e:
         print(e)
         return {
                'res': 'oops error'
            }

def logout(refresh_token):
    try:
        return tokens_services.remove_token_from_db(refresh_token=refresh_token)
    except Exception as e:
        print(e)


def authenticate():
    def _authenticate(f):
        @wraps(f)
        def __authenticate(*args, **kwargs):
            try:
                auth_header = request.headers['authorization']
                if not auth_header:
                    return jsonify({
                        'res': 'incorrect token'
                    }), 401
                
                access_token = auth_header.split(' ')[1]
                if not access_token:
                    return jsonify({
                        'res': 'incorrect token'
                    }), 401
                
                user_data = validate_access_token(access_token=access_token)
                if user_data is None:
                    return jsonify({
                        'res': 'incorrect token'
                    }), 401
                
                return f(user_data)

            except Exception as e:
                print(e)
                return jsonify({
                        'res': 'incorrect token'
                    }), 401
        return __authenticate
    return _authenticate
