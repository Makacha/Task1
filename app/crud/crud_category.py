from app.models import Category
from app.crud import CRUDBase
from app.schemas import CategoryInfo
from app.db import db
from app.util import MyException


class CRUDCategory(CRUDBase[Category, CategoryInfo, CategoryInfo]):

    def loops(self, parent_id: int, id: int) -> bool:
        parent_category = self.get(parent_id)
        while parent_category is not None:
            if parent_category.id == id:
                return True
            parent_category = self.get(parent_category.parent_id)
        return False


crud_category = CRUDCategory(Category)
