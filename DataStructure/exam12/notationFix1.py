'''
중위 표기법과 후위 표기법

중위표기법(infix notation) - 연산자(+, *, -, /)가 피연산자들의 사이에 위치
( A + B ) * ( C + D )
후위표기법(postfix notation) - 연산자가 피연산자들의 뒤에 위치
A B + C D + *

중위 표현식을 후위 표현식으로 변경

괄호의 처리
[중위] ( A + B ) * C
[후위] A B + C *
여는 괄호는 스택에 PUSH
닫는 괄호를 만나면 여는 괄호가 나올 때까지 POP 한다

[중위] A * ( B + C )
[후위] A B C + *
이 경우에는 괄호 안의 연산이 먼저 이루어져야하기 때문에
연산자를 만났을 때, 여는 괄호 너머까지 POP 하지 않도록 해야한다
그러므로 여는 괄호의 우선순위를 가장 낮게 설정한다

|+|
|(|
|*|  <- 이 순서로 쌓여야 한다.
￣
예제 1)
[중위] ( A + B ) * ( C + D )
[후위] A B + C D + *

예제 2)
[중위] ( A + ( B - C ) ) * D
[후위] A B C - + D *

[중위] A * ( B - ( C + D ) )
[후위] A B C D + - *

연산자의 우선순위 설정 (python dictionary 인 prec 이용)
prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

중위 표현식을 왼쪽부터 한 글자씩 읽어들이고
피연산자이면 그냥 출력하고 '('이면 스택에 push 하고
')' 이면 '(' 이 나올 때까지 스택에서 pop 하기
연산자이면 스택에서 이보다 높거나 같은 우선순위 것들을 pop 하기
그리고 이 연산자는 스택에 push 해둔다
표현식 끝에 가서 스택에 남아있는 연산자는 모두 pop 한다

덧셈 덧셈 또는 뺄셈 뺄셈이면 상관없지만
덧셈이나 뺄셈 뺄셈이나 덧셈이면 왼쪽 먼저 계산해야 한다

코드의 구현 - Hint
1. 스택의 맨 위에 있는 연산자와의 우선순위를 비교 (꺼내지 않고!) > 스택의 peek() 연산을 이용한다. 꺼내지는 않고 맨 위의 값만 비교
2. 스택에 남아 있는 연산자 모두 pop() 하는 순환문(반복문) > while not opStack.isEmpty(): 으로 구성할 수 있다

'''

import len


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


prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

# 진짜 어렵다 ㅠ 복습해야겠다
def solution(S):
    opStack = ArrayStack()
    answer = ''
    # 순환문을 돌린다
    for c in S:
        # 만약 c가 '(' 라면
        if c == '(':
            # 일단 스택에 넣어주고
            opStack.push(c)
        # c가 ')' 라면
        elif c == ')':
            # 일단 스택의 마지막에 '(' 가 들어가있지 않은지 확인한다.
            # '(' 가 있으면 ')' 를 꺼내줘야하고(pop)
            # '(' 가 없으면 먼저 스택에 쌓인 우선 순위 괄호가 없기 때문에 answer 에 쌓아준다.
            while opStack.peek() != '(':
                answer += opStack.pop()
            opStack.pop()
        # c가 '(', ')' 가 아니라면 ( 연산자이거나 피연산자이거나 )
        else:
            # prec 과 비교하여 해당 c 가 연산자인지 아닌지 확인한다.
            # c 가 연산자라면
            if c in prec:
                # 일단 스택이 비어있는지 확인한다
                if opStack.isEmpty():
                    # 스택이 비어있다 ? 연산자인데 비어있다 ? 일단 스택에 넣어준다.
                    opStack.push(c)
                # 스택이 안 비어있고, 스택 마지막에 쌓인 연산자가 prec 에 있는 연산자와 c 를 비교하여 우선순위가 높다면
                elif prec[opStack.peek()] >= prec[c]:
                    # ★ prec 에 있는 연산자보다 스택에 맨 마지막에 쌓인 연산자의 우선순위가 높다면
                    if prec[opStack.peek()] >= prec[c]:
                        # 스택에 있는걸 꺼내서 answer 에 담아준다
                        answer += opStack.pop()
                    # while 문 다 돌았으면 c 를 스택에 쌓아준다
                    opStack.push(c)
                # 스택이 비어있지도 않고 스택 마지막에 쌓인 연산자가 prec 에 있는 연산자와 c 를 비교하여 우선순위가 낮다면 (일단 맨 밑에 쌓고 봐야함)
                else:
                    # 스택에 쌓아준다
                    opStack.push(c)
            # c 가 피연산자라면
            else:
                # 어디에도 담지 않고 answer 에 바로 담아준다
                answer += c
    # 순환문 돌리면서
    while not opStack.isEmpty():
        # 스택에서 c 꺼내서 answer 에 담아준다
        answer += opStack.pop()
    # answer 을 리턴한다
    return answer
