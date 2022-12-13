from app.models import Category
from app.crud import CRUDBase
from app.schemas import CategoryInfo
from app.util import MyException
from sqlalchemy.orm import Session


class CRUDCategory(CRUDBase[Category, CategoryInfo, CategoryInfo]):

    def loops(self, db: Session, parent_id: int, id: int) -> bool:
        parent_category = self.get(db, parent_id)
        while parent_category is not None:
            if parent_category.id == id:
                return True
            parent_category = self.get(db, parent_category.parent_id)
        return False


crud_category = CRUDCategory(Category)
