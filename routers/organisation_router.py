from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

from dto.organisation_dto import OrganisationResponse, CreateOrganisationCommand, SearchOrganisationsResponse, \
    SearchOrganisationsCommand
from response import responses
from services.organisation_service import OrganisationService

organisation_router = InferringRouter(tags=["organisations"], responses=responses)
base_path = "/organisation"

@cbv(organisation_router)
class OrganisationRouter(OrganisationService):

    @organisation_router.post(base_path, response_model=OrganisationResponse)
    async def create(self, command: CreateOrganisationCommand)-> OrganisationResponse:
        return await self.create_organisation(command)

    @organisation_router.post(base_path + "/search", response_model=SearchOrganisationsResponse)
    async def search(self, command: SearchOrganisationsCommand) -> SearchOrganisationsResponse:
        return await self.search_organisations(command)
