import queue

Q = queue()
dir(Q)

'''
Queue ?

자료(Data Element)를 보관할 수 있는 (선형) 구조

단, 넣을 땐 한 쪽 끝에서 밀어 넣어야하고 (enqueue 연산)
꺼낼 땐 반대 쪽에서 뽑아 꺼내야 하는 제약이 있음 (dequeue 연산)

선입선출 (FIFO - First-In First-Out) 특징을 가짐

1. 배열을 이용하여 구현
python 리스트와 메서드들을 이용

2. 연결 리스트를 이용하여 구현
이전 강의에서 마련한 양방향 연결리스트 이용

연산의 정의
size() - 현재 큐에 들어있는 데이터 원소의 수를 구함
isEmpty() - 현재 큐가 비어있는지 판단
enqueue(x) - 데이터 원소 x를 큐에 추가
dequeue() - 큐의 맨 앞에 저장된 데이터 원소를 제거(또한, 반환)
peek() - 큐의 맨 앞에 저장된 데이터 원소를 반환 (제거하지 않음)

Q = Queue()
Q.enqueue(A)
Q.enqueue(B)
r1 = Q.dequeue() # A
r2 = Q.dequeue() # B

size() > O(1)
isEmpty() > O(1)
enqueue() > O(1)
★ dequeue() > O(ｎ) queue 의 길이에 비례함. 맨 앞 원소를 꺼내면 뒤에 있는 원소들이 순차적으로 앞당기게 되기 때문
peek() > O(1)

'''


class ArrayQueue:
    def __init__(self):  # 빈 큐를 초기화
        self.data = []

    def size(self):  # 큐의 크기를 리턴
        return len(self.data)

    def isEmpty(self):  # 큐가 비어있는지 판단
        return self.size() == 0


class ArrayStack:
    def enqueue(self, item):  # 데이터 원소를 추가
        self.data.append(item)

    def dequeue(self):  # 데이터 원소를 삭제(리턴)
        return self.data.pop(0)

    def peek(self):  # 큐의 맨 앞 원소 반환
        return self.data[0]
