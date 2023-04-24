from core.organisation_core import OrganisationCore
from dto.generic_dto import SearchResult
from dto.organisation_dto import CreateOrganisationCommand, OrganisationResponse, OrganisationState, SearchOrganisationsCommand, SearchOrganisationsResponse, SearchOrganisationsState
from models.organisation import OrganisationModel
from util.date_util import DateUtil
from util.exceptions.application_exception import ApplicationException
from util.util import Util


class OrganisationService(OrganisationCore):

    async def create_organisation(self, command: CreateOrganisationCommand)->OrganisationResponse:
        if not await self._check_org_exists_or_not(command.name):
            org = OrganisationModel(_id=Util().generate_random_id())
            org.name = command.name
            org.created_at = DateUtil().get_current_timestamp()
            await self._save_org(org)
            return OrganisationResponse(
                status_code = 200,
                data = self.convert_to_org_state(org)
            )
        else:
            raise ApplicationException(status_code=403, message="Organisation Already Exist")

    async def search_organisations(self, command: SearchOrganisationsCommand)->SearchOrganisationsResponse:
        search_result: SearchResult = await self._search_orgs(command)
        orgs_list = []
        for org in search_result.records:
            orgs_list.append(self.convert_to_org_state_by_json_response(org))

        search_orgs_state: SearchOrganisationsState = SearchOrganisationsState(
            total = search_result.total,
            results = orgs_list
        )
        return SearchOrganisationsResponse(
            status_code= 200,
            data = search_orgs_state
        )

    def convert_to_org_state(self, org: OrganisationModel)-> OrganisationState:
        state = OrganisationState(
            org_id = org.org_id,
            name = org.name,
            created_at = org.created_at
        )
        return state

    def convert_to_org_state_by_json_response(self, org: dict)-> OrganisationState:
        state = OrganisationState(
            org_id=org["_id"],
            name=org["name"],
            created_at=org["createdAt"]
        )
        return state
