strings = ['a', 'b', 'c', 'd']

# 4*4 = 16 bytes of storage

# push
# add e to the end of the array
strings.append('e') # O(1)

# pop
# remove the last item of the array
strings.pop() # O(1)

# insert is unshift in javascript
# add x to the beginning of the array   
strings.insert(0, 'x') # O(n)


# strings.splice(2, 0, 'alien')

strings[2:2] = ['alien']

print(strings)