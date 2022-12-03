class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def add_to_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def printLL(self):
        if self.head is None:
            print("Empty Linked List")

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next

        print(llstr)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count +=1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at_index(self, data, index):
        if index < 0 or index >= self.get_length():
            print("Invalid Index")

        if index == 0:
            self.add_to_beginning(data)

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(data,itr.next)
                break
            itr = itr.next
            count +=1

ll = LinkedList()

ll.printLL()
ll.add_to_beginning(5)
ll.add_to_beginning(67)
ll.insert_at_end(3456)
ll.add_to_beginning(579)
ll.printLL()
ll.remove_at(2)
ll.remove_at(0)
ll.insert_at_index("Amit",0)
ll.printLL()