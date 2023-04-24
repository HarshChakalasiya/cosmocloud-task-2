from core.user_core import UserCore
from dto.generic_dto import SearchResult
from dto.user_dto import CreateUserCommand, UserState, SearchUsersResponse, SearchUsersCommand, \
    SearchUsersState, UserResponse
from models.user import UserModel
from util.date_util import DateUtil
from util.exceptions.application_exception import ApplicationException
from util.util import Util


class UserService(UserCore):

    async def create_user(self, command: CreateUserCommand)->UserResponse:
        user = UserModel(_id=Util().generate_random_id())
        user.name = command.name
        user.email = command.email
        user.active = True
        user.created_at = DateUtil().get_current_timestamp()
        await self._save_user(user)
        return UserResponse(
            status_code = 200,
            data = self.convert_to_user_state(user)
        )

    async def fetch_user(self, id: str)->UserResponse:
        user = await self._get_user_by_id(id)
        if user is not None:
            return UserResponse(
                status_code = 200,
                data = self.convert_to_user_state_by_json(user)
            )
        else:
            raise ApplicationException(status_code=404, message="User not found")

    async def search_users(self, command: SearchUsersCommand)->SearchUsersResponse:
        search_result: SearchResult = await self._search_users(command)
        users_list = []
        for user in search_result.records:
            users_list.append(self.convert_to_user_state_by_json(user))

        search_users_state: SearchUsersState = SearchUsersState(
            total = search_result.total,
            results = users_list
        )
        return SearchUsersResponse(
            status_code= 200,
            data = search_users_state
        )

    def convert_to_user_state(self, user: UserModel)-> UserState:
        state = UserState(
            user_id = user.user_id,
            name = user.name,
            email = user.email,
            active = user.active,
            created_at = user.created_at
        )
        return state

    def convert_to_user_state_by_json(self, user: dict)-> UserState:
        state = UserState(
            user_id=user["_id"],
            name=user["name"],
            email=user["email"],
            active=user["active"],
            created_at=user["createdAt"]
        )
        return state
