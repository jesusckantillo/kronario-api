from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship


#Creating database
engine = create_engine('sqlite:///config/kronario.sqlite', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()


class Majors(Base):
    __tablename__ = "majors"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True)
    name = Column(String)
    major_code = Column(String)
    classcodes = relationship("Classcodes",back_populates="majors")
    
class Department(Base):
    __tablename__ = "departments"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True)
    name = Column(String)
    dpt_code = Column(Integer)
    classcodes = relationship("Classcodes", backref="department")

class Classcodes(Base):
    __tablename__ ="classcodes"
    __table_args__ = {'extend_existing': True}
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cc_code = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    majors_id = Column(Integer, ForeignKey("majors.id"))
    majors = relationship("Majors",back_populates="classcodes")



Base.metadata.create_all(engine)

