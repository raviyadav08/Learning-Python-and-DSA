class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insert_node_at_start(self,data):
        if self.head is None:
            self.head = Node(data,next = None)
            return
        else:
            self.head = Node(data,self.head)
            return

    def print_LinkedList(self):
        if self.head is None:
            print("LinkedList is empty!")
            return
        
        itr = self.head
        while itr:
            print(f'{itr.data} ---> ',end='')
            itr = itr.next
        print("")
    
    def insert_node_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
    
    def insert_values(self,datalist):
        self.head = None
        for data in datalist:
            self.insert_node_at_end(data)
    
    def get_length(self):
        count = 0
        if self.head is None:
            return count
        
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_node_at_start(data)

        itr = self.head
        count = 0
        
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next
    
    def remove_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
        
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next

    def remove_by_value(self,data):
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                return
            itr = itr.next

if __name__ == "__main__":
    ll = LinkedList()
    # ll.insert_node_at_start(1)
    # ll.insert_node_at_start(2)
    # ll.insert_node_at_end(3)
    # ll.insert_node_at_end(4)
    # ll.insert_node_at_start(1)
    # ll.insert_values(["mango","banana","grapes","orange"])
    # ll.remove_at(0)
    # ll.print_LinkedList()
    # print(ll.get_length())

    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_LinkedList()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_LinkedList()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_LinkedList()
    ll.remove_by_value("figs")
    ll.print_LinkedList()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_LinkedList()