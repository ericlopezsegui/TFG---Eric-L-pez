from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask'

db = SQLAlchemy(app)

from routes import app as routes_app

from models.torneig import Torneig
from models.personal import Personal
from models.jugador import Jugador
from models.equip import Equip
from models.ubicacio import Ubicacio
from models.arbit import Arbit
from models.partit import Partit
from models.administradors import Administradors
from models.classificació import Classificacio
from models.gol import Gol
from models.grup import Grup
from models.sancions import Sancions
from models.camp import Camp

if __name__ == '__main__':
    app.run(debug=True)