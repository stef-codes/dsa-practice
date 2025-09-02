# Learn to cache
def add_to_80(n):
    return n + 80

add_to_80(5)

cache = {}
def memoize_add_to_80(n):
    if n in cache:
        return cache[n]
    else:
        print('long time')
        answer = n + 80
        cache[n] = answer
        return answer

# print(1, memoize_add_to_80(6))
# print(cache)
# print('-----------')
# print(2, memoize_add_to_80(6))

# Let's make that better with no global scope. This is closure in Python.
def memoize_add_to_80():
    cache = {}
    def inner(n):
        if n in cache:
            return cache[n]
        else:
            print('long time')
            answer = n + 80
            cache[n] = answer
            return answer
    return inner

memoized = memoize_add_to_80()
print(1, memoized(6))
# print(cache)
# print('-----------')
print(2, memoized(6))