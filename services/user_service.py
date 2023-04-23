from core.user_core import UserCore
from dto.generic_dto import SearchResult
from dto.user_dto import CreateUserCommand, CreateUserResponse, UserState, SearchUsersResponse, SearchUsersCommand, \
    SearchUsersState
from models.user import UserModel
from util.date_util import DateUtil
from util.util import Util


class UserService(UserCore):

    async def create_user(self, command: CreateUserCommand)->CreateUserResponse:
        user = UserModel(_id=Util().generate_random_id())
        user.name = command.name
        user.email = command.email
        user.active = True
        user.created_at = DateUtil().get_current_timestamp()
        await self.save_user(user)
        return CreateUserResponse(
            status_code = 200,
            data = self.convert_to_user_state(user)
        )

    async def search_users(self, command: SearchUsersCommand)->SearchUsersResponse:
        search_result: SearchResult = await self._search_users(command)
        # users_list = []
        # for user in search_result.records:
        #     users_list.append(self.convert_to_user_state(user))

        search_users_state: SearchUsersState = SearchUsersState(
            total = search_result.total,
            results = search_result.records
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