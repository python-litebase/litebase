from litebase.endpoints import *
from litebase.core.api.sockets import *

from litebase.core.flask import serve

def run(debug=False, *args, **kwargs):
    """
    Flask server runner.
    
    :param debug: Enable or disable debug mode.
    :type debug: bool, default False

    :param args: Additional arguments passed to the Flask app.
    :type args: tuple

    :param kwargs: Additional keyword arguments passed to the Flask app.
    :type kwargs: dict
    """

    serve(debug, *args, **kwargs)
