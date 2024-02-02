const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getUbicacio = (req, res) => {
    connection.query('SELECT * FROM ubicacio', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving ubicacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(getUbicacio);

const getUbicacioById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM ubicacio WHERE id_ubicacio = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving ubicacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(getUbicacioById);

const getUbicacioId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM ubicacio', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving ubicacio'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(getUbicacioId);

const createUbicacio = (req, res) => {
    const {ciutat, provincia, codi_postal} = req.body;
    connection.query('INSERT INTO ubicacio (ciutat, provincia, codi_postal) VALUES (?, ?, ?)', [ciutat, provincia, codi_postal], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating ubicacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(createUbicacio);

const updateUbicacio = (req, res) => {
    const id = req.params.id;
    const {ciutat, provincia, codi_postal} = req.body;
    connection.query('UPDATE ubicacio SET ciutat = ?, provincia = ?, codi_postal = ? WHERE id_ubicacio = ?', [ciutat, provincia, codi_postal, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating ubicacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(updateUbicacio);

const deleteUbicacio = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM ubicacio WHERE id_ubicacio = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting ubicacio'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/ubicacio')
    .get(deleteUbicacio);
    
module.exports = app;


