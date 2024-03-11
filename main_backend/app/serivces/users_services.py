import os
import datetime
from flask import jsonify
from app import db
from ..models.User import Users

# Функция для создания пользователя
def create_user(user_data):
    try:
        created_user = db.session.query(Users).filter(Users.first_name==user_data["first_name"],
                                                      Users.last_name==user_data["last_name"],
                                                      Users.report==user_data["report"]
                                                      ).first()

        if created_user is None:
            # Создаем пользователя с помощью метода create из класса Users_repository
            user = Users(first_name=user_data["first_name"],
                        last_name=user_data["last_name"],
                        report=user_data["report"],
                        age=user_data["age"],
                        sex=user_data["sex"],
                        password='123456')
            db.session.add(user)
            db.session.commit()

            return jsonify({'message': f'user {user_data.first_name} created'})
    except Exception as e:
        print(e)
        return jsonify({'message': 'error'})

def get_user_by_fio(first_name, last_name, report):
    try:
        user = db.session.query(Users).filter(Users.first_name==first_name, 
                                              Users.last_name==last_name,
                                              Users.report==report).first()
        
        return user
    except Exception as e:
        return e
    
def get_user_by_id(id: int):
    return db.session.query(Users).filter(
        Users.id==id
    ).first()