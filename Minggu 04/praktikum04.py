''' 
    simple and tail recursive python program to
    reverse a linked list
'''
# node class
class Node:
    # constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    # function to initialize head
    def __init__(self):
        self.head = None
    def reverseUtil(self, curr, prev):
        # if last node mark it head
        if curr.next is None:
            self.head = curr
            # update next to prev node
            curr.next = prev
            return
        # save curr.next node for recursive call
        next = curr.next
        # and update next
        curr.next = prev
        self.reverseUtil(next, curr)
        # this function mainly calls reverseUtil()
        # with previous as Node
    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
        # function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        # utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
# drive program
llist = LinkedList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print("Given linked list")
llist.printList()
llist.reverse()
print("\nReverse linked list")
llist.printList()