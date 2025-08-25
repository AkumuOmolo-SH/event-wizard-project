from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///event_wizard.db")

Session=sessionmaker(bind=engine)
session=Session()

Base=declarative_base