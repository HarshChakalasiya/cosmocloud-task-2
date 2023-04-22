from enum import Enum
from typing import Optional, List

from odmantic import Field, Model, Index


class PermissionType(int, Enum):
    READ = 0
    READ_WRITE = 1
    WRITE = 2
    ADMIN = 3

class PermissionModel(Model):
    userId: str = Field(default=None)
    role: PermissionType = Field(default=None)

class OrganisationModel(Model):
    orgId: str = Field(default=None, alias="_id", primary_field=True)
    name: str = Field(default=None, unique=True, index=True)
    permissions: List[PermissionModel] = Field(default=None)

    class Config:
        collection = "organisations"