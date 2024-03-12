import unittest
from flask import Flask
from flask_testing import TestCase
from routes import app

class TestRoutes(TestCase):
    def create_app(self):
        return app

    def test_get_camps(self):
        response = self.client.get('/camps')
        self.assert200(response)

    def test_get_camp(self):
        response = self.client.get('/camps/1')
        self.assert200(response)

    def test_create_camp(self):
        data = {
            'name': 'Camp 1',
            'location': 'Location 1'
        }
        response = self.client.post('/camps', json=data)
        self.assert200(response)

    def test_update_camp(self):
        data = {
            'name': 'Updated Camp 1',
            'location': 'Updated Location 1'
        }
        response = self.client.put('/camps/1', json=data)
        self.assert200(response)

    def test_delete_camp(self):
        response = self.client.delete('/camps/1')
        self.assert200(response)

    # Add tests for other CRUD operations here

if __name__ == '__main__':
    unittest.main()
