from litebase.core.flask import app

@app.route('/schema')
def _schema():
    
    return {
        'schema': {},
    }