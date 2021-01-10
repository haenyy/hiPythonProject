'''
선형탐색 (Linear Search) = O(n),  리스트의 길이에 비례하는 시간 소요
이진탐색 (Binary Search) = O(log n), 한 번 비교가 일어날 때마다 리스트 반씩 줄임(이미 정렬되어있는 경우에만 적용 가능)
'''

L = [2, 3, 5, 6, 9, 11, 15]
x = 10
answer = 0
lower = 0
upper = len(L) - 1

while lower <= upper:
    middle = (lower + upper) // 2

    if L[middle] == x:
        answer = middle
        break
    elif L[middle] < x:
        lower = middle + 1
    elif L[middle] > x:
        upper = middle - 1

    if lower == upper:
        answer = -1

print(answer)

'''
programmers 정답
def solution(L, x):
    answer = 0
    lower = 0
    upper = len(L)-1
    
    while lower <= upper:
        middle = (lower+upper) // 2
        
        if L[middle] == x:
            answer = middle
            break
        elif L[middle] < x:
            lower = middle + 1
        elif L[middle] > x:
            upper = middle - 1
            
        if lower == upper:
            answer = -1
        
    return answer
'''
