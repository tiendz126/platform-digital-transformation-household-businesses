from domain.models.isubscription_repository import ISubscriptionRepository
from domain.models.subscription import Subscription
from typing import List, Optional
from infrastructure.databases.mssql import session
from infrastructure.models.subscription_model import Subscription as SubscriptionModel
from sqlalchemy.orm import Session
from datetime import datetime

class SubscriptionRepository(ISubscriptionRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, subscription: Subscription) -> SubscriptionModel:
        """
        Thêm subscription mới
        """
        try:
            sub_model = SubscriptionModel(
                plan_id=subscription.plan_id,
                household_id=subscription.household_id,
                start_date=subscription.start_date,
                end_date=subscription.end_date,
                is_active=subscription.is_active,
                created_at=subscription.created_at,
                updated_at=subscription.updated_at
            )
            self.session.add(sub_model)
            self.session.commit()
            self.session.refresh(sub_model)
            return sub_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Error creating subscription: {str(e)}")

    def get_by_id(self, subscription_id: int) -> Optional[SubscriptionModel]:
        """
        Lấy subscription theo ID
        """
        return self.session.query(SubscriptionModel).filter_by(id=subscription_id).first()

    def list(self) -> List[SubscriptionModel]:
        """
        Lấy tất cả subscription
        """
        return self.session.query(SubscriptionModel).all()

    def update(self, subscription: SubscriptionModel) -> SubscriptionModel:
        """
        Cập nhật subscription
        """
        try:
            sub_model = self.get_by_id(subscription.id)
            if not sub_model:
                raise ValueError("Subscription not found")

            sub_model.plan_id = subscription.plan_id
            sub_model.household_id = subscription.household_id
            sub_model.start_date = subscription.start_date
            sub_model.end_date = subscription.end_date
            sub_model.is_active = subscription.is_active
            sub_model.updated_at = subscription.updated_at or datetime.utcnow()

            self.session.commit()
            self.session.refresh(sub_model)
            return sub_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Error updating subscription: {str(e)}")

    def delete(self, subscription_id: int) -> None:
        """
        Xóa subscription theo ID
        """
        try:
            sub_model = self.get_by_id(subscription_id)
            if not sub_model:
                raise ValueError("Subscription not found")
            self.session.delete(sub_model)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Error deleting subscription: {str(e)}")

    def get_by_household_id(self, household_id: int) -> Optional[SubscriptionModel]:
        """
        Lấy subscription active theo household_id
        """
        now = datetime.utcnow()
        return self.session.query(SubscriptionModel).filter(
            SubscriptionModel.household_id == household_id,
            SubscriptionModel.is_active == True,
            SubscriptionModel.end_date >= now
        ).first()
