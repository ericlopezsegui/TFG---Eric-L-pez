from app import db

class Partit(db.Model):
    id_partit = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_partit = db.Column(db.Date)
    hora_partit = db.Column(db.Time)
    resultat = db.Column(db.String(50))
    gols_equip1 = db.Column(db.Integer)
    gols_equip2 = db.Column(db.Integer)
    id_equip1 = db.Column(db.Integer, db.ForeignKey('equip.id_equip'))
    id_equip2 = db.Column(db.Integer, db.ForeignKey('equip.id_equip'))
    id_arbitre = db.Column(db.Integer, db.ForeignKey('arbitre.id_arbitre'))
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup'))

    def __repr__(self):
        return '<Partit: %r' % self.id_partit