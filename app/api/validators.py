from datetime import datetime
from http import HTTPStatus

from fastapi import HTTPException
from sqlalchemy.future import select

from app.models import RefLink


async def check_reflink_validate(referral_link):

    if referral_link is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Реферальная ссылка не найдена.'
        )


async def reflink_expires_at_validate(referral_link):

    if referral_link.expires_at < datetime.now():
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='Истек действия срок реферальной ссылки.'
        )


async def create_reflink_validate(user, session):

    result = await session.execute(
        select(RefLink).where(RefLink.user_id == user.id)
    )
    existing_link = result.scalars().first()

    if existing_link:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail='У вас уже есть актуальный реферальный код.'
        )


async def user_reflink_validate(user):

    if not user.reflink:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='У пользователя нет реферального кода.'
        )
    if user.reflink.expires_at < datetime.now():
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Истек действия срок реферальной ссылки.'
        )


async def user_validate(user):

    if not user:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Пользователь не найден.'
        )
