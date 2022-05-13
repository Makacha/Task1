from pydantic import BaseModel


class CategoryInfo(BaseModel):
    id: int
    name: str = None
    parent_id: int = None
