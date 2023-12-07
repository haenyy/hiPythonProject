"""
Q. 정수가 담긴 리스트 num_list가 주어질 때,
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(num_list):
    answer = []
    even_cnt = 0  # 짝수
    odd_cnt = 0  # 홀수
    for i in num_list:

        if i % 2 == 0:
            even_cnt += 1
        else:
            odd_cnt += 1
    answer = [even_cnt, odd_cnt]
    print(answer)
    return answer


num_list = [1, 2, 3, 4, 5]  # result [2, 3]
# num_list = [1, 3, 5, 7]  # result [0, 4]

#solution(num_list)

"""
리스트 인덱싱을 활용한 다른 사람의 풀이다.
나머지를 인덱스로 사용할 생각은 전혀 해보지 못한 방법이다.
"""


def solution2(num_list):
    answer = [0, 0]
    for n in num_list:
        answer[n % 2] += 1
    print(answer)
    return answer


solution2(num_list)
