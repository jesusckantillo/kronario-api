from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#Creating database
engine = create_engine('sqlite:///kronario.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

