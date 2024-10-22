from sqlalchemy import create_engine, Column, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


Base = declarative_base()

class Task(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    # due_date = Column(Date)
    due_date = Column(String(50))
    status = Column(String(50), default='Todo')

    def __repr__(self):
        return f"<Task(title='{self.title}', description='{self.description}', due_date='{self.due_date}', status='{self.status}')>"

def initialize(db_url)->Session:
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
