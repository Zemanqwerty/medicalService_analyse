from app import app, db
from flask import Response, current_app, request

# Создание необходимых таблиц (Если ещё не созданы)
app.app_context().push()
db.create_all()

# Запуск приложения
app.run(host='0.0.0.0', port=5001, debug=True)