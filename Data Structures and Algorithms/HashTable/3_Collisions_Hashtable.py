class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [ [] for i in range(self.MAX)]

    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)      
        return h % 10
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,val)
                found = True
                break
        if not found:
            self.arr[h].append((key,val))


    def __getitem__(self,key):
        h = self.get_hash(key)
        found = False
        for element in self.arr[h]:
            if element[0] == key:
                return print(element[1])
        
        

    def __delitem__(self,key):
        h = self.get_hash(key)
        for idx,element in enumerate(self.arr[h]):
            if element[0] == key:
                del self.arr[h][idx]
                break

if __name__ == "__main__":
    t = HashTable()

    t['march 6'] = 120
    t['march 8'] = 67
    t['march 9'] = 4
    t['march 17'] = 459

    t['march 6']
    t['march 17']
    print(t.arr)
    t.__delitem__('march 6')
    t['march 6']
    print(t.arr)
    t.__delitem__('march 17')
    t['march 17']
    print(t.arr)

    # print(t.arr)