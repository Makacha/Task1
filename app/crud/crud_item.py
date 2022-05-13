from app.models import Item
from app.crud import CRUDBase
from app.schemas import ItemUpdate, ItemCreate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):

    pass


crud_item = CRUDItem(Item)
