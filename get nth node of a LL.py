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

    def getNode(self, n):
        if n < 1: return None

        node = self.head
        count = 1

        while node:
            if n == count: return node.value
            node = node.next
            count += 1

        return None

def getNode(linkedList, n):
    if not linkedList or n < 1: return None

    node = linkedList.getHead()
    count = 1

    while(node):
        if count == n: return node.value
        count += 1
        node = node.next

    return None
        
    
if __name__ == "__main__":
    n1, n2, n3, n4 = Node(10), Node(20), Node(30), Node(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    head = n1
    linkedList = LinkedList(head)
    print(linkedList.getNode(ord("e")))
    print(getNode(linkedList, 2))

