"""
Q. 머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때,
n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를
return 하도록 solution 함수를 완성해보세요.

"""

def solution(n):
    answer = 0
    need_pizza = 0
    while(1):
        need_pizza += 1
        if 6 * need_pizza % n == 0:
            answer = need_pizza
            break
    print(answer)
    return answer


'''
solution2 는 제일 많은 사람들이 코딩한 방식이다. 나같은 경우는 while문을 무한으로 돌리면서 if 조건에 걸리면 break문을 만나 빠져나가기 때문에
반복문에 지양해야할 요소를 사용했는데 solution2처럼 while문에 조건을 제대로 걸어서 코딩하는게 바람직해 보인다.
'''

def solution2(n):
    answer = 1
    while answer * 6 % n != 0:
        answer += 1
    return answer


#solution(6) # result 1
#solution(10) # result 5
solution(4) # result 2