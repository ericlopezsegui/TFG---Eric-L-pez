import express from 'express';
import cors from 'cors';
import mongoose from 'mongoose';

const app = express();
const PORT = process.env.PORT || 5000;

mongoose.connect('mongodb://localhost:3306/Database_torneig', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

const connection = mongoose.connection;

connection.on('error', (error) => console.error('Error en la conexión a la base de datos:', error));
connection.once('open', () => console.log('Conexión exitosa a la base de datos'));

// Middlewares
app.use(express.json());
app.use(cors());

// Puerto en el que escucha el servidor
app.listen(PORT, () => console.log(`Server listening on port ${PORT}`));
