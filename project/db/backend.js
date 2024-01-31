const mysql = require('mysql');
const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'Database_torneig',
});

connection.connect((err) => {
if (err) {
    console.error('Error de connexió a MySQL:', err);
} else {
    console.log('Conenxió exitosa a MySQL');
}
});