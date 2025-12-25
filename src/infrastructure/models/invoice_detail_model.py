from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Numeric
from sqlalchemy.orm import relationship
from infrastructure.databases.base import Base
from datetime import datetime
class InvoiceDetail(Base):
    __tablename__ = 'invoice_detail'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    invoice_id=Column(Integer, ForeignKey("invoices.id"),nullable=False) # chi tiết hóa đơn bán
    product_unit_id=Column(Integer,ForeignKey("product_unit.id"),nullable=False) # Sản phẩm giá theo đơn vị
    vat=Column(Integer,nullable=False)
    discount=Column(Integer, nullable=True) 
    price=Column(Numeric(10), nullable=True)
    description = Column(String(255), nullable=True)
    quantity=Column(Integer,nullable=False)
    status = Column(String(50), nullable=False)  # Draft / Confirm / Delete 
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 
    