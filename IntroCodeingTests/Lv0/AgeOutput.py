"""
Q. 머쓱이는 40살인 선생님이 몇 년도에 태어났는지 궁금해졌습니다.
나이 age가 주어질 때, 2022년을 기준 출생 연도를 return 하는 solution 함수를 완성해주세요.

"""

'''
풀이할 때 그냥 2022라는 숫자를 하드코딩으로 했지만 standard 변수를 하나 만들어서 기준연도를 만들고
계산해도 괜찮다고 생각했다. 이 문제는 쉬워서 다른 사람 풀이는 굳이 가져오지 않았다.
'''

def solution(age):
    answer = 0

    print(2022 - age + 1)
    return answer


# age = 40  # return 1983
age = 23 # return 2000

solution(age)
