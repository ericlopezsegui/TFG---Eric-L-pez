from flask import jsonify, request
from app import db

from models.torneig import Torneig
from models.personal import Personal 
from models.sancions import Sancions
from models.ubicacio import Ubicacio
from models.partit import Partit
from models.jugador import Jugador
from models.grup import Grup
from models.gol import Gol
from models.equip import Equip
from models.classificacio import Classificacio
from models.camp import Camp

def configure_routes(app):
    # RUTES CAMP
    @app.route('/camps', methods=['GET'])
    def get_camps():
        camps = Camp.query.all()
        return jsonify([camp.serialize() for camp in camps])

    @app.route('/camps/<int:id_camp>', methods=['GET'])
    def get_camp(id_camp):
        camp = Camp.query.get_or_404(id_camp)
        return jsonify(camp.serialize())

    @app.route('/camps', methods=['POST'])
    def create_camp():
        datos = request.json
        nuevo_camp = Camp(nom=datos['nom'])
        db.session.add(nuevo_camp)
        db.session.commit()
        return jsonify(nuevo_camp.serialize()), 201

    @app.route('/camps/<int:id_camp>', methods=['PUT'])
    def update_camp(id_camp):
        camp = Camp.query.get_or_404(id_camp)
        datos = request.json
        camp.nom = datos.get('nom', camp.nom)
        camp.id_torneig = datos.get('id_torneig', camp.id_torneig)
        camp.id_partit = datos.get('id_partit', camp.id_partit)
        db.session.commit()
        return jsonify(camp.serialize())

    @app.route('/camps/<int:id_camp>', methods=['DELETE'])
    def delete_camp(id_camp):
        camp = Camp.query.get_or_404(id_camp)
        db.session.delete(camp)
        db.session.commit()
        return jsonify({"message": "Camp eliminat correctament"})

    # RUTES CLASSIFICACIO
    @app.route('/classificacions', methods=['GET'])
    def get_classificacions():
        classificacions = Classificacio.query.all()
        return jsonify([classificacio.serialize() for classificacio in classificacions])

    @app.route('/classificacions/<int:id_grup>', methods=['GET'])
    def get_classificacio(id_grup):
        classificacio = Classificacio.query.get_or_404(id_grup)
        return jsonify(classificacio.serialize())

    @app.route('/classificacions', methods=['POST'])
    def create_classificacio():
        datos = request.json
        nueva_classificacio = Classificacio(id_grup=datos['id_grup'], id_equip=datos['id_equip'], victories=datos['victories'], empats=datos['empats'], derrotes=datos['derrotes'], punts=datos['punts'])
        db.session.add(nueva_classificacio)
        db.session.commit()
        return jsonify(nueva_classificacio.serialize()), 201

    @app.route('/classificacions/<int:id_grup>', methods=['PUT'])
    def update_classificacio(id_grup):
        classificacio = Classificacio.query.get_or_404(id_grup)
        datos = request.json
        classificacio.id_equip = datos.get('id_equip', classificacio.id_equip)
        classificacio.victories = datos.get('victories', classificacio.victories)
        classificacio.empats = datos.get('empats', classificacio.empats)
        classificacio.derrotes = datos.get('derrotes', classificacio.derrotes)
        classificacio.punts = datos.get('punts', classificacio.punts)
        db.session.commit()
        return jsonify(classificacio.serialize())

    @app.route('/classificacions/<int:id_grup>', methods=['DELETE'])
    def delete_classificacio(id_grup):
        classificacio = Classificacio.query.get_or_404(id_grup)
        db.session.delete(classificacio)
        db.session.commit()
        return jsonify({"message": "Classificacio eliminada correctament"})

    # RUTES EQUIP
    @app.route('/equips', methods=['GET'])
    def get_equips():
        equips = Equip.query.all()
        return jsonify([equip.serialize() for equip in equips])

    @app.route('/equips/<int:id_equip>', methods=['GET'])
    def get_equip(id_equip):
        equip = Equip.query.get_or_404(id_equip)
        return jsonify(equip.serialize())

    @app.route('/equips', methods=['POST'])
    def create_equip():
        datos = request.json
        nuevo_equip = Equip(nom=datos['nom'], escut=datos['escut'], id_torneig=datos['id_torneig'])
        db.session.add(nuevo_equip)
        db.session.commit()
        return jsonify(nuevo_equip.serialize()), 201

    @app.route('/equips/<int:id_equip>', methods=['PUT'])
    def update_equip(id_equip):
        equip = Equip.query.get_or_404(id_equip)
        datos = request.json
        equip.nom = datos.get('nom', equip.nom)
        equip.escut = datos.get('escut', equip.escut)
        equip.id_torneig = datos.get('id_torneig', equip.id_torneig)
        equip.id_grup = datos.get('id_grup', equip.id_grup)
        equip.id_partit = datos.get('id_partit', equip.id_partit)
        db.session.commit()
        return jsonify(equip.serialize())

    @app.route('/equips/<int:id_equip>', methods=['DELETE'])
    def delete_equip(id_equip):
        equip = Equip.query.get_or_404(id_equip)
        db.session.delete(equip)
        db.session.commit()
        return jsonify({"message": "Equip eliminat correctament"})

    # RUTES GOL

    @app.route('/gols', methods=['GET'])
    def get_gols():
        gols = Gol.query.all()
        return jsonify([gol.serialize() for gol in gols])

    @app.route('/gols/<int:id_gol>', methods=['GET'])
    def get_gol(id_gol, id_partit):
        gol = Gol.query.get_or_404(id_gol, id_partit)
        return jsonify(gol.serialize())

    @app.route('/gols', methods=['POST'])
    def create_gol():
        datos = request.json
        nuevo_gol = Gol(id_jugador=datos['id_jugador'], id_partit=datos['id_partit'], minut=datos['minut'])
        db.session.add(nuevo_gol)
        db.session.commit()
        return jsonify(nuevo_gol.serialize()), 201

    @app.route('/gols/<int:id_gol>', methods=['PUT'])
    def update_gol(id_gol):
        gol = Gol.query.get_or_404(id_gol)
        datos = request.json
        gol.id_jugador = datos.get('id_jugador', gol.id_jugador)
        gol.id_partit = datos.get('id_partit', gol.id_partit)
        gol.minut = datos.get('minut', gol.minut)
        db.session.commit()
        return jsonify(gol.serialize())

    @app.route('/gols/<int:id_gol>', methods=['DELETE'])
    def delete_gol(id_gol):
        gol = Gol.query.get_or_404(id_gol)
        db.session.delete(gol)
        db.session.commit()
        return jsonify({"message": "Gol eliminat correctament"})

    # RUTES GRUP
    @app.route('/grups', methods=['GET'])
    def get_grups():
        grups = Grup.query.all()
        return jsonify([grup.serialize() for grup in grups])

    @app.route('/grups/<int:id_grup>', methods=['GET'])
    def get_grup(id_grup):
        grup = Grup.query.get_or_404(id_grup)
        return jsonify(grup.serialize())

    @app.route('/grups', methods=['POST'])
    def create_grup():
        datos = request.json
        nuevo_grup = Grup(nom=datos['nom'], nombre_equips=datos['nombre_equips'], id_torneig=datos['id_torneig'])
        db.session.add(nuevo_grup)
        db.session.commit()
        return jsonify(nuevo_grup.serialize()), 201

    @app.route('/grups/<int:id_grup>', methods=['PUT'])
    def update_grup(id_grup):
        grup = Grup.query.get_or_404(id_grup)
        datos = request.json
        grup.nom = datos.get('nom', grup.nom)
        grup.nombre_equips = datos.get('nombre_equips', grup.nombre_equips)
        grup.id_torneig = datos.get('id_torneig', grup.id_torneig)
        db.session.commit()
        return jsonify(grup.serialize())

    @app.route('/grups/<int:id_grup>', methods=['DELETE'])
    def delete_grup(id_grup):
        grup = Grup.query.get_or_404(id_grup)
        db.session.delete(grup)
        db.session.commit()
        return jsonify({"message": "Grup eliminat correctament"})

    # RUTES JUGADOR
    @app.route('/jugadors', methods=['GET'])
    def get_jugadors(id_equip):
        jugadors = Jugador.query.get_or_404(id_equip)
        return jsonify([jugador.serialize() for jugador in jugadors])

    @app.route('/jugadors/<int:id_jugador>', methods=['GET'])
    def get_jugador(id_jugador):
        jugador = Jugador.query.get_or_404(id_jugador)
        return jsonify(jugador.serialize())

    @app.route('/jugadors', methods=['POST'])
    def create_jugador():
        datos = request.json
        nuevo_jugador = Jugador(nom=datos['nom'], cognom=datos['cognom'], dorsal=datos['dorsal'], data_naixement=datos['data_naixement'] ,id_equip=datos['id_equip'])
        db.session.add(nuevo_jugador)
        db.session.commit()
        return jsonify(nuevo_jugador.serialize()), 201

    @app.route('/jugadors/<int:id_jugador>', methods=['PUT'])
    def update_jugador(id_jugador):
        jugador = Jugador.query.get_or_404(id_jugador)
        datos = request.json
        jugador.nom = datos.get('nom', jugador.nom)
        jugador.cognom = datos.get('cognom', jugador.cognom)
        jugador.dorsal = datos.get('dorsal', jugador.dorsal)
        jugador.data_naixement = datos.get('data_naixement', jugador.data_naixement)
        jugador.id_equip = datos.get('id_equip', jugador.id_equip)
        db.session.commit()
        return jsonify(jugador.serialize())

    @app.route('/jugadors/<int:id_jugador>', methods=['DELETE'])
    def delete_jugador(id_jugador):
        jugador = Jugador.query.get_or_404(id_jugador)
        db.session.delete(jugador)
        db.session.commit()
        return jsonify({"message": "Jugador eliminat correctament"})

    # RUTES PARTIT
    @app.route('/partits', methods=['GET'])
    def get_partits(id_grup):
        partits = Partit.query.get_or_404(id_grup)
        return jsonify([partit.serialize() for partit in partits])

    @app.route('/partits/<int:id_partit>', methods=['GET'])
    def get_partit(id_partit):
        partit = Partit.query.get_or_404(id_partit)
        return jsonify(partit.serialize())

    @app.route('/partits', methods=['POST'])
    def create_partit():
        datos = request.json
        nuevo_partit = Partit(data=datos['data_partit'], hora=datos['hora_partit'], id_camp=datos['id_camp'], id_arbitre=datos['id_arbitre'], id_grup=datos['id_grup'])
        db.session.add(nuevo_partit)
        db.session.commit()
        return jsonify(nuevo_partit.serialize()), 201

    @app.route('/partits/<int:id_partit>', methods=['PUT'])
    def update_partit(id_partit):
        partit = Partit.query.get_or_404(id_partit)
        datos = request.json
        partit.data_partit = datos.get('data_partit', partit.data_partit)
        partit.hora_partit = datos.get('hora_partit', partit.hora_partit)
        partit.resultat = datos.get('resultat', partit.resultat)
        partit.gols_equip1 = datos.get('gols_equip1', partit.gols_equip1)
        partit.gols_equip2 = datos.get('gols_equip2', partit.gols_equip2)
        partit.id_equip1 = datos.get('id_equip1', partit.id_equip1)
        partit.id_equip2 = datos.get('id_equip2', partit.id_equip2)
        partit.id_arbitre = datos.get('id_arbitre', partit.id_arbitre)
        partit.id_grup = datos.get('id_grup', partit.id_grup)
        db.session.commit()
        return jsonify(partit.serialize())

    @app.route('/partits/<int:id_partit>', methods=['DELETE'])
    def delete_partit(id_partit):
        partit = Partit.query.get_or_404(id_partit)
        db.session.delete(partit)
        db.session.commit()
        return jsonify({"message": "Partit eliminat correctament"})

    # RUTES PERSONAL
    @app.route('/personals', methods=['GET'])
    def get_personals(id_torneig):
        personals = Personal.query.get_or_404(id_torneig)
        return jsonify([personal.serialize() for personal in personals])

    @app.route('/personals/<int:id_personal>', methods=['GET'])
    def get_personal(id_personal):
        personal = Personal.query.get_or_404(id_personal)
        return jsonify(personal.serialize())

    @app.route('/personals', methods=['POST'])
    def create_personal():
        datos = request.json
        nuevo_personal = Personal(nom=datos['nom'], cognom=datos['cognom'], carrec=datos['carrec'], id_torneig=datos['id_torneig'])
        db.session.add(nuevo_personal)
        db.session.commit()
        return jsonify(nuevo_personal.serialize()), 201

    @app.route('/personals/<int:id_personal>', methods=['PUT'])
    def update_personal(id_personal):
        personal = Personal.query.get_or_404(id_personal)
        datos = request.json
        personal.nom = datos.get('nom', personal.nom)
        personal.cognom = datos.get('cognom', personal.cognom)
        personal.carrec = datos.get('carrec', personal.carrec)
        personal.id_torneig = datos.get('id_torneig', personal.id_torneig)
        personal.id_arbit = datos.get('id_arbit', personal.id_arbit)
        db.session.commit()
        return jsonify(personal.serialize())

    @app.route('/personals/<int:id_personal>', methods=['DELETE'])
    def delete_personal(id_personal):
        personal = Personal.query.get_or_404(id_personal)
        db.session.delete(personal)
        db.session.commit()
        return jsonify({"message": "Personal eliminat correctament"})

    # RUTES SANCIONS

    @app.route('/sancions', methods=['GET'])
    def get_sancions(id_partit):
        sancions = Sancions.query.get_or_404(id_partit)
        return jsonify([sancion.serialize() for sancion in sancions])

    @app.route('/sancions/<int:id_sancion>', methods=['GET'])
    def get_sancion(id_sancion):
        sancion = Sancions.query.get_or_404(id_sancion)
        return jsonify(sancion.serialize())

    @app.route('/sancions', methods=['POST'])
    def create_sancion():
        datos = request.json
        nueva_sancion = Sancions(id_jugador=datos['id_jugador'], id_partit=datos['id_partit'], minut=datos['minut'], motiu=datos['motiu'])
        db.session.add(nueva_sancion)
        db.session.commit()
        return jsonify(nueva_sancion.serialize()), 201

    @app.route('/sancions/<int:id_sancion>', methods=['PUT'])
    def update_sancion(id_sancion):
        sancion = Sancions.query.get_or_404(id_sancion)
        datos = request.json
        sancion.id_jugador = datos.get('id_jugador', sancion.id_jugador)
        sancion.id_partit = datos.get('id_partit', sancion.id_partit)
        sancion.minut = datos.get('minut', sancion.minut)
        sancion.motiu = datos.get('motiu', sancion.motiu)
        db.session.commit()
        return jsonify(sancion.serialize())

    @app.route('/sancions/<int:id_sancion>', methods=['DELETE'])
    def delete_sancion(id_sancion):
        sancion = Sancions.query.get_or_404(id_sancion)
        db.session.delete(sancion)
        db.session.commit()
        return jsonify({"message": "Sancion eliminada correctament"})

    # RUTES TORNEIG
    @app.route('/torneigs', methods=['GET'])
    def get_torneigs():
        torneigs = Torneig.query.all()
        return jsonify([torneig.serialize() for torneig in torneigs])

    @app.route('/torneigs/<int:id_torneig>', methods=['GET'])
    def get_torneig(id_torneig):
        torneig = Torneig.query.get_or_404(id_torneig)
        return jsonify(torneig.serialize())

    @app.route('/torneigs', methods=['POST'])
    def create_torneig():
        datos = request.json
        nuevo_torneig = Torneig(nom=datos['nom'], data_inici=datos['data_inici'], data_fi=datos['data_fi'], id_ubicacio=datos['id_ubicacio'])
        db.session.add(nuevo_torneig)
        db.session.commit()
        return jsonify(nuevo_torneig.serialize()), 201

    @app.route('/torneigs/<int:id_torneig>', methods=['PUT'])
    def update_torneig(id_torneig):
        torneig = Torneig.query.get_or_404(id_torneig)
        datos = request.json
        torneig.nom = datos.get('nom', torneig.nom)
        torneig.data_inici = datos.get('data_inici', torneig.data_inici)
        torneig.data_fi = datos.get('data_fi', torneig.data_fi)
        torneig.id_ubicacio = datos.get('id_ubicacio', torneig.id_ubicacio)
        db.session.commit()
        return jsonify(torneig.serialize())

    @app.route('/torneigs/<int:id_torneig>', methods=['DELETE'])
    def delete_torneig(id_torneig):
        torneig = Torneig.query.get_or_404(id_torneig)
        db.session.delete(torneig)
        db.session.commit()
        return jsonify({"message": "Torneig eliminat correctament"})

    # RUTES UBICACIO
    @app.route('/ubicacions', methods=['GET'])
    def get_ubicacions():
        ubicacions = Ubicacio.query.all()
        return jsonify([ubicacio.serialize() for ubicacio in ubicacions])

    @app.route('/ubicacions/<int:id_ubicacio>', methods=['GET'])
    def get_ubicacio(id_ubicacio):
        ubicacio = Ubicacio.query.get_or_404(id_ubicacio)
        return jsonify(ubicacio.serialize())

    @app.route('/ubicacions', methods=['POST'])
    def create_ubicacio():
        datos = request.json
        nueva_ubicacio = Ubicacio(ciutat=datos['ciutat'], provincia=datos['provincia'], codi_postal=datos['codi_postal'])
        db.session.add(nueva_ubicacio)
        db.session.commit()
        return jsonify(nueva_ubicacio.serialize()), 201

    @app.route('/ubicacions/<int:id_ubicacio>', methods=['PUT'])
    def update_ubicacio(id_ubicacio):
        ubicacio = Ubicacio.query.get_or_404(id_ubicacio)
        datos = request.json
        ubicacio.ciutat = datos.get('ciutat', ubicacio.ciutat)
        ubicacio.provincia = datos.get('provincia', ubicacio.provincia)
        ubicacio.codi_postal = datos.get('codi_postal', ubicacio.codi_postal)
        db.session.commit()
        return jsonify(ubicacio.serialize())
