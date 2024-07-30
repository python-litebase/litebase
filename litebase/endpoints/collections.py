from litebase.core.endpoint import Endpoint
from litebase.models.collection import Collection

# Creates a new endpoint for the collections.
collections = Endpoint('/collections', Collection)
