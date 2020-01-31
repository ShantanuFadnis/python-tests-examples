def fibonacci(n):
    """Returns the nth element of the fibonacci series"""
    if n == 1 or n == 2:
        return 1
    first = 1
    second = 1
    res = 0
    for _ in range(2, n):
        res = first + second
        first = second
        second = res
    return res


def factorial(n):
    """Returns the factorial of a given integer"""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
