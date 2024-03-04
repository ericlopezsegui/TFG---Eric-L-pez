from sqlalchemy import Date, create_engine, Column, Integer, String, Sequence, Time, ForeignKey, DateTime, LargeBinary, PrimaryKeyConstraint
from sqlalchemy.orm import relationship, declarative_base
import mysql.connector

Base = declarative_base()

class Camp (Base):
    __tablename__ = 'camp'
    id_camp = Column(Integer, Sequence('camp_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    id_ubicacio = Column(Integer, ForeignKey('ubicacio.id_ubicacio'), nullable=False)
    ubicacio = relationship('Ubicacio', back_populates='camps')
    partits = relationship('Partit', back_populates='camp')
    
class Classificacio(Base):
    __tablename__ = 'classificacio'
    id_grup = Column(Integer, ForeignKey('grup.id_grup', name='fk_classificacio_grup_id'), primary_key=True)
    id_equip = Column(Integer, ForeignKey('equip.id_equip', name='fk_classificacio_equip_id'), primary_key=True)
    victories = Column(Integer, nullable=False)
    empats = Column(Integer, nullable=False)
    derrotes = Column(Integer, nullable=False)
    punts = Column(Integer, nullable=False)
    
    equip = relationship('Equip', back_populates='classificacio')
    grup = relationship('Grup', back_populates='classificacio')

    __table_args__ = (
        PrimaryKeyConstraint('id_grup', 'id_equip'),
        {},
    )

class Equip (Base):
    __tablename__ = 'equip'
    id_equip = Column(Integer, Sequence('equip_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    escut = Column(LargeBinary, nullable=False)
    id_grup = Column(Integer, ForeignKey('grup.id_grup'), nullable=False)
    id_torneig = Column(Integer, ForeignKey('torneig.id_torneig'), nullable=False)
    classificacio = relationship('Classificacio', back_populates='equip')
    grup = relationship('Grup', back_populates='equips')
    torneig = relationship('Torneig', back_populates='equips')
    jugadors = relationship('Jugador', back_populates='equip')
    partits1 = relationship('Partit', foreign_keys='[Partit.id_equip1]', back_populates='equip1')
    partits2 = relationship('Partit', foreign_keys='[Partit.id_equip2]', back_populates='equip2')

class Gol (Base):
    __tablename__ = 'gol'
    id_gol = Column(Integer, Sequence('gol_id_seq'), primary_key=True, autoincrement=True)
    minut = Column(Time, nullable=False)
    id_partit = Column(Integer, ForeignKey('partit.id_partit'), nullable=False)
    id_jugador = Column(Integer, ForeignKey('jugador.id_jugador'), nullable=False)
    partit = relationship('Partit', back_populates='gols')
    jugador = relationship('Jugador', back_populates='gols')

class Grup (Base):
    __tablename__ = 'grup'
    id_grup = Column(Integer, Sequence('grup_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    num_equips = Column(Integer, nullable=False)
    id_torneig = Column(Integer, ForeignKey('torneig.id_torneig'), nullable=False)
    torneig = relationship('Torneig', back_populates='grups')
    equips = relationship('Equip', back_populates='grup')
    partits = relationship('Partit', back_populates='grup')
    classificacio = relationship('Classificacio', back_populates='grup')
    
class Jugador (Base):
    __tablename__ = 'jugador'
    id_jugador = Column(Integer, Sequence('jugador_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    data_naixement = Column(Date, nullable=False)
    dorsal = Column(Integer, nullable=False)
    id_equip = Column(Integer, ForeignKey('equip.id_equip'), nullable=False)
    equip = relationship('Equip', back_populates='jugadors')
    gols = relationship('Gol', back_populates='jugador')
    sancions = relationship('Sancio', back_populates='jugador')

class Partit (Base):
    __tablename__ = 'partit'
    id_partit = Column(Integer, Sequence('partit_id_seq'), primary_key=True, autoincrement=True)
    data = Column(DateTime, nullable=False)
    hora = Column(Time, nullable=False)
    resultat = Column(String(50), nullable=False)
    id_equip1 = Column(Integer, ForeignKey('equip.id_equip'), nullable=False)
    id_equip2 = Column(Integer, ForeignKey('equip.id_equip'), nullable=False)
    gols_equip1 = Column(Integer, nullable=False)
    gols_equip2 = Column(Integer, nullable=False)
    id_grup = Column(Integer, ForeignKey('grup.id_grup'), nullable=False)
    id_personal = Column(Integer, ForeignKey('personal.id_personal'), nullable=False)
    id_camp = Column(Integer, ForeignKey('camp.id_camp'), nullable=False)
    equip1 = relationship('Equip', foreign_keys=[id_equip1], back_populates='partits1')
    equip2 = relationship('Equip', foreign_keys=[id_equip2], back_populates='partits2') 
    grup = relationship('Grup', back_populates='partits')
    personal = relationship('Personal', back_populates='partits')
    camp = relationship('Camp', back_populates='partits')
    gols = relationship('Gol', back_populates='partit')
    sancions = relationship('Sancio', back_populates='partit')

class Personal (Base):
    __tablename__ = 'personal'
    id_personal = Column(Integer, Sequence('personal_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    carrec = Column(String(50), nullable=False)
    id_torneig = Column(Integer, ForeignKey('torneig.id_torneig'), nullable=False)
    torneig = relationship('Torneig', back_populates='personal')
    partits = relationship('Partit', back_populates='personal')

class Sancio (Base):
    __tablename__ = 'sancio'
    id_jugador = Column(Integer, ForeignKey('jugador.id_jugador'), primary_key=True)
    id_partit = Column(Integer, ForeignKey('partit.id_partit'), primary_key=True)
    targeta_groga = Column(Integer, nullable=False)
    targeta_vermella = Column(Integer, nullable=False)
    doble_targeta_groga = Column(Integer, nullable=False)
    jugador = relationship('Jugador', back_populates='sancions')
    partit = relationship('Partit', back_populates='sancions')

class Torneig (Base):
    __tablename__ = 'torneig'
    id_torneig = Column(Integer, Sequence('torneig_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    data_inici = Column(Date, nullable=False)
    data_fi = Column(Date, nullable=False)
    fase = Column(String(50), nullable=False)
    id_ubicacio = Column(Integer, ForeignKey('ubicacio.id_ubicacio'), nullable=False)
    ubicacio = relationship('Ubicacio', back_populates='torneigs')
    personal = relationship('Personal', back_populates='torneig')

class Ubicacio (Base):
    __tablename__ = 'ubicacio'
    id_ubicacio = Column(Integer, Sequence('ubicacio_id_seq'), primary_key=True, autoincrement=True)
    nom = Column(String(50), nullable=False)
    adreca = Column(String(50), nullable=False)
    ciutat = Column(String(50), nullable=False)
    provincia = Column(String(50), nullable=False)
    pais = Column(String(50), nullable=False)
    codi_postal = Column(Integer, nullable=False)
    camps = relationship('Camp', back_populates='ubicacio')
    torneigs = relationship('Torneig', back_populates='ubicacio')
    
# CREACIÓ DE LA BASE DE DADES

usuari = 'root'
password = 'root'
host = 'localhost'
port = '3306'
Base_name = 'Database_torneig'

# Connexió al servidor MySQL
conexion_mysql = mysql.connector.connect(user=usuari, password=password, host=host, port=port)

# Crea la base de dades en cas que no existeixi
cursor = conexion_mysql.cursor()
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Base_name}")
cursor.close()

# Tanca la connexió al servidor MySQL
conexion_mysql.close()

# Crear el motor de la base de dades i crear les taules
url_de_conexion = f'mysql+mysqlconnector://{usuari}:{password}@{host}:{port}/{Base_name}'
engine = create_engine(url_de_conexion, echo=True)
Base.metadata.create_all(engine)