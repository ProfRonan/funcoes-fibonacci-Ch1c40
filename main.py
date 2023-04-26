def fibonacci(n):
    if n < 0:
        raise ValueError("n tem que ser maior do que zero")
    if n == 0:
        return 1
    if n == 1:
        return 2
    return fibonnaci(n-1) + (n-2)
