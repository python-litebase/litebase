from litebase.core.model import Model
from litebase.core.flask import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from litebase.models.fields import Field

class Collection(Model):
    __tablename__ = '_collections'

    # Custom fields
    name = db.Column(db.String, nullable=False)

    # Fields relationship
    fields = relationship('Field', back_populates='collection')
