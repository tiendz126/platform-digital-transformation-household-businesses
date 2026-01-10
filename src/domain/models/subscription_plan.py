# src/domain/models/subscription_plan.py

from typing import Optional
from datetime import datetime

class SubscriptionPlan:
    def __init__(
        self,
        id: Optional[int],
        name: str,
        price: float,
        duration_days: int,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None
    ):
        self.id = id
        self.name = name
        self.price = price
        self.duration_days = duration_days
        self.created_at = created_at or datetime.utcnow()
        self.updated_at = updated_at or datetime.utcnow()

    def update(self, name: Optional[str] = None, price: Optional[float] = None, duration_days: Optional[int] = None):
        """Cập nhật thông tin plan"""
        if name is not None:
            self.name = name
        if price is not None:
            self.price = price
        if duration_days is not None:
            self.duration_days = duration_days
        self.updated_at = datetime.utcnow()
