from sqlalchemy import Date, create_engine, Column, Integer, String, Sequence, Time, ForeignKey, DateTime, LargeBinary
from sqlalchemy.orm import relationship, declarative_base
import mysql.connector

Base = declarative_base()

class Arbit(Base):
    __tablename__ = 'Arbit'
    id_arbit = Column(Integer, Sequence('id_arbit_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(250), nullable=False)

    # CLAUS FORANIES
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))

    # RELACIONS
    torneig = relationship("Torneig", back_populates="arbit")

class Torneig(Base):
    __tablename__ = 'Torneig'
    id_torneig = Column(Integer, Sequence('id_torneig_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    data_inici = Column(Date, nullable=False)
    data_final = Column(Date, nullable=False)
    fase = Column(String(50), nullable=False)

    # CLAUS FORANIES
    id_ubicacio = Column(Integer, ForeignKey('Ubicació.id_ubicacio'))

    # RELACIONS
    ubicacio = relationship("Ubicació", back_populates="torneig")

class Partit(Base):
    __tablename__ = 'Partit'
    id_partit = Column(Integer, Sequence('id_partit_seq'), primary_key=True, autoincrement=True, nullable=False)
    data_partit = Column(Date, nullable=False)
    hora_partit = Column(Time, nullable=False)
    resultat = Column(String(50),  nullable=False)
    gols_equip1 = Column(Integer, nullable=False)
    gols_equip2 = Column(Integer, nullable=False)
    id_equip1 = Column(Integer, nullable=False)
    id_equip2 = Column(Integer, nullable=False)
   
    # CLAUS FORANIES
    id_arbit = Column(Integer, ForeignKey('Arbit.id_arbit'))
    id_grup = Column(Integer, ForeignKey('Grup.id_grup'))

    # RELACIONS
    arbit = relationship("Arbit", back_populates="partit")
    equip1 = relationship("Equip", foreign_keys=[id_equip1]
                          , backref="equip1")
    equip2 = relationship("Equip", foreign_keys=[id_equip2]
                            , backref="equip2")
    grup = relationship("Torneig", back_populates="partit")

class Camp(Base):
    __tablename__ = 'Camp'
    id_camp = Column(Integer, Sequence('id_camp_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)

    # CLAUS FORANIES
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))
    id_partit = Column(Integer, ForeignKey('Partit.id_partit'))

    # RELACIONS
    torneig = relationship("Torneig", back_populates="camp")
    partit = relationship("Partit", back_populates="camp")

class Administradors(Base):
    __tablename__ = 'Administradors'
    id_administrador = Column(Integer, Sequence('id_administrador_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    email = Column(String(150), nullable=False)
    password = Column(String(250), nullable=False)

    # CLAUS FORANIES
    id_personal = Column(Integer, ForeignKey('Personal.id_personal'))
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))

    # RELACIONS
    personal = relationship("Personal", back_populates="administradors")
    torneig = relationship("Torneig", back_populates="administradors")

class Personal(Base):
    __tablename__ = 'Personal'
    id_personal = Column(Integer, Sequence('id_personal_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    carrec = Column(String(100), nullable=False)

    # CLAUS FORANIES
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))
    id_arbit = Column(Integer, ForeignKey('Arbit.id_arbit'))

    # RELACIONS
    arbit = relationship("Arbit", back_populates="personal")
    torneig = relationship("Torneig", back_populates="personal")

class Ubicació(Base):
    __tablename__ = 'Ubicació'
    id_ubicacio = Column(Integer, Sequence('id_ubicacio_seq'), primary_key=True, autoincrement=True, nullable=False)
    ciutat = Column(String(50), nullable=False)
    provincia = Column(String(50), nullable=False)
    codi_postal = Column(Integer, nullable=False)

class Jugador(Base):
    __tablename__ = 'Jugador'
    id_jugador = Column(Integer, Sequence('id_jugador_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    cognom = Column(String(50), nullable=False)
    data_naixement = Column(DateTime, nullable=False)
    dorsal = Column(Integer, nullable=False)

    # CLAUS FORANIES
    id_equip = Column(Integer, ForeignKey('Equip.id_equip'))

    # RELACIONS
    equip = relationship("Equip", back_populates="jugador")

class Equip(Base):
    __tablename__ = 'Equip'
    id_equip = Column(Integer, Sequence('id_equip_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    escut = Column(LargeBinary, nullable=False)
    
    # CLAUS FORANIES
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))
    id_grup = Column(Integer, ForeignKey('Grup.id_grup'))
    id_partit = Column(Integer, ForeignKey('Partit.id_partit'))

    # RELACIONS
    torneig = relationship("Torneig", back_populates="equip")
    grup = relationship("Grup", back_populates="equip")
    partit = relationship("Partit", back_populates="equip")

class Grup(Base):
    __tablename__ = 'Grup'
    id_grup = Column(Integer, Sequence('id_grup_seq'), primary_key=True, autoincrement=True, nullable=False)
    nom = Column(String(50), nullable=False)
    nombre_equips = Column(Integer, nullable=False)

    # CLAUS FORANIES
    id_torneig = Column(Integer, ForeignKey('Torneig.id_torneig'))

    # RELACIONS
    torneig = relationship("Torneig", back_populates="grup")

class Gol(Base):
    __tablename__ = 'Gol'
    id_gol = Column(Integer, Sequence('id_gol_seq'), primary_key=True, autoincrement=True, nullable=False)
    minut = Column(Integer, nullable=False)

    # CLAUS FORANIES
    id_partit = Column(Integer, ForeignKey('Partit.id_partit'))
    id_jugador = Column(Integer, ForeignKey('Jugador.id_jugador'))

    # RELACIONS
    partit = relationship("Partit", back_populates="gol")
    jugador = relationship("Jugador", back_populates="gol")

class Sancions(Base):
    __tablename__ = "Sancions"
    id_jugador = Column(Integer, ForeignKey("Jugador.id_jugador"), primary_key=True)
    id_partit = Column(Integer, ForeignKey("Partit.id_partit"), primary_key=True)
    
    targeta_groga = Column(Integer, nullable=False)
    doble_targeta_groga = Column(Integer, nullable=False)
    targeta_vermella = Column(Integer, nullable=False)

    # RELACIONS
    jugador = relationship("Jugador", back_populates="sanciones")
    partit = relationship("Partit", back_populates="sanciones")

class Classificacio(Base):
    __tablename__ = 'Classificacio'
    id_grup = Column(Integer, ForeignKey('Grup.id_grup'), primary_key=True)
    id_equip = Column(Integer, ForeignKey('Equip.id_equip'), primary_key=True)

    victories = Column(Integer, nullable=False)
    empats = Column(Integer, nullable=False)
    derrotes = Column(Integer, nullable=False)
    punts = Column(Integer, nullable=False)

    # RELACIONS
    grup = relationship("Grup", back_populates="classificacio")
    equip = relationship("Equip", back_populates="classificacio")

## RELACIONS INVERSES
    
Torneig.arbit = relationship("Arbit", order_by=Arbit.id_arbit, back_populates="torneig")

Ubicació.torneig = relationship("Torneig", order_by=Torneig.id_torneig, back_populates="ubicacio")

Arbit.partit = relationship("Partit", order_by=Partit.id_partit, back_populates="arbit")

Grup.partit = relationship("Partit", order_by=Partit.id_partit, back_populates="grup")

Torneig.camp = relationship("Camp", order_by=Camp.id_camp, back_populates="torneig")
Partit.camp = relationship("Camp", order_by=Camp.id_camp, back_populates="partit")

Personal.administradors = relationship("Administradors", order_by=Administradors.id_administrador, back_populates="personal")
Torneig.administradors = relationship("Administradors", order_by=Administradors.id_administrador, back_populates="torneig")

Arbit.personal = relationship("Personal", order_by=Personal.id_personal, back_populates="arbit")
Torneig.personal = relationship("Personal", order_by=Personal.id_personal, back_populates="torneig")

Equip.jugador = relationship("Jugador", order_by=Jugador.id_jugador, back_populates="equip")

Torneig.equip = relationship("Equip", order_by=Equip.id_equip, back_populates="torneig")
Grup.equip = relationship("Equip", order_by=Equip.id_equip, back_populates="grup")
Partit.equip = relationship("Equip", order_by=Equip.id_equip, back_populates="partit")

Partit.gol = relationship("Gol", order_by=Gol.id_gol, back_populates="partit")
Jugador.gol = relationship("Gol", order_by=Gol.id_gol, back_populates="jugador")

Jugador.sancions = relationship("Sancions", order_by=Sancions.id_jugador, back_populates="jugador")
Partit.sancions = relationship("Sancions", order_by=Sancions.id_partit, back_populates="partit")

Grup.classificacio = relationship("Classificació", order_by=Classificació.id_grup, back_populates="grup")
Equip.classificacio = relationship("Classificació", order_by=Classificació.id_equip, back_populates="equip")

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