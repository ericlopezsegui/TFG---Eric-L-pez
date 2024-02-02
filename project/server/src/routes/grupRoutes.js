const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getGrup = (req, res) => {
    connection.query('SELECT * FROM grup', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving grup'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/grup')
    .get(getGrup);

const getGrupById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM grup WHERE id_grup = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving grup'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/grup')
    .get(getGrupById);

const getGrupId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM grup', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving grup'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/grup')
    .get(getGrupId);

const createGrup = (req, res) => {
    const {nom, nombre_equips, id_torneig} = req.body;
    connection.query('INSERT INTO grup (nom, nombre_equips, id_torneig) VALUES (?, ?)', [nom, nombre_equips, id_torneig], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating grup'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/grup')
    .post(createGrup);

const updateGrup = (req, res) => {
    const id = req.params.id;
    const {nom, nombre_equips, id_torneig} = req.body;
    connection.query('UPDATE grup SET nom = ?, nombre_equips = ?, id_torneig = ? WHERE id_grup = ?', [nom, nombre_equips, id_torneig, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating grup'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/grup')
    .put(updateGrup);

    const deleteGrup = (req, res) => {
        const id = req.params.id;
        connection.query('DELETE FROM grup WHERE id_grup = ?', [id], (error, results) => {
            if (error) {
                res.status(500).json({message: 'Error deleting grup'});
            } else {
                res.status(200).json({results});
            }
        });
    }

// ruta
app.route('/grup')
    .delete(deleteGrup);
    
module.exports = app;

