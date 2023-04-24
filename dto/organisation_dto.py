from typing import Optional, List

from pydantic import validator

from dto.generic_dto import ResponseState
from util.base_model import BaseModel
from util.validator import Validator


class OrganisationState(BaseModel):
    org_id: str
    name: str
    created_at: int

class CreateOrganisationCommand(BaseModel):
    name: str = None


class OrganisationResponse(ResponseState):
    data: Optional[OrganisationState] = None


class SearchOrganisationsFilterCommand(BaseModel):
    name: Optional[str] = None


class SearchOrganisationsCommand(BaseModel):
    page: int = 0
    records: int = 0
    filter: Optional[SearchOrganisationsFilterCommand]


class SearchOrganisationsState(BaseModel):
    total: Optional[int] = 0
    results: List[OrganisationState] = []


class SearchOrganisationsResponse(ResponseState):
    data: Optional[SearchOrganisationsState]