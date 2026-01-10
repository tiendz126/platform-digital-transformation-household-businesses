"""
Subscription Service - Check household có subscription active và CRUD subscription
"""
from datetime import datetime
from infrastructure.databases.mssql import session
from infrastructure.models import Subscription  # path đúng với project

class SubscriptionService:
    def __init__(self, db_session=None):
        # Nếu không truyền session thì dùng mặc định
        self.session = db_session or session

    # ---------------- CHECK ----------------
    def check_household_subscription_active(self, household_id: int) -> bool:
        """Check household có subscription active không"""
        if not household_id:
            # Admin không cần check subscription
            return True
        
        subscription = self.session.query(Subscription).filter_by(
            household_id=household_id,
            is_active=True
        ).first()
        
        if not subscription:
            return False
        
        if subscription.end_date < datetime.utcnow():
            return False
        
        return True

    def get_active_subscription(self, household_id: int):
        """Lấy subscription active của household"""
        if not household_id:
            return None
        
        subscription = self.session.query(Subscription).filter_by(
            household_id=household_id,
            is_active=True
        ).first()
        
        if subscription and subscription.end_date >= datetime.utcnow():
            return subscription
        
        return None

    # ---------------- CREATE ----------------
    def create_subscription(
        self,
        household_id: int,
        plan_id: int,
        start_date: datetime,
        end_date: datetime,
        is_active: bool = True
    ):
        """Tạo subscription mới"""
        subscription = Subscription(
            household_id=household_id,
            plan_id=plan_id,
            start_date=start_date,
            end_date=end_date,
            is_active=is_active,
            created_at=datetime.utcnow(),
            updated_at=datetime.utcnow()
        )
        self.session.add(subscription)
        self.session.commit()
        self.session.refresh(subscription)
        return subscription

    # ---------------- LIST ----------------
    def list_subscriptions(self):
        """Lấy tất cả subscription"""
        return self.session.query(Subscription).all()

    # ---------------- GET BY ID ----------------
    def get_subscription(self, subscription_id: int):
        """Lấy subscription theo ID"""
        return self.session.query(Subscription).filter_by(id=subscription_id).first()

    # ---------------- UPDATE ----------------
    def update_subscription(
        self,
        subscription_id: int,
        household_id: int = None,
        plan_id: int = None,
        start_date: datetime = None,
        end_date: datetime = None,
        is_active: bool = None
    ):
        """Cập nhật subscription theo ID"""
        subscription = self.get_subscription(subscription_id)
        if not subscription:
            raise ValueError("Subscription not found")
        if household_id is not None:
            subscription.household_id = household_id
        if plan_id is not None:
            subscription.plan_id = plan_id
        if start_date is not None:
            subscription.start_date = start_date
        if end_date is not None:
            subscription.end_date = end_date
        if is_active is not None:
            subscription.is_active = is_active
        subscription.updated_at = datetime.utcnow()
        self.session.commit()
        return subscription

    # ---------------- DELETE ----------------
    def delete_subscription(self, subscription_id: int):
        """Xóa subscription theo ID"""
        subscription = self.get_subscription(subscription_id)
        if not subscription:
            raise ValueError("Subscription not found")
        self.session.delete(subscription)
        self.session.commit()
