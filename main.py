def Fibonacci(i):
    if i < 0:
        raise ValueError("n tem que ser maior do que zero")
    if i == 0:
        return 1
    if i == 1:
        return 1
    return Fibonacci(i-1) + Fibonacci(i - 2)
