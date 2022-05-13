from fastapi import APIRouter
from app.schemas import DataResponseSchema
from app.services import ItemService, CategoryService

router = APIRouter()


@router.get("/item")
def read_list_item():
    data = ItemService.get_all_item()
    return DataResponseSchema().success(data)


@router.get("/item/{category_id}")
def read_list_item(category_id: int):
    data = ItemService.get_all_item(category_id)
    return DataResponseSchema().success(data)


@router.get("/category")
def read_list_category():
    data = CategoryService.get_all_category()
    return DataResponseSchema().success(data)


@router.get("/category/{category_id}")
def read_list_category(parent_id: int):
    data = CategoryService.get_all_category(parent_id)
    return DataResponseSchema().success(data)
