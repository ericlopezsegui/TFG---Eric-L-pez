from flask_sqlalchemy import SQLAlchemy
from app import db

class Camp(db.Model):
    __tablename__ = 'camp'
    id_camp = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    id_ubicacio = db.Column(db.Integer, db.ForeignKey('ubicacio.id_ubicacio'), nullable=False)
    ubicacio = db.relationship('Ubicacio', back_populates='camps')
    partits = db.relationship('Partit', back_populates='camp')

class Classificacio(db.Model):
    __tablename__ = 'classificacio'
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup', name='fk_classificacio_grup_id'), primary_key=True)
    id_equip = db.Column(db.Integer, db.ForeignKey('equip.id_equip', name='fk_classificacio_equip_id'), primary_key=True)
    victories = db.Column(db.Integer, nullable=False)
    empats = db.Column(db.Integer, nullable=False)
    derrotes = db.Column(db.Integer, nullable=False)
    punts = db.Column(db.Integer, nullable=False)

    equip = db.relationship('Equip', back_populates='classificacio')
    grup = db.relationship('Grup', back_populates='classificacio')

class Equip(db.Model):
    __tablename__ = 'equip'
    id_equip = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    escut = db.Column(db.LargeBinary, nullable=False)
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup'), nullable=False)
    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'), nullable=False)
    classificacio = db.relationship('Classificacio', back_populates='equip')
    grup = db.relationship('Grup', back_populates='equips')
    torneig = db.relationship('Torneig', back_populates='equips')
    jugadors = db.relationship('Jugador', back_populates='equip')
    partits1 = db.relationship('Partit', foreign_keys='[Partit.id_equip1]', back_populates='equip1')
    partits2 = db.relationship('Partit', foreign_keys='[Partit.id_equip2]', back_populates='equip2')

class Gol(db.Model):
    __tablename__ = 'gol'
    id_gol = db.Column(db.Integer, primary_key=True, autoincrement=True)
    minut = db.Column(db.Time, nullable=False)
    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'), nullable=False)
    id_jugador = db.Column(db.Integer, db.ForeignKey('jugador.id_jugador'), nullable=False)
    partit = db.relationship('Partit', back_populates='gols')
    jugador = db.relationship('Jugador', back_populates='gols')

class Grup(db.Model):
    __tablename__ = 'grup'
    id_grup = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    num_equips = db.Column(db.Integer, nullable=False)
    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'), nullable=False)
    torneig = db.relationship('Torneig', back_populates='grups')
    equips = db.relationship('Equip', back_populates='grup')
    partits = db.relationship('Partit', back_populates='grup')
    classificacio = db.relationship('Classificacio', back_populates='grup')

class Jugador(db.Model):
    __tablename__ = 'jugador'
    id_jugador = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    cognom = db.Column(db.String(50), nullable=False)
    data_naixement = db.Column(db.Date, nullable=False)
    dorsal = db.Column(db.Integer, nullable=False)
    id_equip = db.Column(db.Integer, db.ForeignKey('equip.id_equip'), nullable=False)
    equip = db.relationship('Equip', back_populates='jugadors')
    gols = db.relationship('Gol', back_populates='jugador')
    sancions = db.relationship('Sancio', back_populates='jugador')

class Partit(db.Model):
    __tablename__ = 'partit'
    id_partit = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data = db.Column(db.DateTime, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    resultat = db.Column(db.String(50), nullable=False)
    id_equip1 = db.Column(db.Integer, db.ForeignKey('equip.id_equip'), nullable=False)
    id_equip2 = db.Column(db.Integer, db.ForeignKey('equip.id_equip'), nullable=False)
    gols_equip1 = db.Column(db.Integer, nullable=False)
    gols_equip2 = db.Column(db.Integer, nullable=False)
    id_grup = db.Column(db.Integer, db.ForeignKey('grup.id_grup'), nullable=False)
    id_personal = db.Column(db.Integer, db.ForeignKey('personal.id_personal'), nullable=False)
    id_camp = db.Column(db.Integer, db.ForeignKey('camp.id_camp'), nullable=False)
    equip1 = db.relationship('Equip', foreign_keys=[id_equip1], back_populates='partits1')
    equip2 = db.relationship('Equip', foreign_keys=[id_equip2], back_populates='partits2')    
    grup = db.relationship('Grup', back_populates='partits')
    personal = db.relationship('Personal', back_populates='partits')
    camp = db.relationship('Camp', back_populates='partits')
    gols = db.relationship('Gol', back_populates='partit')
    sancions = db.relationship('Sancio', back_populates='partit')

class Personal(db.Model):
    __tablename__ = 'personal'
    id_personal = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    cognom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    carrec = db.Column(db.String(50), nullable=False)
    id_torneig = db.Column(db.Integer, db.ForeignKey('torneig.id_torneig'), nullable=False)
    torneig = db.relationship('Torneig', back_populates='personal')
    partits = db.relationship('Partit', back_populates='personal')

class Sancio(db.Model):
    __tablename__ = 'sancio'
    id_jugador = db.Column(db.Integer, db.ForeignKey('jugador.id_jugador'), primary_key=True)
    id_partit = db.Column(db.Integer, db.ForeignKey('partit.id_partit'), primary_key=True)
    targeta_groga = db.Column(db.Integer, nullable=False)
    targeta_vermella = db.Column(db.Integer, nullable=False)
    doble_targeta_groga = db.Column(db.Integer, nullable=False)
    jugador = db.relationship('Jugador', back_populates='sancions')
    partit = db.relationship('Partit', back_populates='sancions')

class Torneig(db.Model):
    __tablename__ = 'torneig'
    id_torneig = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    data_inici = db.Column(db.Date, nullable=False)
    data_fi = db.Column(db.Date, nullable=False)
    fase = db.Column(db.String(50), nullable=False)
    id_ubicacio = db.Column(db.Integer, db.ForeignKey('ubicacio.id_ubicacio'), nullable=False)
    ubicacio = db.relationship('Ubicacio', back_populates='torneigs')
    personal = db.relationship('Personal', back_populates='torneig')
    equips = db.relationship('Equip', back_populates='torneig')
    grups = db.relationship('Grup', back_populates='torneig')

class Ubicacio(db.Model):
    __tablename__ = 'ubicacio'
    id_ubicacio = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nom = db.Column(db.String(50), nullable=False)
    adreca = db.Column(db.String(50), nullable=False)
    ciutat = db.Column(db.String(50), nullable=False)
    provincia = db.Column(db.String(50), nullable=False)
    pais = db.Column(db.String(50), nullable=False)
    codi_postal = db.Column(db.Integer, nullable=False)
    camps = db.relationship('Camp', back_populates='ubicacio')
    torneigs = db.relationship('Torneig', back_populates='ubicacio')
