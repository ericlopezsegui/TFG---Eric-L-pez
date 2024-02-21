from app import db

class Administradors(db.Model):
    id_administrador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))
    cognom = db.Column(db.String(50))
    email = db.Column(db.String(150))
    password = db.Column(db.String(250))

    id_personal = db.Column(db.Integer, db.ForeignKey('personal.id_personal'))
    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'))

    def __repr__(self):
        return '<Administradors: %r' % self.nom