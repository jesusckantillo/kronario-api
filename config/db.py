from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Integer, Column, Boolean, String, Index, ForeignKey

#Creating database
engine = create_engine('sqlite:///config/kronario.sqlite', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()
Base.metadata.create_all(engine)
