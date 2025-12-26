from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from infrastructure.databases.base import Base
from datetime import datetime
class ImportDetail(Base):
    __tablename__ = 'import_detail'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    invoice_id=Column(Integer, ForeignKey("invoices.id"),nullable=False) # Chi tiết hóa đơn mua
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    unit_id=Column(Integer, ForeignKey("units.id"),nullable=False)
    quantity=Column(Integer,nullable=False)
    description = Column(String(255), nullable=True)
    status = Column(String(50), nullable=False)  # Draft / Confirm / Delete 
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False)
   