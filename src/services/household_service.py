from domain.models.household import Household
from domain.models.ihousehold_repository import IHouseholdRepository
from typing import List, Optional
from datetime import datetime

class HouseholdService:
    def __init__(self, repository: IHouseholdRepository):
        self.repository = repository

    def create_household(
        self,
        tax_code: Optional[str] = None,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> Household:
       
        creator = created_by if created_by is not None else "SYSTEM"
        updater = updated_by if updated_by is not None else "SYSTEM"
        
        household = Household(
            id=None,
            tax_code=tax_code,
            name=name,
            phone=phone,
            address=address,
            description=description,
            status=status,
            created_by=creator,
            updated_by=updater, 
            created_at=created_at,
            updated_at=updated_at,
        )
        return self.repository.add(household)

    def get_household(self, household_id: int) -> Optional[Household]:
        return self.repository.get_by_id(household_id)

    def list_households(self) -> List[Household]:
        return self.repository.list()

    def update_household(
        self,
        household_id: int,
        tax_code: Optional[str] = None,
        name: Optional[str] = None,
        phone: Optional[str] = None,
        address: Optional[str] = None,
        description: Optional[str] = None,
        status: Optional[str] = None,
        created_by: Optional[str] = None,
        updated_by: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> Household:
        
        existing_household = self.repository.get_by_id(household_id)
        
        if not existing_household:
            raise ValueError(f"Household with ID {household_id} not found.") 
        if tax_code is not None:
            existing_household.tax_code = tax_code
        if name is not None:
            existing_household.name = name
        if phone is not None:
            existing_household.phone = phone
        if address is not None:
            existing_household.address = address
        if description is not None:
            existing_household.description = description
        if status is not None:
            existing_household.status = status
        if updated_by is not None:
            existing_household.updated_by = updated_by
        if updated_at is not None:
            existing_household.updated_at = updated_at
        return self.repository.update(existing_household)

    def delete_household(self, household_id: int) -> None:
        self.repository.delete(household_id)