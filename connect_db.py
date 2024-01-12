"""create session"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///hw_07.db", echo=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()
