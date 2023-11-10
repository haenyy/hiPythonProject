"""
Q. 최빈값은 주어진 값 중에서 가장 자주 나오는 값을 의미합니다.
정수 배열 array가 매개변수로 주어질 때, 최빈값을 return 하도록 solution 함수를 완성해보세요.
최빈값이 여러 개면 -1을 return 합니다.

해당 문제가 69%의 정답율로 lv.0에 있을 문제인가 싶었던게 또 코드는 간단하다. 하지만 구현하기가 까다로웠고 생각하는데 많은 시간을 보냈다...
"""

def solution(array):
    answer = 0
    max = 0
    for i in set(array):
        if len(array) == 1:  # 배열에 하나의 값만 있을 때는 해당 값 return
            answer = i
        else:
            print(i, array.count(i))
            if max < array.count(i):        # 최빈값이 하나일 땐 해당 값 return
                max = array.count(i)
                answer = i
            elif max == array.count(i):     # 최빈값이 여러개일 때 -1 return
                answer = -1

    print(answer)

    return answer




array = [1, 2, 3, 3, 3, 4]
#array = [1, 1, 2, 2]
#array = [1]

solution(array)

"""
다른 사람의 풀이를 보고 감탄을 금치 못했다... 어떻게 이렇게 천재같은 생각을...? 하나씩 제거하는 방법으로 문제를 풀었다.
"""

def solution2(array):
    """

    :rtype: object
    """
    while len(array) != 0:
        for i, a in enumerate(set(array)):
            array.remove(a)
        if i == 0: return a
    return -1


solution2(array)