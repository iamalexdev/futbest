from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True)
    username = Column(String)
    balance = Column(Float, default=100.0)  # Saldo inicial simbólico
    created_at = Column(DateTime, default=datetime.utcnow)

    bets = relationship("Bet", back_populates="user")

class Bet(Base):
    __tablename__ = "bets"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    match = Column(String)
    team = Column(String)
    amount = Column(Float)
    odds = Column(Float)
    status = Column(String, default="pendiente")
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="bets")
