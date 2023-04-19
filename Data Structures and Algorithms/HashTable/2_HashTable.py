class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        
        return h % 10
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        self.arr[h] = val

    def __getitem__(self,key):
        h = self.get_hash(key)
        return print(self.arr[h])

    def __delitem__(self,key):
        h = self.get_hash(key)
        del self.arr[h]

if __name__ == "__main__":
    t = HashTable()
    t.__setitem__('march 6',130)
    t.__setitem__('march 9',20)
    t.__setitem__('dec 17', 25)

    print(t.arr)
    t['march 6']
    t['march 1'] = 100
    print(t.arr)


    t.__delitem__('march 6')
    t.__delitem__('march 1')
    print(t.arr)
