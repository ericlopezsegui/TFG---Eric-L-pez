import React, { useState } from 'react';
import ClassificacioGrups from './ClassificacioGrups';
import useLogicaTorneig from '../services/logica_torneig';

const Torneo = () => {
    const {
        equips,
        partits,
        classificacio,
        afegirEquip,
        crearGrups,
    } = useLogicaTorneig();

    const [nomEquip, setNomEquip] = useState('');
    const [jugador, setJugador] = useState('');
    const [jugadors, setJugadors] = useState([]);
    const [grups, setGrups] = useState([]);

    const handleAgregarEquipo = () => {
        if (nomEquip.trim() !== '' && jugadors.length >= 7 && jugadors.length <= 12) {
        const nouEquip = afegirEquip(nomEquip, jugadors);
        setNomEquip('');
        setJugadors([]);
        }
    };

    const handleCrearGrupos = () => {
        const grupsGenerats = crearGrups();
        setGrups(grupsGenerats);
    };

    return (
        <div>
        <h2>Registro de Equipos</h2>
        <form onSubmit={(e) => e.preventDefault()}>
            <label>
            Nombre del Equipo:
            <input
                type="text"
                value={nomEquip}
                onChange={(e) => setNomEquip(e.target.value)}
            />
            </label>
            <br />
            <label>
            Nombres de los Jugadores:
            {Array.from({ length: 12 }).map((_, index) => (
                <input
                key={index}
                type="text"
                value={jugadors[index] || ''}
                onChange={(e) => {
                    const nuevosJugadors = [...jugadors];
                    nuevosJugadors[index] = e.target.value;
                    setJugadors(nuevosJugadors);
                }}
                placeholder={`Jugador ${index + 1}`}
                />
            ))}
            </label>

            <br />

            <button type="button" onClick={handleAgregarEquipo}>
            Agregar Equipo
            </button>
        </form>

        <h2>Lista de Equipos</h2>
            <ul>
            {equips.map((equip) => (
                <li key={equip.id}>
                {equip.nom} - Jugadores: {equip.jugadors ? equip.jugadors.join(', ') : 'Ninguno'}
                </li>
            ))}
            </ul>

        <h2>Crear Grupos</h2>
        <button onClick={handleCrearGrupos}>Crear Grupos</button>

        <h2>Tabla de Puntuación</h2>
        <ClassificacioGrups grupos={grups} />
        </div>
    );
};

export default Torneo
