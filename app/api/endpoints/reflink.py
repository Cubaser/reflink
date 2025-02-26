from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.validators import (check_reflink_validate,
                                create_reflink_validate,
                                user_reflink_validate,
                                user_validate)
from app.core.config import settings
from app.core.db import get_async_session
from app.core.user import current_user
from app.crud.reflink import reflink_crud
from app.crud.user import user_crud
from app.models import User
from app.schemas.user import UserRead


router = APIRouter()


@router.post('/create',)
async def create_reflink(
        session: AsyncSession = Depends(get_async_session),
        user: User = Depends(current_user)
):
    """
    Только для зарегистрированных пользователей.
    Создание реферальной ссылки.
    """
    await create_reflink_validate(user, session)
    new_link = await reflink_crud.create_reflink(user, session)
    return {
        'message': 'Реферальный код создан',
        'ref_code': new_link.ref_code
    }


@router.delete('/delete')
async def delete_reflink(
    user: User = Depends(current_user),
    session: AsyncSession = Depends(get_async_session)
):
    """
    Только для зарегистрированных пользователей.
    Удаление реферальной ссылки.
    """
    referral_link = await reflink_crud.get_reflink_by_user_id(user, session)

    await check_reflink_validate(referral_link)
    await reflink_crud.remove(referral_link, session)
    return {'message': 'Реферальный код удалён'}


@router.get('/by-email/{email}')
async def get_by_email(
    email: str,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает реферальную ссылку по email адресу.
    """
    user = await user_crud.get_user_by_email(email, session)
    await user_validate(user)
    await user_reflink_validate(user)
    full_link = f'{settings.domain}/auth/register/{user.reflink.ref_code}'
    return {
        'message': 'Реферальнная ссылка',
        'ref_link': full_link
    }


@router.get(
    '/users/{user_id}',
    response_model=list[UserRead]
)
async def get_referrals(
    user_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    """
    Возвращает список рефералов по id.
    """
    user = await user_crud.get(user_id, session)
    await user_validate(user)
    users = await user_crud.get_ref_milti(user.id, session)
    return users
