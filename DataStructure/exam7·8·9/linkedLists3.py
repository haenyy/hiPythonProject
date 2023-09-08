class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail

    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr

    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    # popAfter, popAt 추가
    def popAfter(self, prev):
        # 이전 노드의 다음이 없을 때 None return
        if prev.next is None:
            return None
        # 현재 노드는 이전 노드의 다음 노드
        curr = prev.next
        # 현재 노드의 다음 노드가 없을 때
        if curr.next is None:
            # 현재 노드의 다음 노드가 없고 노드의 개수가 1개일 때
            if self.nodeCount == 1:
                # 노드의 끝이 없음
                self.tail = None
            else:
                # 현재 노드의 다음노드가 없고 노드의 개수는 2개 이상일 때
                # 노드의 끝은 이전 노드임
                self.tail = prev

        # 이전의 다음 노드에 현재의 다음 노드를 연결시켜준다
        prev.next = curr.next
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError

        # 이전 노드는 현재 위치의 -1한 위치임
        prev = self.getAt(pos - 1)

        return self.popAfter(prev)


def solution(x):
    return 0
