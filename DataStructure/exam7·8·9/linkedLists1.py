'''
추상적 자료구조(Abstract Data Structures)
    Data
        ex > 정수, 문자열, 레코드, …
    A set of operations
        ex > 삽입, 삭제, 순회, …
             정렬, 탐색, …

Node에는 Data와 Link(next)로 이루어져 있음
Node 내의 데이터는 다른 구조로 이루어질 수 있음
 문자열, 레코드, 다른 연결 list 등


ex > 67 -> 34 -> 58
    Head(67), Tail(58), of nodes(nodeCount) : 3

1. 특정 원소 참조 (k번째)
2. 리스트 순회
3. 길이 얻어내기
4. 원소 삽입
5. 원소 삭제
6. 두 리스트 합치기

배열 - O(1)
연결 리스트 - O(ｎ)

'''

'''
Programmers 정답
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

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    # From Me!
    # traverse(self) 채워넣기 (리스트 순회)
    # 연결 리스트의 노드들에 들어있는 순서대로 리턴하기.
    def traverse(self):
        answer = []
        linkedList = self.head

        # linkedList != None 과 같음
        while linkedList is not None:
            answer.append(linkedList.data)
            linkedList = linkedList.next
        return answer


# 이 solution 함수는 그대로 두어야 합니다.
def solution(x):
    return 0
