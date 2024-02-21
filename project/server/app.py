from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flask'
db = SQLAlchemy(app)

from project.server.models.torneig import Torneig
from project.server.models.personal import Personal
from project.server.models.jugador import Jugador
from project.server.models.equip import Equip
from project.server.models.ubicacio import Ubicacio
from project.server.models.arbit import Arbit
from project.server.models.partit import Partit
from project.server.models.administradors import Administradors
from project.server.models.classificació import Classificacio
from project.server.models.gol import Gol
from project.server.models.grup import Grup
from project.server.models.sancions import Sancions
from project.server.models.camp import Camp

if __name__ == '__main__':
    app.run(debug=True)

