import sequelize, { Sequelize } from './conf.js';

// models

async function connect() {
    try{
        await sequelize.sync();
        console.log('Connection has been established successfully.');
    } catch (error) {
        console.error('Unable to connect to the database:', error);
    }
}

export default connect;