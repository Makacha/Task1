from app.crud import crud_item, crud_category
from app.models import Item
from app.schemas import ItemCreate, ItemUpdate
from app.util import MyException
from app.db import db


class ItemService:

    @classmethod
    def get_item(cls, item_id: int) -> Item:
        item = crud_item.get(item_id)
        if item is None:
            raise MyException(1, "Item doesn't exist")
        return item

    @classmethod
    def get_all_item(cls, category_id: int = None):
        if category_id is not None:
            return crud_item.get_all(Item.category_id, category_id)
        return crud_item.get_all()

    @classmethod
    def create_item(cls, item: ItemCreate) -> Item:
        if crud_item.exist(item.id):
            raise MyException(2, "Item was created")
        if not crud_category.exist(item.category_id):
            raise MyException(3, "Category doesn't exist")
        return crud_item.create(item)

    @classmethod
    def update_item(cls, item: ItemUpdate) -> Item:
        if not crud_item.exist(item.id):
            raise MyException(1, "Item doesn't exist")
        if item.category_id is not None and not crud_category.exist(item.category_id):
            raise MyException(3, "Category doesn't exist")
        if item.name is not None:
            db.query(Item).filter(Item.id == item.id).update({"name": item.name})
        if item.price is not None:
            db.query(Item).filter(Item.id == item.id).update({"price": item.price})
        if item.category_id is not None:
            db.query(Item).filter(Item.id == item.id).update({"category_id": item.category_id})
        db.commit()
        return crud_item.get(item.id)

    @classmethod
    def delete_item(cls, item_id: int):
        if not crud_item.exist(item_id):
            raise MyException(1, "Item doesn't exist")
        crud_item.delete(item_id)
