from fastapi import APIRouter
from seedwork.infrastructure.request_context import request_context

from modules.catalog.module import CatalogModule
from modules.catalog.application.command.create_listing_draft import (
    CreateListingDraftCommand,
)
from modules.catalog.application.query.get_all_listings import GetAllListings
from modules.catalog.application.query.get_listing_details import GetListingDetails
from config.container import Container, inject
from api.models import ListingReadModel, ListingWriteModel, ListingIndexModel
from api.shared import dependency

router = APIRouter()


@router.get("/items", tags=['items'], response_model=ItemIndexModel)
@router.post("/items", tags=['items'], response_model=ItemReadModel)
@inject
async def create_item(
    request_body: ListingWriteModel,
    module: CatalogModule = dependency(Container.catalog_module)
):
    """Creates a new Item"""

    command_result = module.execute_command()
