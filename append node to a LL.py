class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

    def getNext(self):
        return self.next

class LinkedList:
    def __init__(self, head):
        self.head = head

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def printList(self):
        node = self.head
        while(node):
            print(node.value)
            node = node.next

    def append(self, toAppend):
        if not self.head:
            self.head = toAppend
            return
        
        node = self.head
        
        while(node.next):
            node = node.next
            
        node.next = toAppend

def appendNode(linkedList, toAppend):
    if not linkedList: return None
    
    node = linkedList.getHead()
    
    if not node:
        linkedList.setHead(toAppend)
        return

    while(node.next):
        node = node.next

    node.next = toAppend  
        
    
if __name__ == "__main__":
    n1, n2, n3, n4 = Node(10), Node(20), Node(30), Node(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    linkedList = LinkedList(head)
    linkedList.setHead(None)
    linkedList.append(Node(50))
    appendNode(linkedList, Node(50))
    linkedList.printList()

