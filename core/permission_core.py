from config.database import nosql_engine
from dto.permission_dto import PermissionState
from models.organisation import OrganisationModel
from models.permissions import PermissionModel
from models.user import UserModel


class PermissionCore:
    def __init__(self):
        self.db_engine = nosql_engine
        self.__permission_collection = nosql_engine.get_collection(PermissionModel)
        self.__user_collection = nosql_engine.get_collection(UserModel)
        self.__org_collection = nosql_engine.get_collection(OrganisationModel)

    async def _save_permission(self, permission_model: PermissionModel):
        await self.db_engine.save(permission_model)
        return

    async def _check_user_org_exists_or_not(self, user_id: str, org_id: str):
        user = await self.__user_collection.find_one({"_id": user_id})
        org = await self.__org_collection.find_one({"_id": org_id})
        return True if user is not None and org is not None else False

    async def _fetch_permission_by_id(self, permission_id: str):
        permission = await self.__permission_collection.find_one({"_id": permission_id})
        return permission

    async def _fetch_permission_by_user_id_org_id(self, user_id: str, org_id: str):
        permission = await self.__permission_collection.find_one({"userId": user_id, "orgId": org_id})
        return permission

    async def _remove_permission_by_user_id_org_id(self, user_id:str, org_id: str):
        await self.__permission_collection.delete_one({"userId": user_id, "orgId": org_id})
        return

    async def _remove_permission_by_id(self, permission_id:str):
        await self.__permission_collection.delete_one({"_id": permission_id})
        return

    async def _update_permission(self, permission: PermissionState):
        await self.__permission_collection.update_one(
            {"_id": permission.permission_id},
            {'$set': {"type": permission.type, "updatedAt": permission.updated_at}}
        )
        return
