class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class LinkedList:
    def __init__(self,head=None):
        self.head = head

    def insert_at_beginning(self,data):
        node = Node(data,self.head,None)
        self.head = node

    def printList(self):
        if self.head is None:
            print('Empty LinkedList!!!')
            return
        
        llstr = ''
        itr = self.head
        while itr:
            llstr += itr.data + ' --> '
            itr = itr.next
        
        print(llstr)
        

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None,None)
            return
        
        itr = self.head
        while itr:
            if itr.next is None:
                itr.next = Node(data,None,itr.prev)
                return
            itr = itr.next
    
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next
    
    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception('Invalid Index')
        
        if index == 0:
            self.insert_at_beginning(data)
        
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next.next,itr.prev)
                break
            count += 1
            itr = itr.next
    
    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert,itr.next,itr.prev)
                break
            itr = itr.next

    def remove_by_value(self, data):
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
    # Remove first node that contains data
    def get_last_node(self):
        itr = self.head
        while itr:
            itr = itr.next        
        return itr

    def print_forward(self):
    # This method prints list in forward direction. Use node.next
        itr = self.head
        while itr:
            print(f'{itr.data} -->', end = '')
            itr = itr.next
    
    def print_backward(self):
    # Print linked list in reverse direction. Use node.prev for this.
        if self.head is None:
            print('Empty LinkedList !!')

        last_node = self.get_last_node()
        itr = last_node
        while itr:
            print(f'linked list in reverse : {itr.data} -->' ,end='')
            itr = itr.prev
        
        



if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print_forward()
    ll.print_backward()
    # ll.printList()
    # ll.insert_after_value("mango","apple") # insert apple after mango
    # ll.printList()
    # ll.remove_by_value("orange") # remove orange from linked list
    # ll.printList()
    # ll.remove_by_value("figs")
    # ll.printList()
    # ll.remove_by_value("banana")
    # ll.remove_by_value("mango")
    # ll.remove_by_value("apple")
    # ll.remove_by_value("grapes")
    # ll.printList()
