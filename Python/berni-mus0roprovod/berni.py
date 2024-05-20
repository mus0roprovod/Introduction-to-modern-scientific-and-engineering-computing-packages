def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
    
def binom(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

def berni(n, k):
    coeff = binom(n, k)
    def bernstein_poly(x):
        return coeff * (x ** k) * ((1 - x) ** (n - k))
    return bernstein_poly
