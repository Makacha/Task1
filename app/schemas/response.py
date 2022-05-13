from pydantic import BaseModel
from pydantic.generics import GenericModel
from typing import Generic, TypeVar

T = TypeVar("T")


class ResponseSchema(BaseModel):
    code: int = 0
    message: str = ""

    def success(self):
        self.code = 0
        self.message = "success"
        return self

    def fail(self, code: int, message: str):
        self.code = code
        self.message = message
        return self


class DataResponseSchema(ResponseSchema, GenericModel, Generic[T]):
    data: T

    def success(self, data: T):
        self.code = 0
        self.message = "success"
        self.data = data
        return self

    def fail(self, code: int, message: str, data: T):
        self.code = code
        self.message = message
        self.data = data
        return self
