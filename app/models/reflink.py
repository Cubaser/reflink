from datetime import datetime, timedelta
from uuid import uuid4

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class RefLink(Base):
    user_id = Column(
        String,
        ForeignKey('user.id'),
        nullable=False,
        unique=True
    )
    ref_code = Column(String, unique=True, default=lambda: str(uuid4()))
    expires_at = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now() + timedelta(days=7)
    )

    user = relationship('User', back_populates='reflink')
