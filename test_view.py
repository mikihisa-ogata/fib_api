import unittest
from view import app

# エンドポイントのテスト
class EndpointTest(unittest.TestCase):

    # テストモード
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_endpoint(self):
        test_cases = [
            (10, 200, {'result': 55}),
            (-5, 400, {'error': 'negative is not supported'}),
            ('abc', 400, {'error': 'invalid parameter'}),
            (1000000, 400, {'error': 'n is too big'}),
        ]
        for n, expected_status, expected_data in test_cases:
            with self.subTest(n=n):
                response = self.app.get(f'/fib?n={n}')
                data = response.get_json()
                self.assertEqual(response.status_code, expected_status)
                self.assertEqual(data, expected_data)

if __name__ == '__main__':
    unittest.main()