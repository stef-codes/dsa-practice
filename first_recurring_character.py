"""
//Google Question

Find the first recurring character in an array: 

//Given an array = [2,5,1,2,3,5,1,2,4]:
//It should return 2

//Given an array = [2,1,1,2,3,5,1,2,4]:
//It should return 1

//Given an array = [2,3,4,5]:
//It should return undefined
"""

def first_recurring_character(arr):
     seen = {}
     i = 0 
     for num in arr:
          if num in seen: 
               return num
          else:
               seen[num] = i
               i += 1
     return None

"""
//Bonus... What if we had this:
// [2,5,5,2,3,5,1,2,4]
// return 5 because the pairs are before 2,2
"""

# Test cases
print(first_recurring_character([2,5,1,2,3,5,1,2,4]))  # 2
print(first_recurring_character([2,1,1,2,3,5,1,2,4]))  # 1
print(first_recurring_character([2,3,4,5]))            # None
print(first_recurring_character([2,5,5,2,3,5,1,2,4]))  # 5
