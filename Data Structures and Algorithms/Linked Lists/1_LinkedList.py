class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_beginning(self,data):
        if self.head is None:
            self.head = Node(data,None)
        else:
            self.head = Node(data,self.head)

    def insert_node_at_end(self,data):
        if self.head == None:
            self.head = Node(data,None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)

    def insert_node(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_node_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_data_at(self,index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index!")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next 
            count += 1

    def insert_at(self,index,data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_node_at_beginning()

        count = 0 
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
            count += 1
            itr = itr.next

    def print_linkedlist(self):
        if self.head is None:
            print("Linked List is Empty!!!")

        itr = self.head
        while itr:
            print(f'{itr.data} ---> ',end='')
            itr = itr.next
        print()
    
 
    def insert_after_value(self,data_after,data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert,itr.next)
                itr.next = node
                break
            itr = itr.next
    
    def remove_by_value(self,data):
        if self.head is None:
            return
        
        if self.head.data == data:
            self.head = self.head.next
            return
        
        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

if __name__ == "__main__":
    
    ll = LinkedList()
    ll.insert_node(["banana","mango","grapes","orange"])
    ll.print_linkedlist()
    ll.insert_after_value("mango","apple") # insert apple after mango
    ll.print_linkedlist()
    ll.remove_by_value("orange") # remove orange from linked list
    ll.print_linkedlist()
    ll.remove_by_value("figs")
    ll.print_linkedlist()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print_linkedlist()
