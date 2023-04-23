from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter
from fastapi import Request
from dto.user_dto import CreateUserResponse, CreateUserCommand, SearchUsersResponse, SearchUsersCommand, \
    FetchUserResponse
from response import responses
from services.user_service import UserService

user_router = InferringRouter(tags=["users"], responses=responses)
base_path = "/user"

@cbv(user_router)
class UserRouter(UserService):

    @user_router.post(base_path, response_model=CreateUserResponse)
    async def create(self, command: CreateUserCommand)-> CreateUserResponse:
        return await self.create_user(command)

    @user_router.post(base_path + "/search", response_model=SearchUsersResponse)
    async def search(self,command: SearchUsersCommand) -> SearchUsersResponse:
        return await self.search_users(command)

    @user_router.get(base_path + "/{id}", response_model=FetchUserResponse)
    async def search(self, id: str) -> FetchUserResponse:
        return await self.fetch_user(id)
