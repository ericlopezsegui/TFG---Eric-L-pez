const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getClassificacio = (req, res) => {
    connection.query('SELECT * FROM classificació', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving classificacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/classificacio')
    .get(getClassificacio);

const getClassificacioById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM classificació WHERE id_grup = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving classificacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/classificacio')
    .get(getClassificacioById);

const getClassificacioId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM classificació', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving classificacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/classificacio')
    .get(getClassificacioId);

const createClassificacio = (req, res) => {
    const {id_equip, victories, empats, derrotes, punts} = req.body;
    connection.query('INSERT INTO classificació (id_equip, victories, empats, derrotes, punts) VALUES (?, ?, ?, ?, ?)', [id_equip, victories, empats, derrotes, punts], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating classificacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/classificacio')
    .post(createClassificacio);

const updateClassificacio = (req, res) => {
    const id_equip = req.params.id_equip;
    const {victories, empats, derrotes, punts} = req.body;
    connection.query('UPDATE classificació SET victories = ?, empats = ?, derrotes = ?, punts = ? WHERE id_equip = ?', [victories, empats, derrotes, punts, id_equip], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating classificacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/classificacio')
    .put(updateClassificacio);

const deleteClassificacio = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM classificació WHERE id_grup = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting classificacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

module.exports = app;