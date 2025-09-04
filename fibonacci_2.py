def fibonacci(n):   
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

# def fibonacci_iterative(n):
#     a, b = 0, 1
#     for i in range(n):
#         a, b = b, a + b
#     return a