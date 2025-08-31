def another_fun_challenge(input_value):
    a = 5 # O(1) --> Constant Time
    b = 10 # O(1) --> Constant Time
    c = 50 # O(1) --> Constant Time

    for i in range(input_value):
        x = i + 1 # O(n) --> Linear Time
        y = i + 2 # O(n) --> Linear Time
        z = i + 3 # O(n) --> Linear Time
        print(f"Loop 1 - i={i}, x={x}, y={y}, z={z}")

    for j in range(input_value):
        p = j * 2 # O(n) --> Linear Time
        q = j * 2 # O(n) --> Linear Time
        print(f"Loop 2 - j={j}, p={p}, q={q}")

    who_am_i = "I don't know" # O(1) --> Constant Time
    print(who_am_i)


# Example usage:
another_fun_challenge(5)


# Big O(4 + 3n + 2n) --> Linear Time