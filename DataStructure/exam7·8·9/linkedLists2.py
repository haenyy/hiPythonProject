'''
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

연결리스트의 원소 삽입의 복잡도
    맨 앞에 삽입 : O(1)
    중간에 삽입 : O(ｎ)
    맨 끝에 삽입 : O(1)

연결리스트의 원소 삭제의 복잡도
    맨 앞에 삭제 : O(1)
    중간에 삭제 : O(ｎ)
    맨 앞에 삭제 : O(ｎ)  - 처음부터 찾아가야함, prev를 찾을 수 없음. curr = tail ? ? 안됨.
'''


class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def __repr__(self):
        if self.nodeCount == 0:
            return 'LinkedList: empty'

        s = ''
        curr = self.head
        while curr is not None:
            s += repr(curr.data)
            if curr.next is not None:
                s += ' -> '
            curr = curr.next
        return s

    # concat 추가 (양방향 연결 리스트를 앞 뒤로 이어붙이는 메서드)
    def concat(self, L):
        if L.nodeCount == 0:
            return True

        first = L.head.next
        last = self.tail.prev

        last.next = first
        first.prev = last

        self.tail = L.tail
        self.nodeCount += L.nodeCount

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True

    def getLength(self):
        return self.nodeCount

    # From Me!
    # 원소 삭제
    def popAt(self, pos):
        # 삭제할 노드가 노드의 범위를 벗어나는 경우 exception 처리
        # 모르고 self.nodeCount+1 을 해벌임,, 멍총이,,
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        curr = None
        # 삭제할 노드가 첫 번째 일때
        if pos == 1:
            curr = self.head

            # 삭제할 노드가 첫 번째 이면서 노드가 1개 이하일 경우
            if self.nodeCount <= 1:
                self.head = None
                self.tail = None
            # 삭제할 노드가 첫 번째 이면서 노드가 2개 이상일 경우
            else:
                self.head = curr.next
        # 삭제할 노드가 두 번째 이상일 때
        else:
            prev = self.getAt(pos - 1)
            curr = prev.next

            # 삭제할 노드가 두 번째 이상이면서 노드의 갯수와 같을 경우
            if pos == self.nodeCount:
                prev.next = None
                self.tail = prev
            # 삭제할 노드가 두 번째 이상이면서 노드의 갯수와 같지 않을 경우
            else:
                prev.next = curr.next

        # 노드의 갯수를 -1 해준다
        self.nodeCount -= 1

        return curr.data

    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result

    def concat(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.nodeCount += L.nodeCount
