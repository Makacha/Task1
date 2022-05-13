from fastapi import APIRouter
from app.schemas import ItemCreate, ItemUpdate, ResponseSchema, DataResponseSchema
from app.services import ItemService

router = APIRouter()


@router.get("/{item_id}")
def read_item(item_id: int):
    item = ItemService.get_item(item_id)
    return DataResponseSchema().success(item)


@router.post("/")
def create_item(item: ItemCreate):
    new_item = ItemService.create_item(item)
    return DataResponseSchema().success(new_item)


@router.put("/")
def update_item(item: ItemUpdate):
    item_upd = ItemService.update_item(item)
    return DataResponseSchema().success(item_upd)


@router.delete("/{item_id}")
def delete_item(item_id: int):
    ItemService.delete_item(item_id)
    return ResponseSchema().success()
