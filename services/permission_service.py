from core.permission_core import PermissionCore
from dto.generic_dto import ActionResult
from dto.permission_dto import CreatePermissionCommand, PermissionResponse, PermissionState, \
    UpdatePermissionByUserIdOrgIdCommand, UpdatePermissionByIdCommand
from models.permissions import PermissionModel
from util.date_util import DateUtil
from util.exceptions.application_exception import ApplicationException
from util.util import Util


class PermissionService(PermissionCore):

    async def create_permission(self, command: CreatePermissionCommand)->PermissionResponse:
        if await self._check_user_org_exists_or_not(user_id=command.user_id, org_id=command.org_id):
            permission = await self._fetch_permission_by_user_id_org_id(user_id=command.user_id, org_id=command.org_id)
            if permission is None:
                permission = PermissionModel(_id=Util().generate_random_id())
                permission.user_id = command.user_id
                permission.org_id = command.org_id
                permission.type = command.type
                permission.created_at = DateUtil().get_current_timestamp()
                await self._save_permission(permission)
                return PermissionResponse(
                    status_code = 200,
                    data = self.convert_to_permission_state(permission)
                )
            else:
                return PermissionResponse(
                    status_code = 200,
                    data = self.convert_to_permission_state_by_json_response(permission)
                )
        else:
            raise ApplicationException(status_code=400, message="User or Org not found")

    async def update_permission_by_user_id_org_id(self, command: UpdatePermissionByUserIdOrgIdCommand)->PermissionResponse:
        permission = await self._fetch_permission_by_user_id_org_id(user_id=command.user_id, org_id=command.org_id)
        if permission is not None:
            permission = self.convert_to_permission_state_by_json_response(permission)
            permission.type = command.type
            permission.updated_at = DateUtil().get_current_timestamp()
            await self._update_permission(permission)
            return PermissionResponse(
                status_code = 200,
                data = permission
            )
        else:
            raise ApplicationException(status_code=404, message="Permission not found")

    async def update_permission_by_id(self, permission_id: str, command: UpdatePermissionByIdCommand)->PermissionResponse:
        permission = await self._fetch_permission_by_id(permission_id)
        if permission is not None:
            permission = self.convert_to_permission_state_by_json_response(permission)
            permission.type = command.type
            permission.updated_at = DateUtil().get_current_timestamp()
            await self._update_permission(permission)
            return PermissionResponse(
                status_code = 200,
                data = permission
            )
        else:
            raise ApplicationException(status_code=404, message="Permission not found")

    async def remove_permission_by_id(self, permission_id: str)->ActionResult:
        await self._remove_permission_by_id(permission_id)
        return ActionResult(
                    status_code = 200,
                    data = True
        )

    async def remove_permission_by_user_id_org_id(self, org_id: str, user_id: str)->ActionResult:
        await self._remove_permission_by_user_id_org_id(user_id=user_id, org_id=org_id)
        return ActionResult(
                    status_code = 200,
                    data = True
        )

    def convert_to_permission_state(self, permission: PermissionModel)-> PermissionState:
        state = PermissionState(
            permission_id=permission.permission_id,
            user_id = permission.user_id,
            org_id = permission.org_id,
            type = permission.type,
            created_at = permission.created_at,
            updated_at = permission.updated_at
        )
        return state

    def convert_to_permission_state_by_json_response(self, permission: dict)-> PermissionState:
        state = PermissionState(
            permission_id = permission["_id"],
            user_id=permission["userId"],
            org_id=permission["orgId"],
            type=permission["type"],
            created_at=permission["createdAt"],
            updated_at=permission["updatedAt"]
        )
        return state
