from config.db import Base
from sqlalchemy import Column,Integer,String, ForeignKey
from sqlalchemy.orm import relationship

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
