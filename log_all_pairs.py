# Log all pairs of array
# O(n^2) --> Quadratic Time
boxes = ['a', 'b', 'c', 'd', 'e']

def log_all_pairs_of_array(array):
    for i in range(len(array)):
        for j in range(len(array)):
            print(array[i], array[j])

log_all_pairs_of_array(boxes)
