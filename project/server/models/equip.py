from app import db

class Equip(db.Model):
    id_equip = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), unique=True)
    escut = db.Column(db.blob)

    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'))
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup'))
    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'))

    def __repr__(self):
        return '<Equip: %r' % self.id_equip
