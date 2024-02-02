const dotenv = require('dotenv');
dotenv.config();

const mysql = require('mysql2/promise');
//const bcrypt = require('bcrypt');

const connecion = mysql.createConnection({
    host: process.env.DB_HOST,
    user: process.env.DB_USER,
    password: process.env.DB_PASSWD,
    database: process.env.DB_NAME
});


module.exports = connecion;