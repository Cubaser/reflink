from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import backref, relationship

from app.core.db import Base


class User(SQLAlchemyBaseUserTable[int], Base):
    reflink = relationship(
        'RefLink',
        back_populates='user',
        uselist=False
    )
    referrer_id = Column(Integer, ForeignKey('user.id'), nullable=True)
    referrer = relationship(
        'User',
        remote_side='User.id',
        backref=backref('referrals', lazy='dynamic')
    )
