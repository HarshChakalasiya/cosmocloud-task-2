from enum import Enum

from odmantic import Field, Model


class PermissionType(int, Enum):
    READ = 0
    WRITE = 1
    ADMIN = 2

class PermissionModel(Model):
    permission_id: str = Field(primary_field=True, alias="_id")
    user_id: str = Field(default=None, key_name="userId", index=True)
    org_id: str = Field(default=None, key_name="orgId", index=True)
    type: PermissionType = Field(default=None)
    created_at: int = Field(default=None, key_name="createdAt")
    updated_at: int = Field(default=None, key_name="updatedAt")

    class Config:
        collection = "permissions"