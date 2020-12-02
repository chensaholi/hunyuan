from sqlalchemy import Column, String, Integer, CHAR, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_name = Column(String(length=50))
    user_pwd = Column(String(length=256))
    user_type = Column(CHAR(length=10))
    create_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<UserDetails(id=%s,user_name=%s,user_pwd=%s,user_type=%s)>' % (
            self.user_id,
            self.user_name,
            self.user_pwd,
            self.user_type
        )

