# What is the Big O of the below function? (Hint, you may want to go line by line)
"""
def another_function():
    # Placeholder for whatever logic you need
    print("another_function() was called")

def fun_challenge(input_list):
    a = 10
    a = 50 + 3

    for i in range(len(input_list)):
        another_function()
        stranger = True
        a += 1

    return a

# Example usage
data = [1, 2, 3, 4, 5]
result = fun_challenge(data)
print("Final value of a:", result)
"""

# Count operations
def another_function():
    # Placeholder for whatever logic you need
    print("another_function() was called")

def fun_challenge(input_list):
    operation_count = 0

    # Step 1
    a = 10 # O(1)
    operation_count += 1   # a = 10

    # Step 2
    a = 50 + 3 # O(1)
    operation_count += 1   # a = 50 + 3

    # Step 3 - Loop
    for i in range(len(input_list)):
        another_function() # O(n) --> Linear Time
        operation_count += 1   # another_function() call

        stranger = True # O(n) --> Linear Time
        operation_count += 1   # stranger assignment

        a += 1 # O(n) --> Linear Time
        operation_count += 1   # increment a

    # Step 4
    operation_count += 1  # return statement # O(1) --> Constant Time           
    return a, operation_count
# Big O(3 + 3n) --> Linear Time

# Example usage
data = [1, 2, 3, 4, 5]
final_a, ops = fun_challenge(data)
print(f"\nFinal value of a: {final_a}")
print(f"Total operations: {ops}")
