import requests
import unittest

class TestAPIEndpoints(unittest.TestCase):

    BASE_URL = 'http://yourapi.com/api'

    def test_get_endpoint(self):
        response = requests.get(f'{self.BASE_URL}/endpoint')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_post_endpoint(self):
        response = requests.post(f'{self.BASE_URL}/endpoint', json={'key': 'value'})
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_put_endpoint(self):
        response = requests.put(f'{self.BASE_URL}/endpoint/1', json={'key': 'new_value'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['key'], 'new_value')

    def test_delete_endpoint(self):
        response = requests.delete(f'{self.BASE_URL}/endpoint/1')
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()