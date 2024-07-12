from litebase.core.flask import serve
from litebase.core.api import *
from litebase.core.models import *

def run(debug=False, *args, **kwargs):

    serve(debug, *args, **kwargs)
