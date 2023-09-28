import unittest
from app import app

class FibAPITest(unittest.TestCase):

    # テストモード
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # nが自然数の時
    def test_positive_fib(self):
        response = self.app.get('/fib?n=100')
        data = response.get_json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['n'], 100)
        self.assertEqual(data['result'], 354224848179261915075)

    # nが負の数の時
    def test_negative_input(self):
        response = self.app.get('/fib?n=-5')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'negative in not supported')

    # nが整数以外の時
    def test_invalid_input(self):
        response = self.app.get('/fib?n=abc')
        data = response.get_json()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(data['error'], 'invalid parameter')

if __name__ == '__main__':
    unittest.main()