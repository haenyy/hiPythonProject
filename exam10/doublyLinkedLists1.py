'''
양방향 연결 리스트 (Doubly Linked Lists)
    한 쪽으로만 링크를 연결하지 않고, 양쪽으로.
    앞으로도(다음 node) 뒤로도(이전 node) 진행 가능

Node 의 구조를 확장
리스트 처음(head)과 끝(tail)에 dummy node 를 두자
그러면 데이터를 담고있는 node 들은 모두 같은 모양이 된다.

리스트 마지막에 원소 삽입 할 때

'''


class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr.next.next:
            curr = curr.next
            s += repr(curr.data)
            if curr.next.next is not None:
                s += ' -> '
        return s

    def getLength(self):
        return self.nodeCount

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    # reverse() 추가. 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지
    # (tail 에서 head 방향으로) 순회하면서 방문하게 되는 node 에 들어있는 data item 을
    # 순회 순서에 따라 리스트에 담고 리턴 함
    def reverse(self):
        result = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            result.append(curr.data)
        return result

    # insertBefore() 추가. next 는 어느 node 의 앞에 새로운 node 를 삽입할지 지정하고,
    # newNode는 새로 삽입할 새로운 node 이다.
    def insertBefore(self, next, newNode):
        newNode.prev = next.prev
        newNode.next = next
        next.prev = newNode
        newNode.prev.next = newNode
        self.nodeCount += 1
        return True

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        # 위치가 노드를 절반으로 자른 것보다 뒤쪽에 있으면 뒤에서 하나하나 세도록
        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        # 위치가 노드를 절반으로 자른 것보다 앞쪽에 있으면 앞에서 하나하나 세도록
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # popAfter , poBefore, popAt 추가.
    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        next.prev = curr.prev
        curr.prev.next = next
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        if pos > self.nodeCount // 2:
            i = self.nodeCount
            curr = self.tail
            while i >= pos:
                curr = curr.prev
                i -= 1
        else:
            i = 1
            curr = self.head
            while i <= pos:
                curr = curr.next
                i += 1

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.nodeCount -= 1
        return curr.data
