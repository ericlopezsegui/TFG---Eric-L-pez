from app import db

class Personal(db.Model):
    id_personal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))
    cognom = db.Column(db.String(50))
    carrec = db.Column(db.String(100))

    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'))
    id_arbit = db.Column(db.Integer, db.ForeignKey('arbit.id_arbit'))

    def __repr__(self):
        return '<Personal: %r' % self.id_personal