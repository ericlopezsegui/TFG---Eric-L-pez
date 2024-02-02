const express = require('express');
const app = express();
const connection = require('../config.db');

const getAdmin = (req, res) => {
    connection.query('SELECT * FROM administradors', (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving admin'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/admin')
    .get(getAdmin);

const getAdminById = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT * FROM administradors WHERE id_administrador = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving admin'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/admin')
    .get(getAdminById);

const getAdminId = (req, res) => {
    const id = req.params.id;
    connection.query('SELECT LAST_INSERT_ID() FROM administradors', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error retrieving admin'});
        } else {
            res.status(200).json(results);
        }
    });
}

// ruta
app.route('/admin')
    .get(getAdminId);

const createAdmin = async (req, res) => {
    const {nom, cognom, email, password, id_personal, id_torneig} = req.body;

    try {
        const hashedPasswd = await hashPassword(password);
        connection.query('INSERT INTO administrador (nom, cognom, email, password, id_personal, id_torneig) VALUES (?, ?, ?, ?, ?, ?)', [nom, cognom, email, hashedPasswd, id_personal, id_torneig], (error, results) => {
            if (error) {
                res.status(500).json({message: 'Error creating admin'});
            } else {
                res.status(200).json({results});
            }
        });
    } catch (error) {
        res.status(500).json({message: 'Error creating admin'});
    }
}


// ruta
app.route('/admin')
    .post(createAdmin);

const updateAdmin = async (req, res) => {
    const id = req.params.id;
    const {nom, cognom, email, password, id_personal, id_torneig} = req.body;

    try{
        const hashedPasswd = await hashPassword(password);
        connection.query('UPDATE administrador SET nom = ?, cognom = ?, email = ?, password = ?, id_personal = ?, id_torneig = ? WHERE id_administrador = ?', [nom, cognom, email, hashedPasswd, id_personal, id_torneig, id], (error, results) => {
            if (error) {
                res.status(500).json({message: 'Error updating admin'});
            } else {
                res.status(200).json({results});
            }
        });
    } catch (error) {
        res.status(500).json({message: 'Error updating admin'});
    }
}

// ruta
app.route('/admin')
    .put(updateAdmin);

const deleteAdmin = (req, res) => {
    const id = req.params.id;
    connection.query('DELETE FROM administrador WHERE id_administrador = ?', [id], (error, results) => {
        if (error) {
            res.status(500).json({message: 'Error deleting admin'});
        } else {
            res.status(200).json({results});
        }
    });
}

// ruta
app.route('/admin')
    .delete(deleteAdmin);

module.exports = app;