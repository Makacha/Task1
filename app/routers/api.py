from fastapi import APIRouter
from app.routers.endpoints import item, category, list, timestamp

router = APIRouter()


router.include_router(item.router, prefix="/item", tags=["item"])
router.include_router(category.router, prefix="/category", tags=["category"])
router.include_router(list.router, prefix="/list", tags=["list"])
router.include_router(timestamp.router, prefix="/timestamp", tags=["timestamp"])
