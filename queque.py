from collections import deque
import threading

import time

class Queue:
    
    def __init__(self):
        self.buffer = deque()
    
    def enqueue(self, val):
        print("Entering")
        self.buffer.appendleft(val)
        
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)


orders = ['pizza','samosa','pasta','biryani','burger']

q = Queue()
def take_order(orders):
    for i in orders:
        q.enqueue(i)
        time.sleep(0.5)

def server_order():
    while True:
        if not q.is_empty():
            od = q.dequeue()
            print("Now serving: ",od)
            time.sleep(2)
        else:
            break

t1 = threading.Thread(target=take_order,args=(orders,))
t2 = threading.Thread(target=server_order)

t1.start()
t2.start()

t1.join()
t2.join()