from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from infrastructure.databases.base import Base
from datetime import datetime
class SubscriptionPlan(Base):
    __tablename__ = 'subscriptionplans'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id=Column(Integer, primary_key=True) # Cho phép NULL
    user_id=Column(Integer, ForeignKey("users.id"),nullable=False) # Role Admin
    billing_cycle=Column(String(50),nullable=True)
    price=Column(Integer, nullable=True)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_by= Column(String(50),nullable=True)
    updated_by= Column(String(50),nullable=True)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 