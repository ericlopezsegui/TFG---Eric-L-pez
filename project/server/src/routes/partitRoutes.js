const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getPartit = (req, res) => {
    connection.query('SELECT * FROM partit', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving partit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/partit')
    .get(getPartit);

const getPartitById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM partit WHERE id_partit = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving partit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/partit')
    .get(getPartitById);

const getPartitId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM partit', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving partit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/partit')
    .get(getPartitId);

const createPartit = (req, res) => {
    const {data_partit, hora_partit, resultat, gols_equip1, gols_equip2,id_equip1, id_equip2, id_arbit, id_grup} = req.body;
    connection.query('INSERT INTO partit (data_partit, hora_partit, resultat, gols_equip1, gols_equip2, id_equip1, id_equip2, id_arbit, id_grup) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [data_partit, hora_partit, resultat, gols_equip1, gols_equip2, id_equip1, id_equip2, id_arbit, id_grup], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating partit'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/partit')
    .post(createPartit);

const updatePartit = (req, res) => {
    const id = req.params.id;
    const {data_partit, hora_partit, resultat, gols_equip1, gols_equip2,id_equip1, id_equip2, id_arbit, id_grup} = req.body;
    connection.query('UPDATE partit SET data_partit = ?, hora_partit = ?, resultat = ?, gols_equip1 = ?, gols_equip2 = ?, id_equip1 = ?, id_equip2 = ?, id_arbit = ?, id_grup = ? WHERE id_partit = ?', [data_partit, hora_partit, resultat, gols_equip1, gols_equip2, id_equip1, id_equip2, id_arbit, id_grup, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating partit'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/partit')
    .put(updatePartit);

const deletePartit = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM partit WHERE id_partit = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting partit'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/partit')
    .delete(deletePartit);
    
module.exports = app;