from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate

class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, db: Session, user: UserCreate):
        return self.repo.create_user(db, user)

    def get_users(self, db: Session):
        return self.repo.get_users(db)

    def get_user_by_id(self, db: Session, user_id: int):
        return self.repo.get_user_by_id(db, user_id)

    def update_user(self, db: Session, user_id: int, name: str, email: str):
        return self.repo.update_user(db, user_id, name, email)

    def delete_user(self, db: Session, user_id: int):
        return self.repo.delete_user(db, user_id)
