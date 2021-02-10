class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def setNext(self, next):
        self.next = next

    def getNext(self):
        return self.next

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key    

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value


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

    def reverse(self):
        if not self.head or not self.tail: return None

        tailToBe = self.head
        previous = None
        current = self.head
        next = self.head.next

        while(next):
            current.next = previous
            previous = current
            current = next
            next = next.next
        current.next = previous

        self.head = current
        self.tail = tailToBe

        return self.head

class Document:
    def __init__(self, document, words):
        self.document = document
        self.words = words
        self.linkedList = LinkedList(None, None)
        self.map = {}
        self.maxLength = 0
        self.headMax = None
        self.tailMax = None
        self.documentAsList = self.document.split(" ")
        

    def deleteFromLinkedList(self, node):
        if self.linkedList == None or node == None: return
        if node.getKey() == linkedList.getHead().getKey():
            linkedList.setHead(linkedList.getHead().getNext())
        else:
            node.getPrevious().setNext(node.getNext())

    def findLengthOfSubstring(self):
        
        print()

    def findShortestSubstring(self):
        if not document or not words or len(words) == 0: return None
        if len(document) == 0: return 0

        self.shortestSubstring()

        shortestSubstring = ""

        for i in range(self.headMax.value, self.tailMax.value+1):
            shortestSubstring += documentAsList[i] + " "

        return shortestSubstring[:-1] 

    def shortestSubstring(self):
        cursor = 0
        for index, word in enumerate(self.documentAsList):
            if word in words:
                if word in map:
                    node = map[word]
                    self.deleteFromLinkedList(node)
                else:
                    node = Node(word, index)
                    map[word] = node
                linkedList.append(node)
                if len(map) == len(words):
                    length = findLengthOfSubstring()
                    if length > maxLength:
                        maxLength = length
                        self.headMax = self.linkedList.getHead()
                        self.tailMax = self.linkedList.getTail()
                        
    def shortestSubstring(self):
        while documentReader.hasNextWord():
            wordTuple = documentReader.getNextWord()
            word = wordTuple[0]
            startingIndex = wordTuple[1]
            if word in words:
                if word in map:
                    node = map[word]
                    self.deleteFromLinkedList(node)
                else:
                    node = Node(word, startingIndex)
                    map[word] = node
                linkedList.append(node)
                if len(map) == len(words):
                    length = findLengthOfSubstring()
                    if length > maxLength:
                        maxLength = length
                        self.headMax = self.linkedList.getHead()
                        self.tailMax = self.linkedList.getTail()                        
                    
                
                
class DocumentReader:
    def __init__(self, document):
        self.document = document
        self.cursor = 0
        self.docLength = len(document)
        self.nextWord = None

    def hasNextWord(self):
        if not self.document or self.docLength == 0: return False
        if cursor == 0: return True
        while cursor < docLength:
            if cursor == docLength - 2: return False
#            if document[cursor] == " ":
                        
        
            
        
    
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
    n5.next = None
    linkedList.reverse()
    linkedList.printList()

for i in (enumerate("pradip lamsal".split(" "))):
    print(i)
a = {1:2, 2:3}
print(max(2,5))
