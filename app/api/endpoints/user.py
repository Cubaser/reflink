from fastapi import APIRouter, Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_reflink_validate,
                                reflink_expires_at_validate)
from app.core.db import get_async_session
from app.core.user import UserManager, auth_backend, fastapi_users
from app.crud.reflink import reflink_crud
from app.models import User
from app.schemas.user import UserCreate, UserRead, UserRefCreate, UserUpdate


router = APIRouter()
custom_router = APIRouter()


@custom_router.post("/register/{ref_code}", response_model=UserRead)
async def register_user_with_referral(
    user_create: UserCreate,
    ref_code: str,
    session: AsyncSession = Depends(get_async_session)
):
    """Регистрация по реферальной ссылке"""
    referral_link = await reflink_crud.get_reflink_by_link(ref_code, session)
    await check_reflink_validate(referral_link)
    await reflink_expires_at_validate(referral_link)

    user_db = SQLAlchemyUserDatabase(session, User)
    user_manager = UserManager(user_db)

    user = await user_manager.create(
        UserRefCreate(
            email=user_create.email,
            password=user_create.password,
            is_active=user_create.is_active,
            is_superuser=user_create.is_superuser,
            is_verified=user_create.is_verified,
            referrer_id=referral_link.user_id
        )
    )

    return user

router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix='/auth/jwt',
    tags=['auth'],
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix='/auth',
    tags=['auth'],
)


users_router = fastapi_users.get_users_router(UserRead, UserUpdate)

users_router.routes = [
    rout for rout in users_router.routes if rout.name != 'users:delete_user'
]

router.include_router(
    users_router,
    prefix='/users',
    tags=['users'],
)
