from typing import Optional, List

from dto.generic_dto import ResponseState
from models.permissions import PermissionType
from util.base_model import BaseModel


class PermissionState(BaseModel):
    permission_id: str
    user_id: str
    org_id: str
    type: PermissionType = PermissionType.READ
    created_at: int
    updated_at: Optional[int]

class CreatePermissionCommand(BaseModel):
    user_id: str = None
    org_id: str = None
    type: PermissionType


class UpdatePermissionByUserIdOrgIdCommand(BaseModel):
    user_id: str = None
    org_id: str = None
    type: PermissionType

class UpdatePermissionByIdCommand(BaseModel):
    type: PermissionType

class PermissionResponse(ResponseState):
    data: Optional[PermissionState] = None

class DeletePermissionCommand(BaseModel):
    user_id: str = None
    org_id: str = None
