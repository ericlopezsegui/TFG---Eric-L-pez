from app import db

class Grup(db.Model):
    id_grup = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(100), unique=True)
    nombre_equips = db.Column(db.Integer)

    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'))