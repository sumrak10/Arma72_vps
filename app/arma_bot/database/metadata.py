from typing import Any, Dict

from sqlalchemy.types import JSON
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase


class Base(AsyncAttrs, DeclarativeBase):
    # pass
    type_annotation_map = {
        Dict[str, Any]: JSON
    }
