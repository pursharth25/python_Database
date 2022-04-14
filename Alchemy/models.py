from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///final.db',echo=True) 


Session = sessionmaker(bind=engine) # used
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    lastname = Column(String)
    def __repr__(self):
        return "<User(name='%s', fullname='%s', lastname='%s')>" % (self.name, self.fullname, self.lastname)


if __name__ == '__main__':
    Base.metadata.create_all(engine) 

row = session.query(User).filter(User.fullname.like('p%')).all()
print(row)


                