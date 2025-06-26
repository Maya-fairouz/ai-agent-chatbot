from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    user_input = Column(String)
    bot_response = Column(String)
    timestamp = Column(DateTime)