# フィボナッチ数の計算
def fib_calc(n):
    if n <= 0:
        return None
    elif n == 1 or n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b