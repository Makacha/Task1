from pydantic import BaseModel, validator
from app.util import MyException


class ItemInfo(BaseModel):
    id: int
    name: str = None
    price: float = None

    @validator("price")
    def valid_price(cls, price):
        if price is not None and price < 0:
            raise MyException(5, "Price can't less than 0")
        return price


class ItemCreate(ItemInfo):
    category_id: int


class ItemUpdate(ItemInfo):
    category_id: int = None
