import { Administrador } from '../models/administrador.js';

  const administradorcont ={
    createAdministrador: async (req, res) => {
        try {
            const administrador = await Administrador.create(req.body);
            return res.status(201).json({
                administrador
            });
        } catch (error) {
            return res.status(500).json({error: error.message})
        }
    },

    getAllAdministradors: async (req, res) => {
        try {
            const administradors = await Administrador.findAll();
            return res.status(200).json({administradors});
        } catch (error) {
            return res.status(500).send(error.message);
        }
    },

    getAdministradorById: async (req, res) => {
        const { id } = req.params;

        try {
            const administrador = await Administrador.findOne({
                where: { id: id }
            });
            if (administrador) {
                return res.status(200).json({administrador});
            }
            return res.status(404).send('Administrador with the specified ID does not exists');
        } catch (error) {
            return res.status(500).send(error.message);
        }
    },
    
    updateAdministradorById: async (req, res) => {
        const { id } = req.params;

        try {
            const [ updated ] = await Administrador.update(req.body, {
                where: { id: id }
            });
            if (updated) {
                const updatedAdministrador = await Administrador.findOne({ where: { id: id } });
                return res.status(200).json({ administrador: updatedAdministrador });
            }
            throw new Error('Administrador not found');
        } catch (error) {
            return res.status(500).send(error.message);
        }
    },

    deleteAdministradorById: async (req, res) => {
        const { id } = req.params;
        try {
            const deleted = await Administrador.destroy({
                where: { id: id }
            });
            if (deleted) {
                return res.status(204).send("Administrador deleted");
            }
            throw new Error("Administrador not found");
        } catch (error) {
            return res.status(500).send(error.message);
        }
    },
};

module.exports = administradorcont;