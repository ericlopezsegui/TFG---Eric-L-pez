import DataType from 'sequelize';
import sequelize from '../conf.js';

const Administrador = sequelize.define('administrador', {
    nom: {
        type: DataType.STRING,
        allowNull: false
    },
    cognom: {
        type: DataType.STRING,
        allowNull: false
    },
    usuari: {
        type: DataType.STRING,
        allowNull: false
    },
    password: {
        type: DataType.STRING,
        allowNull: false
    },
    id_torneig: {
        type: DataType.INTEGER,
        allowNull: false,
        references: {
            model: 'Torneig',
            key: 'id_torneig'
        }
    },
    id_personal: {
        type: DataType.INTEGER,
        allowNull: false,
        references: {
            model: 'Personal',
            key: 'id_personal'
        }
    }
});

module.exports = Administrador;