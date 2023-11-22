"""
Q. 정수가 들어 있는 배열 num_list가 매개변수로 주어집니다.
num_list의 원소의 순서를 거꾸로 뒤집은 배열을 return하도록 solution 함수를 완성해주세요.
"""


def solution(num_list):
    # 1. 슬라이싱 사용 (원본 리스트의 순서는 바뀌지 않음)
    # reversed_num_list = num_list[::-1]
    # answer = reversed_num_list

    # 2. reverse() 메서드 사용 (원본 리스트의 순서가 바뀜)
    # 왜 이건 None이라고 나오지....????
    # answer = num_list.reverse()

    # 3. 내장함수 reversed() 사용
    reversed_num_list = list(reversed(num_list))
    answer = reversed_num_list

    # 이외 numpy 를 사용한 array 뒤집기도 존재함

    print(answer)
    return answer


num_list = [1, 2, 3, 4, 5]  # return [5, 4, 3, 2, 1]
# num_list = [1, 1, 1, 1, 1, 2] # return [2, 1, 1, 1, 1, 1]
# num_list = [1, 0, 1, 1, 1, 3, 5] # return [5, 3, 1, 1, 1, 0, 1]

solution(num_list)