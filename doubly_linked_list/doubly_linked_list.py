"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        currentNode = None #default state if it doesn't exist
        if self.length > 0: #it exists
            currentNode = self.head.value #store it because it does exist
            if self.length == 1: #is it lonely?
                self.head = None #off with it's head!
                self.tail = None #and it's tail!
            elif self.length > 1: #it's not lonely
                self.head = self.head.next #transplant it's head!
                self.head.prev = None #nuke it from orbit!
            self.length -= 1 #shrink the length

        return currentNode #returns none by default for a 0 case
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        current = self.tail
        if self.length > 0:
            self.length -= 1
        if current.prev is not None:
            current.prev.next = None
            self.tail = current.prev
        else:
            self.head, self.tail = None, None
        return current.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        new_head = self.delete(node) #store it
        self.add_to_head(new_head) #run add to head with it
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        new_tail = self.delete(node) #store it
        self.add_to_tail(new_tail) #run add to tail with it

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.length == 0:
            return None

        self.length -= 1 
        if self.head is self.tail: #is the node lonely?
            self.head, self.tail = None, None
            return node.value
        elif node is self.head: #is it not lonely, and is head
            self.head = self.head.next
            node.next, self.head.prev = None, None
            return node.value
        elif node is self.tail: #is it not lonely, not head, but is tail
            self.tail = self.tail.prev
            node.prev, self.tail.next = None, None
            return node.value
        else: #it's not lonely, it's not head or tail, but somewhere in between
            prev = node.prev #store the prev Node object 
            next = node.next #store the next Node objext
            prev.next = node.next #access the previous node's next, and assign it to the "next" node from above
            next.prev = node.prev #access the next's node's previous value and assign it to the "prev" node from above
            return node.value #seems like this should leak memory... but it passes the tests

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        currentNode = self.head
        max = 0

        while currentNode is not None:
            if currentNode.value > max:
                max = currentNode.value
            currentNode = currentNode.next

        return max