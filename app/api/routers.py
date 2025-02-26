from fastapi import APIRouter

from app.api.endpoints import reflink_router, user_router
from app.api.endpoints.user import custom_router

main_router = APIRouter()
main_router.include_router(
    reflink_router, prefix='/reflink', tags=['RefLink']
)
main_router.include_router(
    custom_router, prefix='/auth', tags=['auth']
)
main_router.include_router(user_router)
