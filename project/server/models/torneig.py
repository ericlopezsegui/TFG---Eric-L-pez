from app import db

class Torneig(db.Model):
    id_torneig = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), unique=True)
    data_inici = db.Column(db.Date)
    data_final = db.Column(db.Date)
    fase = db.Column(db.String(50))

    id_ubicacio = db.Column(db.Integer, db.ForeignKey('ubicacio.id_ubicacio'))

    def __repr__(self):
        return '<Torneig: %r' % self.id_torneig
    