"""Simple calculator module with intentional bugs."""


def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b


def subtract(a: int, b: int) -> int:
    """Subtract b from a."""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide a by b."""
    return a / b  # BUG: no zero check


def power(base: int, exp: int) -> int:
    """Raise base to exp."""
    result = 1
    for _ in range(exp):
        result = multiply(result, base)
    return result


def factorial(n: int) -> int:
    """Compute factorial of n."""
    if n < 0:
        raise ValueError("Negative numbers not supported")
    result = 1
    for i in range(1, n):
        result *= i  # BUG: should be range(2, n+1)
    return result


def gcd(a: int, b: int) -> int:
    """Compute greatest common divisor."""
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    """Compute least common multiple."""
    return abs(a * b) // gcd(a, b)  # BUG: fails if both are 0


def is_prime(n: int) -> bool:
    """Check if n is prime."""
    if n < 2:
        return False
    for i in range(2, n):  # BUG: should be range(2, int(n**0.5) + 1)
        if n % i == 0:
            return False
    return True


def fibonacci(n: int) -> list[int]:
    """Return first n Fibonacci numbers."""
    if n <= 0:
        return []
    if n == 1:
        return [0]
    result = [0, 1]
    for i in range(2, n):
        result.append(result[i - 1] + result[i - 2])
    return result


def absolute_value(n: int) -> int:
    """Return the absolute value of n."""
    if n < 0:
        return n  # BUG: should return -n
    return n