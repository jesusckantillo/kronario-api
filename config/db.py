from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from sqlalchemy import Column, Integer, String, ForeignKey
from datetime import datetime, time

engine = create_engine('sqlite:///krondb.sqlite')
Base = declarative_base()
SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()


class MajorsClasscodes(Base):
    __tablename__ = "majors_classcodes"
    id = Column(Integer, primary_key=True)
    major_id = Column(Integer, ForeignKey("majors.id"))
    classcode_id = Column(Integer, ForeignKey("classcodes.id"))


class Majors(Base):
    __tablename__ = "majors"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    major_code = Column(String)
    classcodes = relationship("Classcodes", secondary="majors_classcodes", back_populates="majors")


class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    dpt_code = Column(Integer)
    classcodes = relationship("Classcodes", backref="department")


class Classcodes(Base):
    __tablename__ = "classcodes"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    cc_code = Column(String)
    department_id = Column(Integer, ForeignKey("departments.id"))
    departments = relationship("Department", back_populates="classcodes", overlaps="department")
    majors = relationship("Majors", secondary="majors_classcodes", back_populates="classcodes")
    nrcs = relationship("NRC", backref="classcode")  # relación uno a muchos con NRC


class NRC(Base):
    __tablename__ = "nrc"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    nrc = Column(String)
    quotas = Column(Integer)
    cc_code = Column(String, ForeignKey("classcodes.cc_code"))  # clave foránea

    blocks = relationship("Block", backref="nrc")  # relación uno a muchos con Block

    def to_dict(self) -> dict:
        nrc_dict = {
            "name": self.name,
            "nrc": self.nrc,
            "quotas": self.quotas,
            "cc_code": self.cc_code,
            "teachers": None,
            "blocks": []
        }
        block_list = [[block.day,f"{block.time_start} - {block.time_end}",block.room] for block in self.blocks]
        teachers = [block.teacher.name for block in self.blocks]
        nrc_dict["blocks"] = block_list
        nrc_dict["teachers"]  = teachers
        nrc_dict["teachers"]  = set(nrc_dict["teachers"])
        return nrc_dict# relación uno a muchos con Block


class Block(Base):
    __tablename__ = "blocks"
    id = Column(Integer, primary_key=True)
    nrc_id = Column(Integer, ForeignKey("nrc.id"))
    day = Column(String)
    time_start = Column(String)
    time_end = Column(String)
    room = Column(String)
    teacher_id = Column(Integer, ForeignKey("teachers.id"))  # clave foránea

    def parse_time(self, time_str: str) -> time:
        return datetime.strptime(time_str, "%H%M").time()


class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    blocks = relationship("Block", backref="teacher")


# Crear tablas en la base de datos
Base.metadata.create_all(engine)
