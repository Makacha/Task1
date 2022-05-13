from typing import Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from app.models import Base
from app.db import db

ModelType = TypeVar("ModelType", bound=Base)
CreateType = TypeVar("CreateType", bound=BaseModel)
UpdateType = TypeVar("UpdateType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateType, UpdateType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_by_field(self, field=None, value=None):
        if value is None:
            return db.query(self.model).first()
        return db.query(self.model).filter(field == value).first()

    def get_all(self, field=None, value=None):
        if value is None:
            return db.query(self.model).all()
        return db.query(self.model).filter(field == value).all()

    def exist(self, id: int) -> bool:
        return self.get(id) is not None

    def create(self, data: CreateType) -> Type[ModelType]:
        obj_in = jsonable_encoder(data)
        obj = self.model(**obj_in)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, id: int) -> bool:
        db.query(self.model).filter(self.model.id == id).delete()
        db.commit()
        return True
