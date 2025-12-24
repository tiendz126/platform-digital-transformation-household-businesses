from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from infrastructure.databases.base import Base
from datetime import datetime
class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    household_id=Column(Integer, ForeignKey("households.id"),nullable=True) # Admin không cần tham chiếu tới hộ kinh doanh
    user_name=Column(String(18),nullable=False,unique=True)
    password = Column(String(18), nullable=False)
    email= Column(String(100),nullable=True,unique=True)
    role= Column(String(50),nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_by= Column(String(50),nullable=True)# Role Admin or Owner
    updated_by= Column(String(50),nullable=True)# Role Admin or Owner
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 