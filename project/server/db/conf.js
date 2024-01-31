import { Sequelize } from 'sequelize';

const sequelize = new Sequelize('Database_torneig', 'root', 'root', {
    host: 'localhost',
    dialect: 'mysql'
});

export default sequelize;