import unittest
from portfolio import app

class homepage_test(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_main_page(self):
         response = self.app.get('/', follow_redirects=True)
         self.assertEqual(response.status_code, 200)

    def test_nonexistent_page(self):
         response = self.app.get('/azaz', follow_redirects=True)
         self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
    unittest.main()
