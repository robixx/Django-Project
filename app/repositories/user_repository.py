

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate
from datetime import datetime

class UserRepository:

    def create_user(self, db: Session, user: UserCreate):
        db_user = User(name=user.name, email=user.email, password=user.password, IsActive=1)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user

    def get_users(self, db: Session):
        return db.query(User).all()

    def get_user_by_id(self, db: Session, user_id: int):
        return db.query(User).filter(User.id == user_id).first()

    def update_user(self, db: Session, user_id: int, name: str, email: str):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            user.name = name
            user.email = email
            db.commit()
            db.refresh(user)
        return user

    def delete_user(self, db: Session, user_id: int):
        user = db.query(User).filter(User.id == user_id).first()
        if user:
            db.delete(user)
            db.commit()
        return user