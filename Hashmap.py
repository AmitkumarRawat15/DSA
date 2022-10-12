class HashTable:

    def __init__(self):
        self.MAX_SIZE = 100
        self.arr = [None for i in range(self.MAX_SIZE)]

    def get_hash(self,key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash%self.MAX_SIZE


    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __setitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = key

hash = HashTable()
print(hash.get_hash("march 6"))
print(hash.get_hash("march 17"))
hash["march 6"] = 120
hash["march 8"] = 67
hash["march 9"] = 4
hash["march 17"] = 459