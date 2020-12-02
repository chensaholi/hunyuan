from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from utils import get_config


def create_session(config_file=None):
    # Create database session
    if config_file:
        db_url = get_config("DB", "DB_URL")
        pool_recycle = int(get_config("DB", "POOL_RECYCLE"))
        pool_size = int(get_config("DB", "POOL_SIZE"))
        max_overflow = int(get_config("DB", "MAX_OVERFLOW"))
        pool_pre_ping = get_config("DB", "POOL_PRE_PING")
    else:
        db_url = "mysql+mysqlconnector://root:root@139.9.126.27:3306/hunyuan"
        pool_recycle = 3600
        pool_size = 20
        max_overflow = 60
        pool_pre_ping = "True"
    if "True" in pool_pre_ping:
        pool_pre_ping = True
    else:
        pool_pre_ping = False
    engine = create_engine(db_url,
                           pool_recycle=pool_recycle,
                           pool_size=pool_size,
                           max_overflow=max_overflow,
                           pool_pre_ping=pool_pre_ping)
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    return session
