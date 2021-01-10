'''
재귀 알고리즘 응용
재귀함수 (Recursive Functions) = O(n)
하나의 함수에서 자신을 다시 호출하여 작업을 수행하는 것
재귀함수는 종결 조건이 제일 중요하다.
알고리즘의 종결조건에 반드시 필요한 것임. ★

재귀 알고리즘의 효율?
성능상 불리함 ↑

Q. 재귀적 이진 탐색
'''

L = [2, 3, 5, 6, 9, 11, 15]


def binsearch(L, x, lower, upper):
    #if lower == upper:     https://programmers.co.kr/questions/9908 참조하기. trivial case에 해당하는 것을 찾아야함.
    if lower > upper:
        return -1

    mid = (lower + upper) // 2

    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return binsearch(L, x, lower, mid - 1)
    else:
        return binsearch(L, x, mid + 1, upper)


print(binsearch(L, 6, 0, 6))

'''
programmers 정답

def solution(L, x, l, u):
    if l > u:
        return -1
    mid = (l + u) // 2
    if x == L[mid]:
        return mid
    elif x < L[mid]:
        return solution(L, x, l, mid - 1)
    else:
        return solution(L, x, mid + 1, u)

'''
