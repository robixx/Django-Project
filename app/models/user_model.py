
from sqlalchemy import Column, Integer, String,DateTime
from datetime import datetime
from app.core.database import Base

class User(Base):
    __tablename__ = "users"  # existing table name

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    createDate = Column("createdate", DateTime, default=datetime.now)  # local time
    IsActive = Column("isactive", Integer, default=1)       
