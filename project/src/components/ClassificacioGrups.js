import React from 'react';

const ClassificacioGrups = ({ grupos }) => {
    if (!grupos || grupos.length === 0) {
        return <p>No hay grupos para mostrar</p>;
    }

    const classificacioGrups = (grup) => {
        if (!grup || !grup.equips) {
        return [];
        }

        return grup.equips.map((equip) => ({
        nom: equip.nom || 'Equipo sin nombre',
        punts: equip.punts || 0, 
        }));
    };

    return (
        <div>
        <h3>Tabla de Puntuación</h3>
        {grupos.map((grup) => (
            <div key={grup.id}>
            <h4>Grupo {grup.id}</h4>
            <table>
                <thead>
                <tr>
                    <th>Equipo</th>
                    <th>Puntos</th>
                </tr>
                </thead>
                <tbody>
                {classificacioGrups(grup).map((equip) => (
                    <tr key={equip.nom}>
                    <td>{equip.nom}</td>
                    <td>{equip.punts}</td>
                    </tr>
                ))}
                </tbody>
            </table>
            </div>
        ))}
        </div>
    );
};

export default ClassificacioGrups;
