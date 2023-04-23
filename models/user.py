from odmantic import Model, Field


class UserModel(Model):
    user_id: str = Field(default=None, primary_field=True, alias="_id")
    name: str = Field(default=None, index=True)
    email: str = Field(default=None)
    active: bool = Field(default=False)
    created_at: int = Field(default=None, key_name="createdAt")

    class Config:
        collection = "users"