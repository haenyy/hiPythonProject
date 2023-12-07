"""
Q. 각에서 0도 초과 90도 미만은 예각, 90도는 직각, 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다.
각 angle이 매개변수로 주어질 때 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.
예각 : 0 < angle < 90
직각 : angle = 90
둔각 : 90 < angle < 180
평각 : angle = 180
"""


def solution(angle):
    answer = 0
    if 0 < angle < 90:
        answer = 1
    elif angle == 90:
        answer = 2
    elif 90 < angle < 180:
        answer = 3
    else:
        answer = 4
    return answer


# angle = 70  # result = 1
# angle = 91 # result = 3
angle = 180  # result = 4

'''
가장 많이 좋아요를 받은 다른 사람의 풀이이다. 숏코딩은 둘째치고 (angle % 90 > 0) 의 값이 True | False -> (1, 0)
으로 계산되기 때문에 1, 2, 3, 4 분기처리가 가능하다. 너무 똑똑한것 같다... 
'''


def solution2(angle):
    print((angle // 90) * 2)
    print((angle % 90 > 0))
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    print(answer)
    return answer


solution2(angle)
