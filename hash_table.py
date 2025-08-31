# Building a hash table from scratch

class HashTable:
    def __init__(self, size):
        self.data = [None] * size   # fixed-size list

# create a hash function to hash the key
    def _hash(self, key):
        hash_value = 0
        for i in range(len(key)):
            hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
        return hash_value

# add a value to the key in the hash table
    def set(self, key, value):
        index = self._hash(key)
        if not self.data[index]:
            self.data[index] = []
        self.data[index].append([key, value])  # collision handling with chaining


# return the value of the key
    def get(self, key):
        index = self._hash(key)
        bucket = self.data[index]
        if bucket:
            for pair in bucket:
                if pair[0] == key:
                    return pair[1]
        return None


# Usage
my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000)
print(my_hash_table.get('grapes'))  # 10000
my_hash_table.set('apples', 9)
print(my_hash_table.get('apples'))  # 9
