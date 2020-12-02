from database.session import create_session
from database.models import User


session = create_session()


def get_users():
    user_info = []
    try:
        res = session.query(User).all()
        for user in res:
            temp_dict = {
                "user_id": user.user_id,
                "user_name": user.user_name,
                "user_type": user.user_type,
                "user_pwd": user.user_pwd,
                "create_time": user.create_time
            }
            user_info.append(temp_dict)
    except Exception as e:
        print("query db error: %s" % e)
    finally:
        session.remove()
        return {"result": user_info}


def create_user(user_name, user_pwd, user_type):
    try:
        res = session.query(User.user_id).filter_by(user_name=user_name).one_or_none()
        if res:
            return "current name is exists"
        user = User(user_name=user_name, user_pwd=user_pwd, user_type=user_type)
        session.add(user)
        session.commit()
        return 0
    except Exception as e:
        session.rollback()
        msg = "query db error: %s" % e
        return msg
    finally:
        session.remove()

