import DataTypes from 'sequelize';
import sequelize from '../conf.js';

const Jugador = sequelize.define('jugador', {
    nom: {
        type: DataTypes.STRING,
        allowNull: false
    },
    cognoms: {
        type: DataTypes.STRING,
        allowNull: false
    },
    dataNaixement: {
        type: DataTypes.DATE,
        allowNull: false
    },
    dorsal: {
        type: DataTypes.INTEGER,
        allowNull: false
    },
    
    id_equip: {
        type: DataTypes.INTEGER,
        allowNull: false,
        references: {
            model: 'Equip',
            key: 'id_equip'
        }
    }
});

module.exports = Jugador;