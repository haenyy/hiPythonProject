from DataStructure.exam10.doublyLinkedLists1 import Node
from DataStructure.exam10.doublyLinkedLists1 import DoublyLinkedList

'''
스택(Stack)
자료 (data element) 를 보관할 수 있는 (선형) 구조
단, 넣을 때에는 한 쪽 끝에서 밀어 넣어야 하고 (push)
    꺼낼 때에는 같은 쪽에서 뽑아 꺼내야 하는 제약이 있음 (pop)
후입선출 (LIFO - Last-In First-Out) 특징을 가진다

비어있는 스택에서 데이터 원소를 꺼내려고 할 때 스택 언더플로우 (Stack Underflow) 발생
꽉차있는 스택에서 데이터 원소를 넣으려고 할 때 스택 오버플로우 (Stack Overflow) 발생

1. 배열(array)을 이용하여 구현
    Python 리스트와 메서드들을 이용
2. 연결 리스트(linked list)를 이용하여 구현
    지난 강의에서 했던 양방향 연결 리스트 이용

size()       - 현재 스택에 들어있는 데이터 원소의 수를 구함
isEmpty()    - 현재 스택이 비어 있는지를 판단
push(x)      - 데이터 원소 x를 스택에 추가
pop()        - 스택의 맨 위에 저장된 데이터 원소를 제거 (또한, 반환)
peek()       - 스택의 맨 위에 저장된 데이터 원소를 반환 (제거하지 않음)

수식의 괄호 유효성 검사.
알고리즘 설계 - 수식을 왼쪽부터 한 글자씩 읽어서:
    여는 괄호 (, {, [ 를 만나면 스택에 푸시
    닫는 괄호 ), }, ] 를 만나면
        1. 스택이 비어있으면 올바르지 않은 수식
        2. 스택에서 pop, 쌍을 이루는 여는 괄호인지 검사
             맞지 않으면 올바르지 않은 수식
끝까지 검사한 후, 스택이 비어 있어야 올바른 수식



'''


class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def solution(expr):
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        S = ArrayStack()
        for c in expr:
            if c in '({[':
                S.push(c)

            elif c in match:
                if S.isEmpty():
                    return False
                else:
                    t = S.pop()
                    if t != match[c]:
                        return False
        # 처음에 True 를 return 시켰는데, 끝까지 검사 후 스택에 무엇인가 남아있다면 괄호를 열었으나 닫지 않은 경우이므로
        # 올바르지 않다고 판단해야 한다. 그러므로 무조건 True 를 반환하는게 아닌 S.isEmpty() 를 반환해야 한다.
        return S.isEmpty()


class LinkedListStack:

    def __init__(self):
        self.data = DoublyLinkedList()

    def size(self):
        return self.data.getLength()

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        node = Node(item)
        self.data.insertAt(self.size() + 1, node)

    def pop(self):
        return self.data.popAt(self.size())

    def peek(self):
        return self.data.getAt(self.size()).data
