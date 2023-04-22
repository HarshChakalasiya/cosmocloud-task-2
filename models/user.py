from odmantic import Model, Field


class UserModel(Model):
    userId: str = Field(default=None, primary_field=True, alias="_id")
    name: str = Field(default=None, index=True)
    email: str = Field(default=None)
    active: bool = Field(default=False)
    createdAt: str = Field(default=None)

    class Config:
        collection = "users"