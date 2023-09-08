'''
재귀 알고리즘 기초
재귀함수 (Recursive Functions) = O(n)
하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
재귀함수는 종결 조건이 제일 중요하다.
알고리즘의 종결조건에 반드시 필요한 것임. ★
'''


def solution(x):
    if x <= 1:
        return x
    else:
        return solution(x-1) + solution(x-2)


for i in range(1, 10):
    print(solution(i))
