import unittest
from app import app
from app import fib_calc

# エンドポイントのテスト
class EndpointTest(unittest.TestCase):

    # テストモード
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_endpoint(self):
        test_cases = [
            (10, 200, {'result': 55}),
            (-5, 400, {'error': 'negative in not supported'}),
            ('abc', 400, {'error': 'invalid parameter'}),
            (1000000, 400, {'error': 'n is too big'}),
        ]

        for n, expected_status, expected_data in test_cases:
            with self.subTest(n=n):
                response = self.app.get(f'/fib?n={n}')
                data = response.get_json()
                self.assertEqual(response.status_code, expected_status)
                self.assertEqual(data, expected_data)

# フィボナッチ数を計算する関数のテスト
class FibCalcTest(unittest.TestCase):
    def test_fib(self):
        test_cases = [(0, 0), (1, 1), (2, 1), (3, 2), (10, 55), (-1, 0), (-5, 0)]
        for n, expected in test_cases:
            with self.subTest(n=n, expected=expected):
                result = fib_calc(n)
                self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()