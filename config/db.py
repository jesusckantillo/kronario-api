from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column,Integer,String, ForeignKey, JSON
from sqlalchemy.orm import relationship


#Creating database
engine = create_engine('sqlite:///krondb.sqlite', echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()



#Association table:
class MajorsClasscodes(Base):
    __tablename__ = "majors_classcodes"
    id = Column(Integer, primary_key=True)
    major_id = Column(Integer, ForeignKey("majors.id"))
    classcode_id = Column(Integer, ForeignKey("classcodes.id"))



class Majors(Base):
    __tablename__ = "majors"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    major_code = Column(String)
    classcodes = relationship("Classcodes",secondary="majors_classcodes", back_populates="majors")
    
class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    dpt_code = Column(Integer)
    classcodes = relationship("Classcodes", backref="department")

class Classcodes(Base):
    __tablename__ ="classcodes"
    id = Column(Integer,primary_key=True)
    name = Column(String)
    cc_code = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    majors_id = Column(Integer, ForeignKey("majors.id"))
    majors = relationship("Majors", secondary="majors_classcodes", back_populates="classcodes")


class NRC(Base):
    __tablename__ = "nrc"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nrc = Column(String)
    teachers = Column(JSON)
    blocks = Column(JSON)
    quotas = Column(Integer)
    cc_code = Column(String, ForeignKey("classcodes.cc_code")) # clave foránea
    classcode = relationship("Classcodes", backref="nrcs") # relación con la clase Classcodes



Base.metadata.create_all(engine)