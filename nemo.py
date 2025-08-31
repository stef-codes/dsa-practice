# O(n) --> Linear Time
import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill', 'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = ['nemo'] * 100


def find_nemo(array):    
    # print('running') # fix this to run 10 times

    for i in range(len(array)):
        print('running') # fix this to run 10 times
        if array[i] == 'nemo':
            print('Found Nemo!')
            break
    # print(f'Call to find Nemo took {(t1 - t0) * 1000:.2f} milliseconds')
   # print(f'Call to find Nemo took {(t1 - t0)} milliseconds')
find_nemo(everyone) 


# O(1) --> Constant Time
"""
boxes = [0, 1, 2, 3, 4, 5]
def print_first_two_boxes(boxes):
    print(boxes[0]) # O(1)  --> Constant Time                       
    print(boxes[1]) # O(1)  --> Constant Time
print_first_two_boxes(boxes); # O(2)  --> Linear Time
"""






