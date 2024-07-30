from litebase.core.model import Model
from litebase.core.flask import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship


class Field(Model):
    __tablename__ = '_fields'

    # Custom fields
    name: Mapped[str] = mapped_column(nullable=False)

    # Parent
    collection_id: Mapped[str] = mapped_column(
        ForeignKey('_collections.id'), 
        nullable=False,
    )

    collection = relationship('Collection', back_populates='fields')