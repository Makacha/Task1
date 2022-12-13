from app.crud import crud_category
from app.models import Category
from app.util import MyException
from app.schemas import CategoryInfo


class CategoryService:

    @classmethod
    def get_category(cls, category_id: int, db=None) -> Category:
        category = crud_category.get(db, category_id)
        if category is None:
            raise MyException(3, "Category doesn't exist")
        return category

    @classmethod
    def get_all_category(cls, parent_id: int = None, db=None):
        if parent_id is not None:
            return crud_category.get_all(db, Category.parent_id, parent_id)
        return crud_category.get_all(db)

    @classmethod
    def create_category(cls, category: CategoryInfo, db=None) -> Category:
        if crud_category.exist(db, category.id):
            raise MyException(4, "Category was created")
        if category.parent_id is not None and not crud_category.exist(db, category.parent_id):
            raise MyException(3, "Category doesn't exist")
        return crud_category.create(db, category)

    @classmethod
    def update_category(cls, category: CategoryInfo, db=None) -> Category:
        if not crud_category.exist(db, category.id):
            raise MyException(3, "Category doesn't exist")
        if category.parent_id is not None:
            if not crud_category.exist(db, category.parent_id):
                raise MyException(3, "Category doesn't exist")
            if crud_category.loops(db, category.parent_id, category.id):
                raise MyException(6, "The child category can't be parent")
        if category.name is not None:
            db.query(Category).filter(Category.id == category.id). \
                update({"name": category.name})
        if category.parent_id is not None:
            db.query(Category).filter(Category.id == category.id). \
                update({"parent_id": category.parent_id})
        db.commit()
        return crud_category.get(db, category.id)

    @classmethod
    def delete_category(cls, category_id: int, db=None):
        if not crud_category.exist(db, category_id):
            raise MyException(3, "Category doesn't exist")
        crud_category.delete(db, category_id)
