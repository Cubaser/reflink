from datetime import datetime

from pydantic import BaseModel


class RefLinkBase(BaseModel):
    user_id: str
    ref_code: str
    expires_at: datetime

    class Config:
        orm_mode = True


class RefLinkCreate(RefLinkBase):
    pass


class RefLinkRead(RefLinkBase):
    id: int
