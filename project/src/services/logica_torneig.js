import { useState } from "react";

const useLogicaTorneig = () => {
    const [equips, setEquips] = useState([]);
    const [partits, setPartits] = useState([]);
    const [classificacio, setClassificacio] = useState([]);

    crearTorneig = () => {
        const torneig = {
            id: torneig.torneigs.length + 1,
            nom: torneig.nom,
        };

        torneig.torneig

        return torneig;
    };

    const afegirEquip = (nomEquip, jugadors) => {
        if (!jugadors || jugadors.length === 0) {
            console.error("El nombre de jugadors ha de ser entre 7 i 12");
            return null;
        }
        
        if (jugadors.length < 7 || jugadors.length > 12) {
            console.error("El nombre de jugadors ha de ser entre 7 i 12");
            return null;
        }
        
        const equip_nou = {
            id: equips.length + 1,
            nom: nomEquip,
            nom_jugadors: jugadors,
            punts: 0,
            gols_a_favor: 0,
            gols_en_contra: 0,
            gols_diferencia: 0,
        };

        setEquips((prevEquips) => [...prevEquips, equip_nou]);

        return equip_nou;
    };

    const crearGrups = () => {
        const equipsCopiats = [...equips];
        const grups = [];

        while (equipsCopiats.length > 0) {
        const grup = {
            id: grups.length + 1,
            equips: [],
        };

        for (let i = 0; i < 4; i++) {
            const index = Math.floor(Math.random() * equipsCopiats.length);
            const equip = equipsCopiats.splice(index, 1)[0];
            grup.equips.push(equip);
        }

        grups.push(grup);
        }

        return grups;
    };

    return {
        equips,
        partits,
        classificacio,
        afegirEquip,
        crearGrups,
    };
};

export default useLogicaTorneig;
