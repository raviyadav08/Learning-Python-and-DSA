from collections import deque
import threading 
import time

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is Empty!")
            return
        return self.buffer.pop()
        
    def is_empty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
    def print_queue(self):
        return print(self.buffer)
    
def place_order(olist):
    for order in olist:
        print(f"Order placed for : {order}")
        q.enqueue(order)
        time.sleep(0.5)

def serve_order(q):
    while True:
        print(f'served order : {q.dequeue()}')
        time.sleep(2)

if __name__ == "__main__":
    q = Queue()
    orders = ['pizza','samosa','pasta','biryani','burger']
  
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order, args=(q,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

