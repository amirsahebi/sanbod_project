from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import String,Integer,Column, Text , DateTime

engine = create_engine("mysql+pymysql://amir:sahebi@mysql:3306/test",echo=True) 

Base = declarative_base()

sessionlocal=sessionmaker(bind=engine)

print("Creating database ...")

class City(Base):
    __tablename__='cities'
    id = Column(Integer,primary_key=True)
    name = Column(String(255),nullable=False,unique=True)
    weather = Column(String(255),nullable=False)

    def __repr__(self):
        return f"<city name={self.name}>"


Base.metadata.create_all(engine)