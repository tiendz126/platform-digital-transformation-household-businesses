from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from infrastructure.databases.base import Base
from datetime import datetime
class InvoiceDetail(Base):
    __tablename__ = 'invoice_detail'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    invoice_id=Column(Integer, ForeignKey("invoices.id"),nullable=True) # Hóa đơn mua
    product_unit_id=Column(Integer,ForeignKey("product_unit.id"),nullable=True) # Hóa đơn bán
    discount_total=Column(Integer,nullable=True)
    vat=Column(Integer,nullable=False)
    discount=Column(Integer, nullable=False) 
    price=Column(Integer, nullable=True)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)  # Draft / Confirm / Delete 
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 