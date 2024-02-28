import unittest
from flask import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import app, db
from models.administradors import Administradors

class TestRoutes(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app_context = app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_administradores(self):
        administrador = Administradors(nom='Nombre', cognom='Apellido', email='admin@example.com', password='123456')
        db.session.add(administrador)
        db.session.commit()

        response = self.app.get('/administradores')
        self.assertEqual(response.status_code, 200)

        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['nom'], 'Nombre')
        self.assertEqual(data[0]['cognom'], 'Apellido')
        self.assertEqual(data[0]['email'], 'admin@example.com')

if __name__ == '__main__':
    unittest.main()
