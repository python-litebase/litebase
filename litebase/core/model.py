import uuid

from collections import OrderedDict
from datetime import datetime, UTC
from litebase.core.flask import db
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.orm.collections import InstrumentedList

class Model(db.Model):

    __abstract__ = True

    # System fields
    id: Mapped[str] = mapped_column(primary_key=True)

    # Timestamps
    created: Mapped[datetime] = mapped_column()
    updated: Mapped[datetime] = mapped_column()

    def __init__(self, **data):
        """
        Sets the model attributes.
        """

        for key, value in data.items():

            if key in self._fields():

                setattr(self, key, value)

    def _fields(self):
        """
        Returns the model fields.
        """
        
        
        return [
            str(column.name) for column in self.__table__.columns
        ]
    
    def _relationships(self):
        """
        Returns the model relationships.
        """

        relationships = []

        for key in dir(self):

            value = getattr(self, key)

            # `many` children records
            if type(value) == InstrumentedList:

                relationships.append(key)

            # # Many-to-one relationships
            # if type(value) == DeclarativeBase:

            #     relationships.append(key)

            # # Many-to-many relationships
            # if type(value) == relationship:

            #     relationships.append(key)

        return relationships

    def to_dict(self):
        """
        Serializes the model to a dictionary.
        """

        response = OrderedDict({
            field: getattr(self, field) for field in self._fields()
        })

        # Translates datetime objects to strings
        for key, value in response.items():

            if isinstance(value, datetime):

                response[key] = value.isoformat(
                    timespec='milliseconds',
                )

        return response

    def fetch(self, id, expand=None):
        """
        Fetches a model instance by ID.

        :param id: ID of the model instance.
        :type id: str

        :param expand: Expands the model relationships.
        :type expand: list[str]
        """

        data = self.query

        # Joins the expanded fields
        # if expand is not None:

        #     for field in expand:

        #         data = data.join(field)

        data = data.get(id)

        if data is None:

            raise Exception(f'Resource with id `{id}` not found on collection `{self.__tablename__}`')

        for field in self._fields():

            # Gets the column type
            column = self.__table__.columns[field]

            match column.type:

                case 'DATETIME':

                    # Parses the datetime string
                    value = datetime.fromisoformat(value)

            setattr(self, field, getattr(data, field))

        del data

        return self

    def create(self):
        """
        Creates or updates the model instance.
        """

        # Factors a new ID
        self.id = str(uuid.uuid4().hex.replace('-', '').lower()[0:16])

        # Sets the created timestamp
        self.created = datetime.now(UTC)
        self.updated = self.created

        # Commit the changes
        db.session.add(self)
        db.session.commit()

        return self
    
    def update(self, data):
        """
        Updates the model instance.
        """

        if self.id is None:

            raise Exception('Resource does not have an ID')

        self.fetch(self.id)

        for key, value in data.items():

            if key in self._fields():

                setattr(self, key, value)

        # Updates the updated timestamp and clears the timezone
        self.updated = datetime.now(UTC).replace(tzinfo=None)

        # Commit the changes
        db.session.merge(self)
        db.session.commit()

        return self
    
