from config.database import nosql_engine
from dto.generic_dto import SearchResult
from dto.organisation_dto import SearchOrganisationsCommand
from models.organisation import OrganisationModel
from util.config import params


class OrganisationCore:
    def __init__(self):
        self.db_engine = nosql_engine
        self.__org_collection = nosql_engine.get_collection(OrganisationModel)

    async def _save_org(self, org_model: OrganisationModel):
        await self.db_engine.save(org_model)
        return

    async def _check_org_exists_or_not(self, org_name: str):
        org = await self.__org_collection.find_one({"name": org_name})
        return True if org is not None else False

    async def _search_orgs(self, command: SearchOrganisationsCommand) -> SearchResult:
        filters = await self.__search_orgs_filter(command)
        total = await self.__org_collection.count_documents(filters)
        orgs = await self.__search_orgs_pagination(command, filters)
        return SearchResult(
            total = total,
            records = orgs
        )

    async def __search_orgs_filter(self, command: SearchOrganisationsCommand):
        _filter = {}
        if command.filter is not None:
            if command.filter.name is not None and command.filter.name != "":
                _filter[+OrganisationModel.name] = command.filter.name

        return _filter


    async def __search_orgs_pagination(self, command: SearchOrganisationsCommand, filter: dict):
        pages = ((command.page - 1) * command.records) if command.page != 0 and command.page is not None else 0
        records = command.records if command.records != 0 else int(params.max_msg_count)
        results = []
        result = self.__org_collection.find(filter).skip(pages).limit(records)
        for org in await result.to_list(length=records):
            results.append(org)
        return results
