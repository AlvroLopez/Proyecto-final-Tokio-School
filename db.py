from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///database/datos.db")

Session = sessionmaker(bind=engine)
sesion = Session()

Base = declarative_base()
