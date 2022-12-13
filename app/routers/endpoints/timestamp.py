from fastapi import APIRouter
from app.schemas import DataResponseSchema
from app.util import get_current_timestamp

router = APIRouter()


@router.get("/", response_model=DataResponseSchema[int])
def get_timestamp():
    return DataResponseSchema().success(get_current_timestamp())
