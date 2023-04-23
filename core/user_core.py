from config.database import nosql_engine
from dto.generic_dto import SearchResult
from dto.user_dto import SearchUsersCommand
from models.user import UserModel
from util.config import params


class UserCore:
    def __init__(self):
        self.db_engine = nosql_engine
        self.__user_collection = nosql_engine.get_collection(UserModel)

    async def _save_user(self, user_model: UserModel):
        await self.db_engine.save(user_model)
        return

    async def _get_user_by_id(self, user_id: str):
        user = await self.__user_collection.find_one({"_id": user_id})
        return user

    async def _search_users(self, command: SearchUsersCommand) -> SearchResult:
        filters = await self.__search_users_filter(command)
        total = await self.__user_collection.count_documents(filters)
        users = await self.__search_users_pagination(command, filters)
        return SearchResult(
            total = total,
            records = users
        )

    async def __search_users_filter(self, command: SearchUsersCommand):
        _filter = {}
        if command.filter is not None:
            if command.filter.name is not None and command.filter.name != "":
                _filter[+UserModel.name] = command.filter.name

        return _filter


    async def __search_users_pagination(self, command: SearchUsersCommand, filter: dict):
        pages = ((command.page - 1) * command.records) if command.page != 0 and command.page is not None else 0
        records = command.records if command.records != 0 else int(params.max_msg_count)
        results = []
        result = self.__user_collection.find(filter).skip(pages).limit(records)
        for user in await result.to_list(length=records):
            results.append(user)
        return results
