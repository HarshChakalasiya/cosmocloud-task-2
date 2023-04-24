from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from dto.user_dto import UserResponse, CreateUserCommand, SearchUsersResponse, SearchUsersCommand
from response import responses
from services.user_service import UserService

user_router = InferringRouter(tags=["users"], responses=responses)
base_path = "/user"

@cbv(user_router)
class UserRouter(UserService):

    @user_router.post(base_path, response_model=UserResponse)
    async def create(self, command: CreateUserCommand)-> UserResponse:
        return await self.create_user(command)

    @user_router.post(base_path + "/search", response_model=SearchUsersResponse)
    async def search(self, command: SearchUsersCommand) -> SearchUsersResponse:
        return await self.search_users(command)

    @user_router.get(base_path + "/{id}", response_model=UserResponse)
    async def fetch(self, id: str) -> UserResponse:
        return await self.fetch_user(id)
