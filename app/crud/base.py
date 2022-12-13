from typing import Generic, TypeVar, Type

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.models import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateType = TypeVar("CreateType", bound=BaseModel)
UpdateType = TypeVar("UpdateType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateType, UpdateType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.id == id).first()

    def get_by_field(self, db: Session, field=None, value=None):
        if value is None:
            return db.query(self.model).first()
        return db.query(self.model).filter(field == value).first()

    def get_all(self, db: Session, field=None, value=None):
        if value is None:
            return db.query(self.model).all()
        return db.query(self.model).filter(field == value).all()

    def exist(self, db: Session, id: int) -> bool:
        return self.get(db, id) is not None

    def create(self, db: Session, data: CreateType) -> Type[ModelType]:
        obj_in = jsonable_encoder(data)
        obj = self.model(**obj_in)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    def delete(self, db: Session, id: int) -> bool:
        db.query(self.model).filter(self.model.id == id).delete()
        db.commit()
        return True
