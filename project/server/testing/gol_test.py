from app import db

class Gol(db.Model):
    id_gol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    minut = db.Column(db.Integer)

    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'))
    id_jugador = db.Column(db.Integer, db.ForeignKey('jugador.id_jugador'))

    def __repr__(self):
        return '<Gol: %r' % self.id_gol