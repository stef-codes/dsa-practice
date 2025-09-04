def fibonacci(n):   
    cache = {}  # O(n)
    if n < 2:
        return n
    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]
    #   return fibonacci(n - 1) + fibonacci(n - 2)  # O(2^n)

print(fibonacci(10))

# def fibonacci_iterative(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a