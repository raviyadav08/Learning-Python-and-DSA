class linkedlistnode:
    def __init__(self,data,nextNode=None):
        self.data=data
        self.nextNode=nextNode

class linkedlist:
    def __init__(self,head=None):
        self.head = head

    def insert(self,data):
        node = linkedlistnode(data)
        if self.head is None:
            self.head = node
            return
        
        currentNode = self.head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            currentNode = currentNode.nextNode

    def printlinkedlist(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'{currentNode.data} --> ',end='')
            currentNode = currentNode.nextNode
        print('None')

ll = linkedlist()
ll.insert('110')
ll.insert('120')
ll.insert('130')
ll.printlinkedlist()