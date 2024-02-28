from app import db

class Sancions(db.Model):
    id_jugador = db.Column(db.Integer, db.ForeignKey('jugador.id_jugador'), primary_key=True ,autoincrement=True)
    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'), primary_key=True ,autoincrement=True)

    targeta_groga = db.Column(db.Integer)
    doble_targeta_groga = db.Column(db.Integer)
    targeta_vermella = db.Column(db.Integer)

    def __repr__(self):
        return '<Sancions: %r' % self.id_jugador