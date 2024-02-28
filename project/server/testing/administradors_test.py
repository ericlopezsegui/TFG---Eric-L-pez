import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'server')))
from app import app, db  # Importa tu aplicación Flask y la instancia de la base de datos
from models.administradors import Administradors  # Importa el modelo de administradores

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_administradores(client):
    # Prueba la ruta para obtener todos los administradores
    response = client.get('/administradores')
    assert response.status_code == 200
    assert len(response.json) > 0

def test_get_administrador(client):
    # Prueba la ruta para obtener un administrador por su ID
    response = client.get('/administradores/1')
    assert response.status_code == 200
    assert 'nom' in response.json  # Verifica que se recibe el campo 'nom'

def test_create_administrador(client):
    # Prueba la ruta para crear un nuevo administrador
    data = {
        'nom': 'Nuevo',
        'cognom': 'Administrador',
        'email': 'nuevo@example.com',
        'password': 'contraseña'
    }
    response = client.post('/administradores', json=data)
    assert response.status_code == 201

    # Verifica que el nuevo administrador se haya agregado correctamente
    nuevo_administrador = Administradors.query.filter_by(email='nuevo@example.com').first()
    assert nuevo_administrador is not None

def test_update_administrador(client):
    # Prueba la ruta para actualizar un administrador existente
    data = {
        'nom': 'Nuevo nombre',
        'cognom': 'Nuevo apellido'
    }
    response = client.put('/administradores/1', json=data)
    assert response.status_code == 200

    # Verifica que el administrador haya sido actualizado correctamente en la base de datos
    administrador_actualizado = Administradors.query.get(1)
    assert administrador_actualizado.nom == 'Nuevo nombre'
    assert administrador_actualizado.cognom == 'Nuevo apellido'

def test_delete_administrador(client):
    # Prueba la ruta para eliminar un administrador
    response = client.delete('/administradores/1')
    assert response.status_code == 200

    # Verifica que el administrador haya sido eliminado de la base de datos
    administrador_eliminado = Administradors.query.get(1)
    assert administrador_eliminado is None
