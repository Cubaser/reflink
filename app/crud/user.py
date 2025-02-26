from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.base import CRUDBase
from app.models import User


class CRUDUser(CRUDBase):

    async def get_user_by_email(
            self,
            email: str,
            session: AsyncSession,
    ) -> User:
        result = await session.execute(
            select(self.model)
            .options(selectinload(self.model.reflink))
            .where(self.model.email.ilike(email))
        )
        user = result.scalars().first()
        return user

    async def get_ref_milti(
            self,
            user_id: int,
            session: AsyncSession,
    ) -> list[User]:
        users = await session.execute(
            select(self.model).where(self.model.referrer_id == user_id))
        users = users.scalars().all()
        return users


user_crud = CRUDUser(User)
