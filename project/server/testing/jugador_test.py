from app import db

class Jugador(db.Model):
    id_jugador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), unique=True)
    cognom = db.Column(db.String(50), unique=True)
    dorsal = db.Column(db.Integer)
    data_naixement = db.Column(db.Date)

    id_equip = db.Column(db.Integer, db.ForeignKey('equip.id_equip'))
    
    def __repr__(self):
        return '<Jugador: %r' % self.id_jugador