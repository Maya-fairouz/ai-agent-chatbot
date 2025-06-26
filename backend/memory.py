from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Chat
from datetime import datetime

engine = create_engine('sqlite:///chats.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

class Memory:
    def __init__(self):
        self.session = Session()

    def add_chat(self, user_input, bot_response):
        chat = Chat(user_input=user_input, bot_response=bot_response, timestamp=datetime.now())
        self.session.add(chat)
        self.session.commit()

    def get_chats(self):
        return self.session.query(Chat).all()

    def clear_chats(self):
        self.session.query(Chat).delete()
        self.session.commit()