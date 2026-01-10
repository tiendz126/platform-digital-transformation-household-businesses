from domain.models.ihousehold_repository import IHouseholdRepository
from domain.models.household import Household
from typing import List, Optional
from infrastructure.models.household_model import Household as HouseholdModel
from infrastructure.databases.mssql import session
from sqlalchemy.orm import Session
from datetime import datetime

class HouseholdRepository(IHouseholdRepository):
    def __init__(self, session: Session = session):
        self.session = session

    def add(self, household: Household) -> HouseholdModel:
        try:
            household_model = HouseholdModel(
            name=household.name,
            address=household.address,
            status=household.status or 'active',
            tax_code=household.tax_code,
            phone=household.phone,
            description=household.description,
            created_by=household.created_by or "system",
            updated_by=household.updated_by or "system", 
            created_at=household.created_at or datetime.utcnow(),
            updated_at=household.updated_at or datetime.utcnow()
        )
            self.session.add(household_model)
            self.session.commit()
            self.session.refresh(household_model)
            return household_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error creating household: {str(e)}')
        finally:
            self.session.close()

    def get_by_id(self, household_id: int) -> Optional[HouseholdModel]:
        try:
            return self.session.query(HouseholdModel).filter_by(id=household_id).first()
        finally:
            self.session.close()

    def list(self) -> List[HouseholdModel]:
        try:
            return self.session.query(HouseholdModel).all()
        finally:
            self.session.close()

    def update(self, household: Household) -> HouseholdModel:
        try:
            household_model = self.session.query(HouseholdModel).filter_by(id=household.id).first()
            if not household_model:
                raise ValueError('Household not found')

            if household.name is not None:
                household_model.name = household.name
            if household.address is not None:
                household_model.address = household.address
            household_model.updated_at = household.updated_at or datetime.utcnow()

            self.session.commit()
            self.session.refresh(household_model)
            return household_model
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error updating household: {str(e)}')
        finally:
            self.session.close()

    def delete(self, household_id: int) -> None:
        try:
            household_model = self.session.query(HouseholdModel).filter_by(id=household_id).first()
            if household_model:
                self.session.delete(household_model)
                self.session.commit()
            else:
                raise ValueError('Household not found')
        except Exception as e:
            self.session.rollback()
            raise ValueError(f'Error deleting household: {str(e)}')
        finally:
            self.session.close()
