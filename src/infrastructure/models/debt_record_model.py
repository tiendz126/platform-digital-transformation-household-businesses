from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base
from datetime import datetime
class DebtRecord(Base):
    __tablename__ = 'debt_record'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    invoice_id=Column(Integer, ForeignKey("invoices.id"),nullable=False,unique=True)
    debt_amount=Column(Numeric(10), nullable=False) # Số tiền nợ cho hóa đơn cụ thể
    paid_amount=Column(Numeric(10), nullable=True)  # Số tiền đã trả cho hóa đơn cụ thể
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 
    
    
