import unittest

from dojo.views import app


class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_urls_are_available(self):
        URLS = ['/', '/task1', '/task2']
        for url in URLS:
            response = self.app.get(url)
            self.assertEqual(response.status_code, 200)
        response = self.app.post('/task1')
        self.assertEqual(response.status_code, 200)
