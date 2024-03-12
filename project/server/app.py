from http.client import HTTPException
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db_config import Config, Testing, Development, Production

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Development)

db.init_app(app)

class validationError (HTTPException):
    code = 400
    description = 'Validation Error'

@app.errorhandler(validationError)
def handleValidationError(e):
    response = jsonify({'eroor': e.Description})
    response.status_code = e.code
    return response

@app.errorhandler(Exception)
def unexpectedError (error):
    response = jsonify({'message':'An unexpected error occurred {}'.format(error)})
    response.status_code = 500
    return response

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
