const express = require('express');
const app = express();

const dotenv = require('dotenv');
dotenv.config();

const connection = require('../config.db');

const getEquip = (req, res) => {
    connection.query('SELECT * FROM equip', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving equip'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/equip')
    .get(getEquip);

const getEquipById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM equip WHERE id_equip = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving equip'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/equip')
    .get(getEquipById);

const getEquipId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM equip', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving equip'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/equip')
    .get(getEquipId);

const createEquip = (req, res) => {
    const {nom, escut, punts, victoria, derrota, empat, id_torneig, id_grup, id_partit} = req.body;
    
    connection.query('INSERT INTO equip (nom, escut, punts, victoria, derrota, empat, id_torneig, id_grup, id_partit) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', [nom, escut, punts, victoria, derrota, empat, id_torneig, id_grup, id_partit], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error creating equip'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/equip')
    .post(createEquip);

const updateEquip = (req, res) => {
    const id = req.params.id;
    const {nom, escut, punts, victoria, derrota, empat, id_torneig, id_grup, id_partit} = req.body;
    connection.query('UPDATE equip SET nom = ?, escut = ?, punts = ?, victoria = ?, derrota = ?, empat = ?, id_torneig = ?, id_grup = ?, id_partit = ? WHERE id_equip = ?', [nom, escut, punts, victoria, derrota, empat, id_torneig, id_grup, id_partit, id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error updating equip'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/equip')
    .put(updateEquip);

const deleteEquip = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM equip WHERE id_equip = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting equip'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/equip')
    .delete(deleteEquip);

module.exports = app;