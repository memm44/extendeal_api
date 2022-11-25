from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from app.api.schemas.items.output_items import ItemRecords
from app.api.services.item import ItemService
from app.api.services.user import UserService

item_router = APIRouter(prefix="/items", tags=["Items"])


@item_router.get("", response_model=ItemRecords)
def get_items(__=Depends(UserService.get_current_username)):
    """
    Get items from ecommerce website https://www.disco.com.ar/electro/informatica
    :param __: verifies authentication
    :return: fresh items scrapped from webpage store.
    """
    result_dict_items = ItemService().get_items()
    if not result_dict_items:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Temporal error with the store webpage",
        )
    return result_dict_items
