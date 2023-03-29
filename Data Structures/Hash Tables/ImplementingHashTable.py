
# Creating a HashTable
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]
    
    # Generating the hash value of a key
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val
    
    def get(self,key):
        h = self.get_hash(key)
        return self.arr[h]


if __name__ == '__main__':
    t = HashTable()
    # print(t.get_hash('march 6'))
    t.add('march 6',130)
    print(t.get('march 6'))
