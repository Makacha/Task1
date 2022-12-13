from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import ItemCreate, ItemUpdate, ResponseSchema, DataResponseSchema
from app.services import ItemService
from app.db import get_db

router = APIRouter()


@router.get("/{item_id}", response_model=DataResponseSchema[ItemCreate])
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = ItemService.get_item(item_id, db)
    return DataResponseSchema().success(item)


@router.post("/", response_model=DataResponseSchema[ItemCreate])
def create_item(item: ItemCreate, db: Session = Depends(get_db)):
    new_item = ItemService.create_item(item, db)
    return DataResponseSchema().success(new_item)


@router.put("/", response_model=DataResponseSchema[ItemCreate])
def update_item(item: ItemUpdate, db: Session = Depends(get_db)):
    item_upd = ItemService.update_item(item, db)
    return DataResponseSchema().success(item_upd)


@router.delete("/{item_id}", response_model=ResponseSchema)
def delete_item(item_id: int, db: Session = Depends(get_db)):
    ItemService.delete_item(item_id, db)
    return ResponseSchema().success()
