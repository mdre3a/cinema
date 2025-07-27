from sqlalchemy.orm.session import Session
from app.models.user import User
from app.core.security import get_password_hash


def update(db: Session):
    date_format = "%Y-%m-%d %H:%M:%S"
    _id = 0
    users = [
        User(id=(_id := _id + 1), email='admin@localdemo.com', hashed_password=get_password_hash("123"), name="Administrator", role="admin"),
        User(id=(_id := _id + 1), email='user@localdemo.com', hashed_password=get_password_hash("123"), name="User", role="user")
    ]
    db.bulk_save_objects(users)
