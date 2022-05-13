from fastapi import APIRouter
from app.schemas import CategoryInfo, DataResponseSchema, ResponseSchema
from app.crud import crud_category
from app.services import CategoryService

router = APIRouter()


@router.get("/{category_id}")
def read_category(category_id: int):
    category = CategoryService.get_category(category_id)
    return DataResponseSchema().success(category)


@router.post("/")
def create_category(category: CategoryInfo):
    new_category = CategoryService.create_category(category)
    return DataResponseSchema().success(new_category)


@router.put("/")
def update_category(category: CategoryInfo):
    category_upd = CategoryService.update_category(category)
    return DataResponseSchema().success(category_upd)


@router.delete("/{category_id}")
def delete_category(category_id: int):
    CategoryService.delete_category(category_id)
    return ResponseSchema().success()
