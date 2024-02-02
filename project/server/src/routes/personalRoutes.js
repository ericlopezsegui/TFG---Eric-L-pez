const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getPersonal = (req, res) => {
    connection.query('SELECT * FROM personal', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving personal'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/personal')
    .get(getPersonal);

const getPersonalById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM personal WHERE id_personal = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving personal'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/personal')
    .get(getPersonalById);

const getPersonalId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM personal', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving personal'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/personal')
    .get(getPersonalId);

const createPersonal = (req, res) => {
    const {nom, cognom, carrec, id_torneig, id_arbit} = req.body;

    connection.query('INSERT INTO personal (nom, cognom, carrec, id_torneig, id_arbit) VALUES (?, ?, ?, ?, ?)', [nom, cognom, carrec, id_torneig, id_arbit], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating personal'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/personal')
    .post(createPersonal);

const updatePersonal = (req, res) => {
    const id = req.params.id;
    const {nom, cognom, carrec, id_torneig, id_arbit} = req.body;

    connection.query('UPDATE personal SET nom = ?, cognom = ?, carrec = ?, id_torneig = ?, id_arbit = ? WHERE id_personal = ?', [nom, cognom, carrec, id_torneig, id_arbit, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating personal'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/personal')
    .put(updatePersonal);

const deletePersonal = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM personal WHERE id_personal = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting personal'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/personal')
    .delete(deletePersonal);

module.exports = app;
