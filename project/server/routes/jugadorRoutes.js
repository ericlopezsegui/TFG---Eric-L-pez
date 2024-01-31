import { Router } from 'express';
const router = Router();

import { createJugador, getAllJugadores, getJugadorById, updateJugadorById, deleteJugadorById } from '../controllers/jugadorcont.js';

// Rutas CRUD para jugadores
router.post('/jugadores', createJugador);
router.get('/jugadores', getAllJugadores);
router.get('/jugadores/:id', getJugadorById);
router.put('/jugadores/:id', updateJugadorById);
router.delete('/jugadores/:id', deleteJugadorById);

export default router;
