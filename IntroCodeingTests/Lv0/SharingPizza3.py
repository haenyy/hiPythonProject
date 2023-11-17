"""
Q. 머쓱이네 피자가게는 피자를 두 조각에서 열 조각까지 원하는 조각 수로 잘라줍니다.
피자 조각 수 slice와 피자를 먹는 사람의 수 n이 매개변수로 주어질 때,
n명의 사람이 최소 한 조각 이상 피자를 먹으려면 최소 몇 판의 피자를 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

"""


def solution(slice, n):
    answer = 1
    while slice * answer < n:
        answer += 1
        print(answer)
    return answer


#solution(7, 10)  # result 2
solution(4, 12)  # result 3

'''
다른 사람의 풀이는 이렇게 간단했다. ceil 함수를 쓰는 코드도 여럿 보였는데 실수를 올림하여 정수로 반환하는 함수였다. 
return문에 ceil(n/slice) 만 추가하면 되는 간단한 코드다.
'''


def solution2(slice, n):
    return ((n - 1) // slice) + 1
