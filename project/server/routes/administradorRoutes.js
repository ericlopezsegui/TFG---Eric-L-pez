import { Router } from 'express';
import { createAdministrador, getAllAdministradores, getAdministradorById, updateAdministradorById, deleteAdministradorById } from '../../server/controllers/administradorController';

const router = Router();

router.post('/administradores', createAdministrador);
router.get('/administradores', getAllAdministradores);
router.get('/administradores/:id', getAdministradorById);
router.put('/administradores/:id', updateAdministradorById);
router.delete('/administradores/:id', deleteAdministradorById);

export default router;
