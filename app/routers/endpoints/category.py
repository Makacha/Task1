from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import CategoryInfo, DataResponseSchema, ResponseSchema
from app.crud import crud_category
from app.services import CategoryService
from app.db import get_db

router = APIRouter()


@router.get("/{category_id}", response_model=DataResponseSchema[CategoryInfo])
def read_category(category_id: int, db: Session = Depends(get_db)):
    category = CategoryService.get_category(category_id, db)
    return DataResponseSchema().success(category)


@router.post("/", response_model=DataResponseSchema[CategoryInfo])
def create_category(category: CategoryInfo, db: Session = Depends(get_db)):
    new_category = CategoryService.create_category(category, db)
    return DataResponseSchema().success(new_category)


@router.put("/", response_model=DataResponseSchema[CategoryInfo])
def update_category(category: CategoryInfo, db: Session = Depends(get_db)):
    category_upd = CategoryService.update_category(category, db)
    return DataResponseSchema().success(category_upd)


@router.delete("/{category_id}", response_model=ResponseSchema)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    CategoryService.delete_category(category_id, db)
    return ResponseSchema().success()
