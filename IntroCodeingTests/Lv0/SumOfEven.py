"""
Q. 정수 n이 주어질 때, n이하의 짝수를 모두 더한 값을 return 하도록 solution 함수를 작성해주세요.
"""


def solution(n):
    answer = 0
    for i in range(n+1):
        if i % 2 == 0:
            answer += i
    print(answer)
    return answer


n = 10  # result = 30
# n = 4 # result = 6

solution(n)


'''
가장 많이 좋아요를 받은 다른 사람의 풀이다.
sum 함수 내에 for문을 풀어 써 범위만큼 2씩 더하는 방법을 사용했다.
'''

def solution2(n):
    return sum([i for i in range(2, n + 1, 2)])


solution2(n)

'''
해당 풀이는 등차수열 2n 의 합 공식을 이용한 풀이다.
2x(x+1)/2
'''


def solution3(n):
    return 2*(n//2)*((n//2)+1)/2


solution3(n)