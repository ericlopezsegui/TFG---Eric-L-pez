from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig')

db = SQLAlchemy(app)

if __name__ == '__main__':
    from routes import configure_routes
    configure_routes(app)
    app.run(debug=True)