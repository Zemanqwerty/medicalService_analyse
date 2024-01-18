from app import db
from ..models.Token import Tokens


def get_tokens_by_user_id(user_id: int):
    return db.session.query(Tokens).filter(Tokens.user==user_id).first()

def update_token(new_refresh_token, user_id):
    token = db.session.query(Tokens).filter(Tokens.user==user_id).first()
    
    # Переопределение данных о пользователе
    token.refresh_token = new_refresh_token

    db.session.commit()
    return f'token {token.id} updated'

def save_token(new_refresh_token, user_id):
    token = Tokens(refresh_token=new_refresh_token, user=user_id)
    db.session.add(token)
    db.session.commit()
    return f'token saved'

def get_tokens_by_token(refresh_token):
    return db.session.query(Tokens).filter(Tokens.refresh_token==refresh_token).first()