from flask import Flask, request, jsonify

app = Flask(__name__)

# フィボナッチ数の計算
def fib_calc(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b

@app.route('/')
def hello():
    return "enter number"

# フィボナッチ数を返すAPIエンドポイント
@app.route('/fib', methods=['GET'])
def get_fib():
    try:
        n = int(request.args.get('n'))
        if n < 0:
            return jsonify({'error': 'negative in not supported'}), 400
        result = fib_calc(n)
        return jsonify({'n': n, 'result': result})
    except ValueError:
        return jsonify({'error': 'invalid parameter'}), 400

if __name__ == '__main__':
    app.run()
