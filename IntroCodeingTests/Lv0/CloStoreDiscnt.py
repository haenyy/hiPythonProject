import math
'''
Q. 머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
   구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
'''
def solution(price):
    # 코테 정확성 테스트 시 테스트 케이스 13, 14번을 통과하지 못해서 계속 실패했었는데
    # 아마도 return 시 소숫점 이하 버리는 구문을 넣지 않아서 그랬던 것 같다.

    answer = 0

    if price >= 500000:
        answer = price * 0.8
    elif price >= 300000:
        answer = price * 0.9
    elif price >= 100000:
        answer = price * 0.95
    else :
        answer = price

    print(math.trunc(answer))
    return math.trunc(answer)

solution(1000000)

