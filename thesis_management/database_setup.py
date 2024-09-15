from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Thesis(Base):
    __tablename__ = 'theses'
    id = Column(Integer, primary_key=True)
    title = Column(String)

engine = create_engine('sqlite:///thesis.db')
Base.metadata.create_all(engine)
