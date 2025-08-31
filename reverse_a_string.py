def reverse_a_string(str):
 chars = list(str) 
 left, right = 0, len(chars) -1 

 for i in range(len(chars)): 
    if left >= right:
        break
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1
 return "".join(chars)
 
print(reverse_a_string("hello"))   # "olleh"
print(reverse_a_string("python")) 



  

