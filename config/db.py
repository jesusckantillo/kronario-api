
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Column, Boolean, String, Index, ForeignKey

#Creating database
engine = create_engine('sqlite:///kronario.sqlite', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
db = Session()

Base.metadata.create_all(engine)
