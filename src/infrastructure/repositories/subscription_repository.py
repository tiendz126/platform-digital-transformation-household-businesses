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
        finally:
            self.session.close()

    def get_by_id(self, subscription_id: int) -> Optional[SubscriptionModel]:
        return self.session.query(SubscriptionModel).filter_by(id=subscription_id).first()

    def list(self) -> List[SubscriptionModel]:
        return self.session.query(SubscriptionModel).all()

    def update(self, subscription: SubscriptionModel) -> SubscriptionModel:
        try:
            sub_model = SubscriptionModel(
                id=subscription.id,
                plan_id=subscription.plan_id,
                household_id=subscription.household_id,
                start_date=subscription.start_date,
                end_date=subscription.end_date,
                is_active=subscription.is_active,
                created_at=subscription.created_at,
                updated_at=subscription.updated_at
            )
            self.session.merge(sub_model)
            self.session.commit()
            self.session.refresh(sub_model)
            return sub_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Error updating subscription: {str(e)}")
        finally:
            self.session.close()

    def delete(self, subscription_id: int) -> None:
        try:
            sub_model = self.session.query(SubscriptionModel).filter_by(id=subscription_id).first()
            if sub_model:
                self.session.delete(sub_model)
                self.session.commit()
            else:
                raise ValueError("Subscription not found")
        except Exception as e:
            self.session.rollback()
            raise ValueError(f"Error deleting subscription: {str(e)}")
        finally:
            self.session.close()

    def get_by_household_id(self, household_id: int) -> Optional[SubscriptionModel]:
        return self.session.query(SubscriptionModel).filter_by(
            household_id=household_id,
            is_active=True
        ).first()
