from app import db

class Ubicacio(db.Model):
    id_ubicacio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ciutat= db.Column(db.String(50))
    provincia = db.Column(db.String(50))
    codi_postal = db.Column(db.Integer)
    
    def __repr__(self):
        return '<Ubicacio: %r' % self.id_ubicacio