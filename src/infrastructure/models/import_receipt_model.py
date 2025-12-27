from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from infrastructure.databases.base import Base
from datetime import datetime
class ImportReceipt(Base):
    __tablename__ = 'import_receipts'
    __table_args__ = {'extend_existing': True}  # Thêm dòng này

    id = Column(Integer, primary_key=True) # Cho phép NULL
    warehouse_id=Column(Integer, ForeignKey("warehouses.id"),nullable=False)
    created_at = Column(DateTime,default=datetime.utcnow,nullable=False)
    import_date=Column(Date,nullable=False )
    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,nullable=False) 
    
   