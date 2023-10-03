from flask import Flask, request, jsonify
from model import fib_calc

app = Flask(__name__)

# フィボナッチ数を返すAPIエンドポイント
@app.route('/fib', methods=['GET'])
def get_fib():
    try:
        n = int(request.args.get('n'))
    except Exception:
        return jsonify({'error': 'invalid parameter'}), 400
    
    if n <= 0:
        return jsonify({'error': 'negative is not supported'}), 400
    
    if n > 20000:
        return jsonify({'error': 'n is too big'}), 400
    
    result = fib_calc(n)
    return jsonify({'result': result}), 200

if __name__ == '__main__':
    app.run()