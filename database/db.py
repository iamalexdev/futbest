from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base, User

engine = create_engine("sqlite:///futbetmaster.db", echo=False)
Session = sessionmaker(bind=engine)

def init_db():
    Base.metadata.create_all(engine)

def get_session():
    return Session()

def get_user(telegram_id):
    session = get_session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    session.close()
    return user

def create_user(telegram_id, username):
    session = get_session()
    user = User(telegram_id=telegram_id, username=username)
    session.add(user)
    session.commit()
    session.close()

def update_balance(telegram_id, amount):
    session = get_session()
    user = session.query(User).filter_by(telegram_id=telegram_id).first()
    if user:
        user.balance += amount
        session.commit()
    session.close()
