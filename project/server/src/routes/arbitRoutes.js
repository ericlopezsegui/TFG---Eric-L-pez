const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getArbit = (req, res) => {
    connection.query('SELECT * FROM arbit', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving arbit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/arbit')
    .get(getArbit);

const getArbitById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM arbit WHERE id_arbit = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving arbit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/arbit')
    .get(getArbitById);

const getArbitId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM arbit', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving arbit'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/arbit')
    .get(getArbitId);

const createArbit = async (req, res) => {
    const {nom, cognom, email, password, id_torneig} = req.body;
    
    try {
        const hashedPasswd = await hashPassword(password);
        connection.query('INSERT INTO arbit (nom, cognom, email, password, id_torneig) VALUES (?, ?, ?, ?, ?)', [nom, cognom, email, hashedPasswd, id_torneig], (error, results) => {
            if (error) {
                res.status(500).json({message: 'Error creating arbit'});
            } else {
                res.status(200).json({results});
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// ruta
app.route('/arbit')
    .post(createArbit);

const updateArbit = async (req, res) => {
    const id = req.params.id;
    const {nom, cognom, email, password, id_torneig} = req.body;
    
    try {
        const hashedPasswd = await hashPassword(password);
        connection.query('UPDATE arbit SET nom = ?, cognom = ?, email = ?, password = ?, id_torneig = ? WHERE id_arbit = ?', [nom, cognom, email, hashedPasswd, id_torneig, id], (error, results) => {
            if (error) {
                res.status(500).json({message: 'Error updating arbit'});
            } else {
                res.status(200).json({results});
            }
        });
    } catch (error) {
        console.log(error);
    }
}

// ruta
app.route('/arbit')
    .put(updateArbit);

const deleteArbit = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM arbit WHERE id_arbit = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting arbit'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/arbit')
    .delete(deleteArbit);

module.exports = app;
