from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///event_wizard.db', echo=True)
Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()