import unittest
from flask_testing import TestCase
from api import app

class WeatherTestCase(TestCase):

    def create_app(self):
        app.config['TESTING'] = True
        return app

    def test_turkish_characters(self):
        response = self.client.post('/', data={'city': 'Şırnak'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))

    def test_valid_city(self):
        response = self.client.post('/', data={'city': 'Mexico'})
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))
        self.assertIn('Mexico', response.data.decode('utf-8'))

    def test_default_city(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('Türkçe karakter kullanmayınız', response.data.decode('utf-8'))
        self.assertIn('Istanbul', response.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
