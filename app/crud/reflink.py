from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import RefLink, User


class CRUDRefLink(CRUDBase):

    async def create_reflink(
            self,
            user: User,
            session: AsyncSession,
    ) -> RefLink:
        obj_in = {
            'user_id': user.id
        }
        db_obj = self.model(**obj_in)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def get_reflink_by_link(
            self,
            ref_code: str,
            session: AsyncSession,
    ) -> RefLink:
        result = await session.execute(
            select(self.model).filter(self.model.ref_code == ref_code)
        )
        referral_link = result.scalars().first()
        return referral_link

    async def get_reflink_by_user_id(
            self,
            user: User,
            session: AsyncSession,
    ) -> RefLink:
        result = await session.execute(
            select(self.model).where(self.model.user_id == user.id)
        )
        referral_link = result.scalars().first()
        return referral_link

    async def get_reflink_by_email(
            self,
            email: str,
            session: AsyncSession,
    ) -> RefLink:
        result = await session.execute(
            select(User).where(User.email == email)
        )
        referral_link = result.scalars().first()
        return referral_link


reflink_crud = CRUDRefLink(RefLink)
