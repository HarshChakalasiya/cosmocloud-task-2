from typing import Optional, List

from pydantic import validator

from dto.generic_dto import ResponseState
from util.base_model import BaseModel
from util.validator import Validator


class UserState(BaseModel):
    user_id: str
    name: str
    email: str
    active: bool = False
    created_at: int

class CreateUserCommand(BaseModel):
    name: str = None
    email: str = None

    @validator('email')
    def email_validator(cls, value):
        return Validator().email_validator(value)


class CreateUserResponse(ResponseState):
    data: Optional[UserState] = None


class SearchUsersFilterCommand(BaseModel):
    name: Optional[str] = None


class SearchUsersCommand(BaseModel):
    page: int = 0
    records: int = 0
    filter: Optional[SearchUsersFilterCommand]


class SearchUsersState(BaseModel):
    total: Optional[int] = 0
    results: List[dict] = []


class SearchUsersResponse(ResponseState):
    data: Optional[SearchUsersState]