from typing import Optional

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    ...


class UserCreate(schemas.BaseUserCreate):
    ...


class UserRefCreate(schemas.BaseUserCreate):
    referrer_id: Optional[int] = None


class UserUpdate(schemas.BaseUserUpdate):
    ...
