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
        
        self.tail.next = toAppend
        self.tail = toAppend

    def printList(self):
        node = self.head
        while(node):
            print(node.value)
            node = node.next

    def lengthOfCycleIfExists(self):
        if not self.head: return None
        fastPointer = head
        slowPointer = head

        while(fastPointer):
            fastPointer = fastPointer.next
            if not fastPointer: return 0
            if fastPointer == slowPointer: break

            fastPointer = fastPointer.next
            if fastPointer == slowPointer: break

            slowPointer = slowPointer.next
            
        count = 0
        slowPointer = slowPointer.next
        count += 1
        while(fastPointer!=slowPointer):
            slowPointer = slowPointer.next
            count += 1

        return count

    def startingNodeOfTheCycle(self):
        if not self.head or not self.tail: return None
        cycleLength = self.lengthOfCycleIfExists()

        laggingPointer = head
        leadingPointer = head

        for i in range(cycleLength):
            leadingPointer = leadingPointer.next

        while(leadingPointer != laggingPointer):
            leadingPointer = leadingPointer.next
            laggingPointer = laggingPointer.next

        return leadingPointer.value
    
if __name__ == "__main__":
    n1, n2, n3, n4 = Node(90), Node(20), Node(30), Node(40)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n5 = Node(50)
    head = n1
    tail = n4
    linkedList = LinkedList(head, tail)
    linkedList.append(n5)
    n5.next = n2        
    print(linkedList.startingNodeOfTheCycle())


