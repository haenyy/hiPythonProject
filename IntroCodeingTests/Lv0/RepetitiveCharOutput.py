"""
Q. 문자열 my_string과 정수 n이 매개변수로 주어질 때,
my_string에 들어있는 각 문자를 n만큼 반복한 문자열을 return 하도록 solution 함수를 완성해보세요.
"""


def solution(my_string, n):
    answer = ''
    for i in my_string:
        answer += i * n

    print(answer)
    return answer


my_string = "hello"
n = 3
# result "hhheeellllllooo"

#solution(my_string, n)

'''
한 줄로 완성한 다른사람의 풀이를 가져와봤다.
join 함수로 리스트를 문자열로 합치는 방법을 사용했다.
이런 방법과 함께 내가 사용한 방법은 문자열을 더하는 방법을 사용했다.
'''


def solution2(my_string, n):
    print(''.join(i * n for i in my_string))
    return ''.join(i * n for i in my_string)


solution2(my_string, n)
