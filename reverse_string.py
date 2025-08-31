def reverse_string(s):
    array_str = list(s)
    reversed_array = []

    def add_to_array(array):
        if array:
            reversed_array.append(array.pop())
            add_to_array(array)

    add_to_array(array_str)
    return ''.join(reversed_array)

print(reverse_string("yoyo master"))  # "retsam oyoy"

    
def reverse_string_recursive(s):
    if s == "":
        return ""
    else:
        return reverse_string_recursive(s[1:]) + s[0]

print(reverse_string_recursive("yoyo master"))