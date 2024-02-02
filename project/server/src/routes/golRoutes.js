const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getGol = (req, res) => {
    connection.query('SELECT * FROM gol', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving gol'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/gol')
    .get(getGol);

const getGolById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM gol WHERE id_gol = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving gol'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/gol')
    .get(getGolById);

const getGolId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM gol', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving gol'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/gol')
    .get(getGolId);

const createGol = (req, res) => {
    const {id_jugador, id_partit, minut} = req.body;
    connection.query('INSERT INTO gol (minut, id_partit, id_jugador) VALUES (?, ?, ?)', [minut, id_partit, id_jugador], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating gol'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/gol')
    .get(createGol);

const updateGol = (req, res) => {
    const id = req.params.id;
    const {minut, id_partit, id_jugador} = req.body;
    connection.query('UPDATE gol SET minut = ?, id_partit = ?, id_jugador = ? WHERE id_gol = ?', [minut, id_partit, id_jugador, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving gol'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/gol')
    .put(updateGol);

const deleteGol = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM gol WHERE id_gol = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting gol'});
        } else {
            res.status(200).json(results);
        }
    });
}

module.exports = app;

