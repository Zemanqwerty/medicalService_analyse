from flask import Flask, current_app, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
import os
from loguru import logger


# Определение корневой директории
BASEDIR = os.path.abspath(os.path.dirname(__file__))

# Определение логгера
logger.add('debug.log', format='{time} {level} {message}', level='DEBUG')

# Определение приложения
app = Flask(__name__)
app.config.from_object('config.DevelopConfig')
cors = CORS(app, supports_credentials=True)




db = SQLAlchemy(app)

# Определение корневого пути для записи файлов
UPLOAD_FOLDER = os.path.join(BASEDIR, 'files/')
# Определение допустимых расширения для файлов
ALLOWED_EXTENSIONS = {'pdf'}



# подключение всех функционирующих файлов (необходимо определить для конкретной работы приложения)
from app.models import User, Token, AnalyseData, Data
from app.views import upload_views, Auth_controller, lk_views