counter = 0
def inception(counter):
    print(counter)
    if counter > 3: 
        return 'done'
    counter += 1
    return inception(counter)

print(inception(counter))

# Tips for recursion        
# 1. Identify the base case 
# 2. Identify the recursive case
# 3. Call the function itself   
# 4. Make sure to return the function call  




