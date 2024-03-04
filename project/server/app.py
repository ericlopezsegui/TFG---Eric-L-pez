from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/Database_torneig'

# Inicialización de la extensión SQLAlchemy con la aplicación
db.init_app(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
