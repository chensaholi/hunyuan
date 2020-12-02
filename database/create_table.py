from sqlalchemy import create_engine, Column, String, Integer, CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://root:root@139.9.126.27:3306/hunyuan")

"""
1. show databases;
2. CREATE DATABASE `hunyuan` CHARACTER SET utf8 COLLATE utf8_general_ci;
3. drop database hunyuan;
4. desc hunyuan;
5. DROP TABLE hunyuan;

"""


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(length=50))
    user_pwd = Column(String(length=256))
    user_type = Column(CHAR(length=10))
    create_time = Column(DateTime)


if __name__ == '__main__':
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
