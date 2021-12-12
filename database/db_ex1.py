from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() # create a super class reference

class Contact(Base):

    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    contact = Column(String(10))
    date = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.name
        
class TodoList(Base):
    __tablename__ = "todolist"
    id = Column(Integer, primary_key=True)
    task = Column(String)
    date = Column(DateTime, default=datetime.now())
    status = Column(Boolean,default=False)

    def __str__(self):
        return self.task

if __name__ == "__main__":
    Base.metadata.create_all(create_engine('sqlite:///ex.db'))