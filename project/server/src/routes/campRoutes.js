const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getCamp = (req, res) => {
    connection.query('SELECT * FROM camp', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving camp'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/camp')
    .get(getCamp);

const getCampById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM camp WHERE id_camp = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving camp'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/camp')
    .get(getCampById);

const getCampId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM camp', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving camp'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/camp')
    .get(getCampId);

const createCamp = (req, res) => {
    const {nom, id_torneig} = req.body;
    connection.query('INSERT INTO camp (nom, id_torneig) VALUES (?, ?)', [nom, id_torneig], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating camp'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/camp')
    .post(createCamp);

const updateCamp = (req, res) => {
    const id = req.params.id;
    const {nom, id_torneig, id_partit} = req.body;
    connection.query('UPDATE camp SET nom = ?, id_torneig = ?, id_partit = ? WHERE id_camp = ?', [nom, id_torneig, id_partit, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating camp'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/camp')
    .put(updateCamp);

const deleteCamp = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM camp WHERE id_camp = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting camp'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/camp')
    .delete(deleteCamp);

module.exports = app;
