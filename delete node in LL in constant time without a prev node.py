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
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

    def setTail(self, tail):
        self.tail = tail

    def getTail(self):
        return self.tail

    def append(self, toAppend):
        if not self.head:
            self.head = toAppend
            self.tail = toAppend
            return
        
        tail.next = toAppend
        self.tail = toAppend

    def printList(self):
        node = self.head
        while(node):
            print(node.value)
            node = node.next

    def deleteNode(self, node):
        if not node: return
        if not node.next:
            raise Exception("The tail node cannot be deleted")
        node.value = node.next.value
        node.next = node.next.next
        
    
if __name__ == "__main__":
    n1, n2, n3, n4 = Node(20), Node(10), Node(20), Node(10)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    tail = n4
    linkedList = LinkedList(head, tail)
    linkedList.deleteNode(n3)
    linkedList.printList()


