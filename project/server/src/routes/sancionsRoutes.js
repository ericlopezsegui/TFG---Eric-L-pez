const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getSancions = (req, res) => {
    connection.query('SELECT * FROM sancions', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving sancions'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/sancions')
    .get(getSancions);

const getSancionsById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM sancions WHERE id_sancio = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving sancions'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/sancions')
    .get(getSancionsById);

const getSancionsId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM sancions', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving sancions'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/sancions')
    .get(getSancionsId);

const createSancions = (req, res) => {
    const {id_jugador, id_partit, targeta_groga, doble_targeta_groga, targeta_vermella} = req.body;
    connection.query('INSERT INTO sancions (targeta_groga, doble_targeta_groga, targeta_vermella, id_jugador, id_partit) VALUES (?, ?, ?, ?, ?)', [targeta_groga, doble_targeta_groga, targeta_vermella, id_jugador, id_partit], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating sancions'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/sancions')
    .post(createSancions);

const updateSancions = (req, res) => {
    const id = req.params.id;
    const {targeta_groga, doble_targeta_groga, targeta_vermella, id_jugador, id_partit} = req.body;
    connection.query('UPDATE sancions SET targeta_groga = ?, doble_targeta_groga = ?, targeta_vermella = ?, id_jugador = ?, id_partit = ? WHERE id_sancio = ?', [targeta_groga, doble_targeta_groga, targeta_vermella, id_jugador, id_partit, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating sancions'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/sancions')
    .put(updateSancions);

const deleteSancions = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM sancions WHERE id_sancio = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting sancions'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/sancions')
    .delete(deleteSancions);
    
module.exports = app;

