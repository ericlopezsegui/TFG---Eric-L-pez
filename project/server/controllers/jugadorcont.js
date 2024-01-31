import { Jugador } from '../db/models/jugador';

async function createJugador(nom, cognoms, dorsal, dataNaixement) {
  try {
    const jugador = await create({
      nom,
      cognoms,
      dorsal,
      dataNaixement,
    });
    console.log('Jugador creado:', jugador.toJSON());
    return jugador;
  } catch (error) {
    console.error('Error al crear el jugador:', error);
    throw error;
  }
}

async function getJugadors() {
    try {
      const jugadors = await Jugador.findAll();
      console.log('Lista de jugadores:', jugadors.map((jugador) => jugador.toJSON()));
      return jugadors;
    } catch (error) {
      console.error('Error al obtener la lista de jugadores:', error);
      throw error;
    }
  }
  
  async function getJugadorById(id) {
    try {
      const jugador = await Jugador.findByPk(id);
      console.log('Jugador encontrado:', jugador ? jugador.toJSON() : null);
      return jugador;
    } catch (error) {
      console.error('Error al obtener el jugador por ID:', error);
      throw error;
    }
  }

  async function updateJugador(id, nuevosDatos) {
    try {
      const jugador = await Jugador.findByPk(id);
      if (jugador) {
        await jugador.update(nuevosDatos);
        console.log('Jugador actualizado:', jugador.toJSON());
        return jugador;
      } else {
        console.error('Jugador no encontrado.');
        return null;
      }
    } catch (error) {
      console.error('Error al actualizar el jugador:', error);
      throw error;
    }
  }
  
  async function deleteJugador(id) {
    try {
      const jugador = await Jugador.findByPk(id);
      if (jugador) {
        await jugador.destroy();
        console.log('Jugador eliminado:', jugador.toJSON());
      } else {
        console.error('Jugador no encontrado.');
      }
    } catch (error) {
      console.error('Error al eliminar el jugador:', error);
      throw error;
    }
  }

export {
    createJugador,
    getJugadors,
    getJugadorById,
    updateJugador,
    deleteJugador,
};
