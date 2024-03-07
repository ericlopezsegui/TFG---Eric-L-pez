import os
from flask import jsonify, send_from_directory, request, abort
from app import app, db

from models import *

@app.route('/camps', methods=['GET'])
def get_camps():
    camps = Camp.query.all()
    if not camps:
        abort(404, 'No camps found')

    return jsonify([camp.serialize() for camp in camps])

@app.route('/camps/<int:id_camp>', methods=['GET'])
def get_camp(id_camp):
    camp = Camp.query.get(id_camp)
    if not camp:
        abort(404, 'Camp not found')

    return jsonify(camp.serialize())

@app.route('/camps', methods=['POST'])
def create_camp():
    data = request.get_json()
    if not data or 'nom' not in data or 'id_ubicacio' not in data:
        abort(400, 'Missing data: nom or id_ubicacio is required')

    camp = Camp(nom=data['nom'], id_ubicacio=data['id_ubicacio'])
    db.session.add(camp)
    db.session.commit()
    return jsonify(camp.serialize())

@app.route('/camps/<int:id_camp>', methods=['PUT'])
def update_camp(id_camp):
    camp = Camp.query.get(id_camp)
    if not camp:
        abort(404, 'Camp not found')

    data = request.get_json()
    if not data or 'nom' not in data or 'id_ubicacio' not in data:
        abort(400, 'Missing data: nom or id_ubicacio is required')

    camp.nom = data['nom']
    camp.id_ubicacio = data['id_ubicacio']
    db.session.commit()
    return jsonify(camp.serialize())

@app.route('/camps/<int:id_camp>', methods=['DELETE'])
def delete_camp(id_camp):
    camp = Camp.query.get(id_camp)
    if not camp:
        abort(404, 'Camp not found')
    db.session.delete(camp)
    db.session.commit()
    return jsonify(camp.serialize())

@app.route('/classificacions', methods=['GET'])
def get_classificacions():
    classificacions = Classificacio.query.all()
    if not classificacions:
        abort(404, 'No classificacions found')
    return jsonify([classificacio.serialize() for classificacio in classificacions])

@app.route('/classificacions/<int:id_grup>/<int:id_equip>', methods=['GET'])
def get_classificacio(id_grup, id_equip):
    classificacio = Classificacio.query.get((id_grup, id_equip))
    if not classificacio:
        abort(404, 'Classificacio not found')

    return jsonify(classificacio.serialize())

@app.route('/classificacions', methods=['POST'])
def create_classificacio():
    data = request.get_json()
    if 'id_grup' not in data or 'id_equip' not in data or 'victories' not in data or 'empats' not in data or 'derrotes' not in data or 'punts' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    if not isinstance(data['id_grup'], int) or not isinstance(data['id_equip'], int) or not isinstance(data['victories'], int) or not isinstance(data['empats'], int) or not isinstance(data['derrotes'], int) or not isinstance(data['punts'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    classificacio = Classificacio(id_grup=data['id_grup'], id_equip=data['id_equip'], victories=data['victories'], empats=data['empats'], derrotes=data['derrotes'], punts=data['punts'])
    db.session.add(classificacio)
    db.session.commit()
    return jsonify(classificacio.serialize())

@app.route('/classificacions/<int:id_grup>/<int:id_equip>', methods=['PUT'])
def update_classificacio(id_grup, id_equip):
    classificacio = Classificacio.query.get((id_grup, id_equip))
    if classificacio is None:
        return jsonify({'error': 'Classificacio does not exist '}), 404
        
    data = request.get_json()
    if 'victories' not in data or 'empats' not in data or 'derrotes' not in data or 'punts' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    if not isinstance(data['victories'], int) or not isinstance(data['empats'], int) or not isinstance(data['derrotes'], int) or not isinstance(data['punts'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    classificacio.victories = data['victories']
    classificacio.empats = data['empats']
    classificacio.derrotes = data['derrotes']
    classificacio.punts = data['punts']
    db.session.commit()
    return jsonify(classificacio.serialize())

@app.route('/classificacions/<int:id_grup>/<int:id_equip>', methods=['DELETE'])
def delete_classificacio(id_grup, id_equip):
    classificacio = Classificacio.query.get((id_grup, id_equip))
    if classificacio is None:
        return jsonify({'error': 'Classificacio does not exist '}), 404
    
    db.session.delete(classificacio)
    db.session.commit()
    return jsonify(classificacio.serialize())

@app.route('/equips', methods=['GET'])
def get_equips():
    equips = Equip.query.all()
    if not equips:
        abort(404, 'No equips found')

    return jsonify([equip.serialize() for equip in equips])

@app.route('/equips/<int:id_equip>', methods=['GET'])
def get_equip(id_equip):
    equip = Equip.query.get(id_equip)
    if not equip:
        abort(404, 'Equip not found')
        
    return jsonify(equip.serialize())

@app.route('/equips', methods=['POST'])
def create_equip():
    data = request.get_json()
    if 'nom' not in data or 'escut' not in data or 'id_grup' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['escut'], str) or not isinstance(data['id_grup'], int) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Los tipos de datos son incorrectos'}), 400
    
    equip = Equip(nom=data['nom'], escut=data['escut'], id_grup=data['id_grup'], id_torneig=data['id_torneig'])
    db.session.add(equip)
    db.session.commit()
    return jsonify(equip.serialize())

@app.route('/equips/<int:id_equip>', methods=['PUT'])
def update_equip(id_equip):
    equip = Equip.query.get(id_equip)
    if equip is None:
        return jsonify({'error': 'El equipo no existe'}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'escut' not in data or 'id_grup' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Faltan campos requeridos'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['escut'], str) or not isinstance(data['id_grup'], int) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Los tipos de datos son incorrectos'}), 400
    
    equip.nom = data['nom']
    equip.escut = data['escut']
    equip.id_grup = data['id_grup']
    equip.id_torneig = data['id_torneig']
    db.session.commit()
    return jsonify(equip.serialize())

@app.route('/equips/<int:id_equip>', methods=['DELETE'])
def delete_equip(id_equip):
    equip = Equip.query.get(id_equip)
    if equip is None:
        return jsonify({'error': 'El equipo no existe'}), 404
    
    db.session.delete(equip)
    db.session.commit()
    return jsonify(equip.serialize())

@app.route('/gols', methods=['GET'])
def get_gols():
    gols = Gol.query.all()
    if not gols:
        abort(404, 'No gols found')
    return jsonify([gol.serialize() for gol in gols])

@app.route('/gols/<int:id_gol>', methods=['GET'])
def get_gol(id_gol):
    gol = Gol.query.get(id_gol)
    if not gol:
        abort(404, 'Gol not found')
    return jsonify(gol.serialize())

@app.route('/gols', methods=['POST'])
def create_gol():
    data = request.get_json()
    if 'minut' not in data or 'id_partit' not in data or 'id_jugador' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['minut'], int) or not isinstance(data['id_partit'], int) or not isinstance(data['id_jugador'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    gol = Gol(minut=data['minut'], id_partit=data['id_partit'], id_jugador=data['id_jugador'])
    db.session.add(gol)
    db.session.commit()
    return jsonify(gol.serialize())

@app.route('/gols/<int:id_gol>', methods=['PUT'])
def update_gol(id_gol):
    gol = Gol.query.get(id_gol)
    if gol is None:
        return jsonify({'error': 'Gol does not exist '}), 404
    
    data = request.get_json()
    if 'minut' not in data or 'id_partit' not in data or 'id_jugador' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['minut'], int) or not isinstance(data['id_partit'], int) or not isinstance(data['id_jugador'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    gol.minut = data['minut']
    gol.id_partit = data['id_partit']
    gol.id_jugador = data['id_jugador']
    db.session.commit()
    return jsonify(gol.serialize())

@app.route('/gols/<int:id_gol>', methods=['DELETE'])
def delete_gol(id_gol):
    gol = Gol.query.get(id_gol)
    if gol is None:
        return jsonify({'error': 'Gol does not exist '}), 404
    
    db.session.delete(gol)
    db.session.commit()
    return jsonify(gol.serialize())

@app.route('/grups', methods=['GET'])
def get_grups():
    grups = Grup.query.all()
    if not grups:
        abort(404, 'No grups found')

    return jsonify([grup.serialize() for grup in grups])

@app.route('/grups/<int:id_grup>', methods=['GET'])
def get_grup(id_grup):
    grup = Grup.query.get(id_grup)
    if not grup:
        abort(404, 'Grup not found')

    return jsonify(grup.serialize())

@app.route('/grups', methods=['POST'])
def create_grup():
    data = request.get_json()
    if 'nom' not in data or 'num_equips' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['num_equips'], int) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    grup = Grup(nom=data['nom'], num_equips=data['num_equips'], id_torneig=data['id_torneig'])
    db.session.add(grup)
    db.session.commit()
    return jsonify(grup.serialize())

@app.route('/grups/<int:id_grup>', methods=['PUT'])
def update_grup(id_grup):
    grup = Grup.query.get(id_grup)
    if grup is None:
        return jsonify({'error': 'Grup does not exist '}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'num_equips' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['num_equips'], int) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    grup.nom = data['nom']
    grup.num_equips = data['num_equips']
    grup.id_torneig = data['id_torneig']
    db.session.commit()
    return jsonify(grup.serialize())

@app.route('/grups/<int:id_grup>', methods=['DELETE'])
def delete_grup(id_grup):
    grup = Grup.query.get(id_grup)
    if grup is None:
        return jsonify({'error': 'Grup does not exist '}), 404
        
    db.session.delete(grup)
    db.session.commit()
    return jsonify(grup.serialize())

@app.route('/jugadors', methods=['GET'])
def get_jugadors():
    jugadors = Jugador.query.all()
    if not jugadors:
        abort(404, 'No jugadors found')

    return jsonify([jugador.serialize() for jugador in jugadors])

@app.route('/jugadors/<int:id_jugador>', methods=['GET'])
def get_jugador(id_jugador):
    jugador = Jugador.query.get(id_jugador)
    if not jugador:
        abort(404, 'Jugador not found')

    return jsonify(jugador.serialize())

@app.route('/jugadors', methods=['POST'])
def create_jugador():
    data = request.get_json()
    if 'nom' not in data or 'cognom' not in data or 'data_naixement' not in data or 'dorsal' not in data or 'id_equip' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['cognom'], str) or not isinstance(data['data_naixement'], str) or not isinstance(data['dorsal'], int) or not isinstance(data['id_equip'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    jugador = Jugador(nom=data['nom'], cognom=data['cognom'], data_naixement=data['data_naixement'], dorsal=data['dorsal'], id_equip=data['id_equip'])
    db.session.add(jugador)
    db.session.commit()
    return jsonify(jugador.serialize())

@app.route('/jugadors/<int:id_jugador>', methods=['PUT'])
def update_jugador(id_jugador):
    jugador = Jugador.query.get(id_jugador)
    if jugador is None:
        return jsonify({'error': 'Jugador does not exist '}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'cognom' not in data or 'data_naixement' not in data or 'dorsal' not in data or 'id_equip' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['cognom'], str) or not isinstance(data['data_naixement'], str) or not isinstance(data['dorsal'], int) or not isinstance(data['id_equip'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    jugador.nom = data['nom']
    jugador.cognom = data['cognom']
    jugador.data_naixement = data['data_naixement']
    jugador.dorsal = data['dorsal']
    jugador.id_equip = data['id_equip']
    db.session.commit()
    return jsonify(jugador.serialize())

@app.route('/jugadors/<int:id_jugador>', methods=['DELETE'])
def delete_jugador(id_jugador):
    jugador = Jugador.query.get(id_jugador)
    if jugador is None:
        return jsonify({'error': 'Jugador does not exist '}), 404
    
    db.session.delete(jugador)
    db.session.commit()
    return jsonify(jugador.serialize())

@app.route('/partits', methods=['GET'])
def get_partits():
    partits = Partit.query.all()
    if not partits:
        abort(404, 'No partits found')

    return jsonify([partit.serialize() for partit in partits])

@app.route('/partits/<int:id_partit>', methods=['GET'])
def get_partit(id_partit):
    partit = Partit.query.get(id_partit)
    if not partit:
        abort(404, 'Partit not found')
    return jsonify(partit.serialize())

@app.route('/partits', methods=['POST'])
def create_partit():
    data = request.get_json()
    if 'data' not in data or 'hora' not in data or 'resultat' not in data or 'id_equip1' not in data or 'id_equip2' not in data or 'gols_equip1' not in data or 'gols_equip2' not in data or 'id_grup' not in data or 'id_personal' not in data or 'id_camp' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['data'], str) or not isinstance(data['hora'], str) or not isinstance(data['resultat'], str) or not isinstance(data['id_equip1'], int) or not isinstance(data['id_equip2'], int) or not isinstance(data['gols_equip1'], int) or not isinstance(data['gols_equip2'], int) or not isinstance(data['id_grup'], int) or not isinstance(data['id_personal'], int) or not isinstance(data['id_camp'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    partit = Partit(data=data['data'], hora=data['hora'], resultat=data['resultat'], id_equip1=data['id_equip1'], id_equip2=data['id_equip2'], gols_equip1=data['gols_equip1'], gols_equip2=data['gols_equip2'], id_grup=data['id_grup'], id_personal=data['id_personal'], id_camp=data['id_camp'])
    db.session.add(partit)
    db.session.commit()
    return jsonify(partit.serialize())

@app.route('/partits/<int:id_partit>', methods=['PUT'])
def update_partit(id_partit):
    partit = Partit.query.get(id_partit)
    if partit is None:
        return jsonify({'error': 'Partit does not exist '}), 404
    
    data = request.get_json()
    if 'data' not in data or 'hora' not in data or 'resultat' not in data or 'id_equip1' not in data or 'id_equip2' not in data or 'gols_equip1' not in data or 'gols_equip2' not in data or 'id_grup' not in data or 'id_personal' not in data or 'id_camp' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['data'], str) or not isinstance(data['hora'], str) or not isinstance(data['resultat'], str) or not isinstance(data['id_equip1'], int) or not isinstance(data['id_equip2'], int) or not isinstance(data['gols_equip1'], int) or not isinstance(data['gols_equip2'], int) or not isinstance(data['id_grup'], int) or not isinstance(data['id_personal'], int) or not isinstance(data['id_camp'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    partit.data = data['data']
    partit.hora = data['hora']
    partit.resultat = data['resultat']
    partit.id_equip1 = data['id_equip1']
    partit.id_equip2 = data['id_equip2']
    partit.gols_equip1 = data['gols_equip1']
    partit.gols_equip2 = data['gols_equip2']
    partit.id_grup = data['id_grup']
    partit.id_perosnal = data['id_personal']
    partit.id_camp = data['id_camp']
    db.session.commit()
    return jsonify(partit.serialize())

@app.route('/partits/<int:id_partit>', methods=['DELETE'])
def delete_partit(id_partit):
    partit = Partit.query.get(id_partit)
    if partit is None:
        return jsonify({'error': 'Partit does not exist '}), 404
    
    db.session.delete(partit)
    db.session.commit()
    return jsonify(partit.serialize())

@app.route('/personal', methods=['GET'])
def get_personal():
    personal = Personal.query.all()
    if not personal:
        abort(404, 'No personal found')

    return jsonify([personal.serialize() for personal in personal])

@app.route('/personal/<int:id_personal>', methods=['GET'], endpoint='get_personal_2')
def get_personal(id_personal):
    personal = Personal.query.get(id_personal)
    if not personal:
        abort(404, 'Personal not found')

    return jsonify(personal.serialize())

@app.route('/personal', methods=['POST'])
def create_personal():
    data = request.get_json()
    if 'nom' not in data or 'cognom' not in data or 'email' not in data or 'password' not in data or 'carrec' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['cognom'], str) or not isinstance(data['email'], str) or not isinstance(data['password'], str) or not isinstance(data['carrec'], str) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    personal = Personal(nom=data['nom'], cognom=data['cognom'], email=data['email'], password=data['password'], carrec=data['carrec'], id_torneig=data['id_torneig'])
    db.session.add(personal)
    db.session.commit()
    return jsonify(personal.serialize())

@app.route('/personal/<int:id_personal>', methods=['PUT'])
def update_personal(id_personal):
    personal = Personal.query.get(id_personal)
    if personal is None:
        return jsonify({'error': 'Personal does not exist '}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'cognom' not in data or 'email' not in data or 'password' not in data or 'carrec' not in data or 'id_torneig' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['cognom'], str) or not isinstance(data['email'], str) or not isinstance(data['password'], str) or not isinstance(data['carrec'], str) or not isinstance(data['id_torneig'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    personal.nom = data['nom']
    personal.cognom = data['cognom']
    personal.email = data['email']
    personal.password = data['password']
    personal.carrec = data['carrec']
    personal.id_torneig = data['id_torneig']
    db.session.commit()
    return jsonify(personal.serialize())

@app.route('/personal/<int:id_personal>', methods=['DELETE'])
def delete_personal(id_personal):
    personal = Personal.query.get(id_personal)
    if personal is None:
        return jsonify({'error': 'Personal does not exist '}), 404
    
    db.session.delete(personal)
    db.session.commit()
    return jsonify(personal.serialize())

@app.route('/sancions', methods=['GET'])
def get_sancions():
    sancions = Sancio.query.all()
    if not sancions:
        abort(404, 'No sancions found')

    return jsonify([sancio.serialize() for sancio in sancions])

@app.route('/sancions/<int:id_jugador>/<int:id_partit>', methods=['GET'])
def get_sancio(id_jugador, id_partit):
    sancio = Sancio.query.get((id_jugador, id_partit))
    if not sancio:
        abort(404, 'Sancio not found')

    return jsonify(sancio.serialize())

@app.route('/sancions', methods=['POST'])
def create_sancio():
    data = request.get_json()
    if 'id_jugador' not in data or 'id_partit' not in data or 'targeta_groga' not in data or 'targeta_vermella' not in data or 'doble_targeta_groga' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['id_jugador'], int) or not isinstance(data['id_partit'], int) or not isinstance(data['targeta_groga'], int) or not isinstance(data['targeta_vermella'], int) or not isinstance(data['doble_targeta_groga'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    sancio = Sancio(id_jugador=data['id_jugador'], id_partit=data['id_partit'], targeta_groga=data['targeta_groga'], targeta_vermella=data['targeta_vermella'], doble_targeta_groga=data['doble_targeta_groga'])
    db.session.add(sancio)
    db.session.commit()
    return jsonify(sancio.serialize())

@app.route('/sancions/<int:id_jugador>/<int:id_partit>', methods=['PUT'])
def update_sancio(id_jugador, id_partit):
    sancio = Sancio.query.get((id_jugador, id_partit))
    if sancio is None:
        return jsonify({'error': 'Sancio does not exist '}), 404
    
    data = request.get_json()
    if 'targeta_groga' not in data or 'targeta_vermella' not in data or 'doble_targeta_groga' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['targeta_groga'], int) or not isinstance(data['targeta_vermella'], int) or not isinstance(data['doble_targeta_groga'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    sancio.targeta_groga = data['targeta_groga']
    sancio.targeta_vermella = data['targeta_vermella']
    sancio.doble_targeta_groga = data['doble_targeta_groga']
    db.session.commit()
    return jsonify(sancio.serialize())

@app.route('/sancions/<int:id_jugador>/<int:id_partit>', methods=['DELETE'])
def delete_sancio(id_jugador, id_partit):
    sancio = Sancio.query.get((id_jugador, id_partit))
    if sancio is None:
        return jsonify({'error': 'Sancio does not exist '}), 404
    
    db.session.delete(sancio)
    db.session.commit()
    return jsonify(sancio.serialize())

@app.route('/torneigs', methods=['GET'])
def get_torneigs():
    torneigs = Torneig.query.all()
    if not torneigs:
        abort(404, 'No torneigs found')

    return jsonify([torneig.serialize() for torneig in torneigs])

@app.route('/torneigs/<int:id_torneig>', methods=['GET'])
def get_torneig(id_torneig):
    torneig = Torneig.query.get(id_torneig)
    if not torneig:
        abort(404, 'Torneig not found')

    return jsonify(torneig.serialize())

@app.route('/torneigs', methods=['POST'])
def create_torneig():
    data = request.get_json()
    if 'nom' not in data or 'data_inici' not in data or 'data_fi' not in data or 'fase' not in data or 'id_ubicacio' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['data_inici'], str) or not isinstance(data['data_fi'], str) or not isinstance(data['fase'], str) or not isinstance(data['id_ubicacio'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    torneig = Torneig(nom=data['nom'], data_inici=data['data_inici'], data_fi=data['data_fi'], fase=data['fase'], id_ubicacio=data['id_ubicacio'])
    db.session.add(torneig)
    db.session.commit()
    return jsonify(torneig.serialize())

@app.route('/torneigs/<int:id_torneig>', methods=['PUT'])
def update_torneig(id_torneig):
    torneig = Torneig.query.get(id_torneig)
    if torneig is None:
        return jsonify({'error': 'Torneig does not exist '}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'data_inici' not in data or 'data_fi' not in data or 'fase' not in data or 'id_ubicacio' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['data_inici'], str) or not isinstance(data['data_fi'], str) or not isinstance(data['fase'], str) or not isinstance(data['id_ubicacio'], int):
        return jsonify({'error': 'Data is incorrect'}), 400

    torneig.nom = data['nom']
    torneig.data_inici = data['data_inici']
    torneig.data_fi = data['data_fi']
    torneig.fase = data['fase']
    torneig.id_ubicacio = data['id_ubicacio']
    db.session.commit()
    return jsonify(torneig.serialize())

@app.route('/torneigs/<int:id_torneig>', methods=['DELETE'])
def delete_torneig(id_torneig):
    torneig = Torneig.query.get(id_torneig)
    if torneig is None:
        return jsonify({'error': 'Torneig does not exist '}), 404
    

    db.session.delete(torneig)
    db.session.commit()
    return jsonify(torneig.serialize())

@app.route('/ubicacions', methods=['GET'])
def get_ubicacions():
    ubicacions = Ubicacio.query.all()
    if not ubicacions:
        abort(404, 'No ubicacions found')

    return jsonify([ubicacio.serialize() for ubicacio in ubicacions])

@app.route('/ubicacions/<int:id_ubicacio>', methods=['GET'])
def get_ubicacio(id_ubicacio):
    ubicacio = Ubicacio.query.get(id_ubicacio)
    if not ubicacio:
        abort(404, 'Ubicacio not found')

    return jsonify(ubicacio.serialize())

@app.route('/ubicacions', methods=['POST'])
def create_ubicacio():
    data = request.get_json()
    if 'nom' not in data or 'adreca' not in data or 'ciutat' not in data or 'provincia' not in data or 'pais' not in data or 'codi_postal' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['adreca'], str) or not isinstance(data['ciutat'], str) or not isinstance(data['provincia'], str) or not isinstance(data['pais'], str) or not isinstance(data['codi_postal'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    ubicacio = Ubicacio(nom=data['nom'], adreca=data['adreca'], ciutat=data['ciutat'], provincia=data['provincia'], pais=data['pais'], codi_postal=data['codi_postal'])
    db.session.add(ubicacio)
    db.session.commit()
    return jsonify(ubicacio.serialize())

@app.route('/ubicacions/<int:id_ubicacio>', methods=['PUT'])
def update_ubicacio(id_ubicacio):
    ubicacio = Ubicacio.query.get(id_ubicacio)
    if ubicacio is None:
        return jsonify({'error': 'Ubicacio does not exist '}), 404
    
    data = request.get_json()
    if 'nom' not in data or 'adreca' not in data or 'ciutat' not in data or 'provincia' not in data or 'pais' not in data or 'codi_postal' not in data:
        return jsonify({'error': 'Missing required data'}), 400
    
    if not isinstance(data['nom'], str) or not isinstance(data['adreca'], str) or not isinstance(data['ciutat'], str) or not isinstance(data['provincia'], str) or not isinstance(data['pais'], str) or not isinstance(data['codi_postal'], int):
        return jsonify({'error': 'Data is incorrect'}), 400
    
    ubicacio.nom = data['nom']
    ubicacio.adreca = data['adreca']
    ubicacio.ciutat = data['ciutat']
    ubicacio.provincia = data['provincia']
    ubicacio.pais = data['pais']
    ubicacio.codi_postal = data['codi_postal']
    db.session.commit()
    return jsonify(ubicacio.serialize())

@app.route('/ubicacions/<int:id_ubicacio>', methods=['DELETE'])
def delete_ubicacio(id_ubicacio):
    ubicacio = Ubicacio.query.get(id_ubicacio)
    if ubicacio is None:
        return jsonify({'error': 'Ubicacio does not exist '}), 404
    
    db.session.delete(ubicacio)
    db.session.commit()
    return jsonify(ubicacio.serialize())

@app.route('/')
def index():
    return jsonify({"message": "Welcome to my Flask app!"})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')
