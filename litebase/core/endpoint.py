import json


from flask import request, Response
from litebase.core.flask import app, db
from litebase.core.model import Model

class Endpoint:
    """
    Provides basic endpoint functionality for the API.
    """

    def __init__(self, path, model, *args, **kwargs):
        """
        Initializes the endpoint.
        
        :param path: path of the endpoint
        :type path: str

        :param model: model of the endpoint
        :type model: type
        """

        self.path = path
        self.model = model

        self._register()

    def _register(self):
        """
        Registers the endpoint routes
        """

        # CRUD endpoints
        app.add_url_rule(self.path, view_func=self.create, methods=['POST'])
        app.add_url_rule(f'{self.path}/<id>', view_func=self.read, methods=['GET'])
        app.add_url_rule(f'{self.path}/<id>', view_func=self.update, methods=['PATCH'])
        app.add_url_rule(f'{self.path}/<id>', view_func=self.delete, methods=['DELETE'])
        
        # List/search endpoint
        app.add_url_rule(self.path, view_func=self.search, methods=['GET'])

    def create(self):
        """
        Creates a resouce.
        """

        # Creates a model instance
        model: Model = self.model(**request.json)

        try:

            # Saves or updates the resouce
            return Response(
                response=json.dumps(model.create().to_dict()), 
                status=201,
                mimetype='application/json',
            )
        
        except Exception as e:

            # Returns an error response
            return Response(
                response=json.dumps({'error': str(e)}), 
                status=400,
                mimetype='application/json',
            )

    def read(self, id):
        """
        Reads the resouce.

        :param id: ID of the resouce.
        :type id: str
        """

        model: Model = self.model()

        try:

            return Response(
                response=json.dumps(model.fetch(
                    id=id,
                    expand=request.args.get('expand', '').split(','),
                ).to_dict()), 
                status=200,
                mimetype='application/json',
            )
        
        except Exception as e:

            # Returns an error response
            return Response(
                response=json.dumps({'error': str(e)}), 
                status=400,
                mimetype='application/json',
            )

    def update(self, id):
        """
        Updates the resouce.
        """

        model: Model = self.model(id=id)

        try:    

            return Response(
                response=json.dumps(model.update(request.json).to_dict()), 
                status=200,
                mimetype='application/json',
            )

        except Exception as e:

            return Response(
                response=json.dumps({'error': str(e)}), 
                status=400,
                mimetype='application/json',
            )

    def delete(self, id):
        """
        Deletes the resouce.
        """

        # Gets the resouce
        instance = self.model.query.get(id)

        # Deletes the resouce
        db.session.delete(instance)

        # Commits the changes
        db.session.commit()

        return {}

    def search(self):
        """
        Searches the resouce.
        """

        # List all the resouces
        return [
            instance.to_dict() for instance in self.model.query.all()
        ]
