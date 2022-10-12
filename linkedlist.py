class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:

    def __init__(self,head=None):
        self.head = head

    def at_begining(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print("LinkedList Is Empty")
            return

        llstr = ''
        itr = self.head

        while itr:
            llstr += str(itr.data) + "-->>" if itr.next else str(itr.data)
            itr = itr.next
        print(llstr)

    def at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return 

        itr = self.head
         
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values_new(self,data_list):
        self.head = None
        for data in data_list:
            self.at_end(data)
    
    def insert_values(self,data_list):
        for data in data_list:
            self.at_end(data)
        
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_index(self, index, data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.at_begining(data)
            return

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node=Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
        
    def remove_at_index(self, index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid Index")

        if index==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head

        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            
            itr = itr.next
            count+=1

ll = LinkedList()
ll.at_begining(56)
ll.at_begining(765)
ll.at_end(87)
ll.at_end(34)
ll.print()
ll.insert_at_index(2,99)
# ll.insert_values_new(["banana","apple","pineapple","cherry"])
ll.print()
ll.remove_at_index(0)