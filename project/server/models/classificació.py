from app import db

class Classificacio(db.Model):
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup'), primary_key=True ,autoincrement=True)
    id_equip = db.Column(db.Integer, db.ForeignKey('equip.id_equip'), primary_key=True ,autoincrement=True)
    
    victories = db.Column(db.Integer)
    empats = db.Column(db.Integer)
    derrotes = db.Column(db.Integer)
    punts = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Classificacio: %r' % self.id_grup