from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from dto.generic_dto import ActionResult
from dto.permission_dto import PermissionResponse, CreatePermissionCommand, UpdatePermissionCommand
from response import responses
from services.permission_service import PermissionService

permission_router = InferringRouter(tags=["permissions"], responses=responses)
base_path = "/permission"

@cbv(permission_router)
class PermissionRouter(PermissionService):

    @permission_router.post(base_path, response_model=PermissionResponse)
    async def create(self, command: CreatePermissionCommand)-> PermissionResponse:
        return await self.create_permission(command)

    @permission_router.put(base_path + "/update/{id}", response_model=PermissionResponse)
    async def update(self, id:str, command: UpdatePermissionCommand) -> PermissionResponse:
        return await self.update_permission_by_id(id, command)

    @permission_router.put(base_path + "/update/organisation/{org_id}/user/{user_id}", response_model=PermissionResponse)
    async def update_by_user_id_org_id(self, user_id: str, org_id: str, command: UpdatePermissionCommand) -> PermissionResponse:
        return await self.update_permission_by_user_id_org_id(user_id= user_id, org_id=org_id, command=command)

    @permission_router.delete(base_path + "/remove/{id}", response_model=ActionResult)
    async def remove(self, id: str) -> ActionResult:
        return await self.remove_permission_by_id(id)

    @permission_router.delete(base_path + "/remove/organisation/{org_id}/user/{user_id}", response_model=ActionResult)
    async def remove_by_user_id_org_id(self, org_id: str, user_id: str) -> ActionResult:
        return await self.remove_permission_by_user_id_org_id(user_id= user_id, org_id=org_id)
