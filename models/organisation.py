from enum import Enum
from typing import Optional, List

from odmantic import Field, Model, Index


class OrganisationModel(Model):
    org_id: str = Field(alias="_id", primary_field=True)
    name: str = Field(default=None, unique=True, index=True)
    created_at: int = Field(default=None, key_name="createdAt")

    class Config:
        collection = "organisations"