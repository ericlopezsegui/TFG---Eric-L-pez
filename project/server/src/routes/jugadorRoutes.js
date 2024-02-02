const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getJugador = (req, res) => {
    connection.query('SELECT * FROM jugador', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving jugador'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/jugador')
    .get(getJugador);

const getJugadorById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM jugador WHERE id_jugador = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving jugador'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/jugador')
    .get(getJugadorById);

const getJugadorId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM jugador', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving jugador'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/jugador')
    .get(getJugadorId);

const createJugador = (req, res) => {
    const {nom, cognom, data_naixement, dorsal, id_equip} = req.body;
    connection.query('INSERT INTO jugador (nom, cognom, data_naixement, dorsal, id_equip) VALUES (?, ?, ?, ?, ?)', [nom, cognom, data_naixement, dorsal, id_equip], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating jugador'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/jugador')
    .post(createJugador);

const updateJugador = (req, res) => {
    const id = req.params.id;
    const {nom, cognom, data_naixement, dorsal, id_equip} = req.body;
    connection.query('UPDATE jugador SET nom = ?, cognom = ?, data_naixement = ?, dorsal = ?, id_equip = ? WHERE id_jugador = ?', [nom, cognom, data_naixement, dorsal, id_equip, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating jugador'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/jugador')
    .put(updateJugador);

const deleteJugador = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM jugador WHERE id_jugador = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting jugador'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/jugador')
    .delete(deleteJugador);

module.exports = app;