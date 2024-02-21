from app import db

class Camp(db.Model):
    id_camp = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50))

    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'))
    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'))
                          
    def __repr__(self):
        return '<Camp: %r' % self.nom