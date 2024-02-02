const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getTorneig = (req, res) => {
    connection.query('SELECT * FROM torneig', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving torneig'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/torneig')
    .get(getTorneig);

const getTorneigById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM torneig WHERE id_torneig = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving torneig'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/torneig')
    .get(getTorneigById);
    
const getTorneigId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM torneig', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving torneig'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/torneig')
    .get(getTorneigId);

const createTorneig = (req, res) => {
    const {nom, data_inici, data_final, fase, id_ubicacio} = req.body;
    connection.query('INSERT INTO torneig (nom, data_inici, data_final, fase, id_ubicacio) VALUES (?, ?, ?, ?, ?)', [nom, data_inici, data_final, fase, id_ubicacio], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating torneig'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/torneig')
    .post(createTorneig);

const updateTorneig = (req, res) => {
    const id = req.params.id;
    const {nom, data_inici, data_final, fase, id_ubicacio} = req.body;
    connection.query('UPDATE torneig SET nom = ?, data_inici = ?, data_final = ?, fase = ?, id_ubicacio = ? WHERE id_torneig = ?', [nom, data_inici, data_final, fase, id_ubicacio, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating torneig'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/torneig')
    .put(updateTorneig);

const deleteTorneig = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM torneig WHERE id_torneig = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting torneig'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/torneig')
    .delete(deleteTorneig);

module.exports = app;