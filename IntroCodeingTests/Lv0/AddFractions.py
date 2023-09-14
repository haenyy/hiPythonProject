import math

'''
Q. 첫 번째 분수의 분자와 분모를 뜻하는 numer1, denom1, 두 번째 분수의 분자와 분모를 뜻하는 numer2, denom2가 매개변수로 주어집니다.
두 분수를 더한 값을 기약 분수로 나타냈을 때 분자와 분모를 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

기약분수를 활용한 분수의 덧셈을 해야 한다! 이 과정에서 참고할 것은 최대공약수를 구하는 유클리드 호제법.
해당 문제는 Lv0이지만 생각보다 어려웠다. 손으로 계산하는건 되는데 그 과정을 알고리즘으로 풀자니 잘 안풀렸다.
내가 짠 코드가 길고 지저분해서 다른 블로그들을 보면서 다른 방법으로도 참고 하면서 풀었다.
'''


def solution(numer1, denom1, numer2, denom2):
    # 첫번째 코드 > 정확성 40점
    answer = []
    num1 = numer1 * denom2
    num2 = numer2 * denom1

    den = denom1 * denom2
    num = num1 + num2

    maximum = 1
    for i in range(num, 1, -1):
        if num % i == 0 and den % i == 0:
            maximum = i
            print("maximum?", maximum)

    answer = [math.trunc(num / maximum), math.trunc(den / maximum)]

    print(answer)
    return answer


def solution2(numer1, denom1, numer2, denom2):
    # 두번째 코드 > 정확성 33.3점
    answer = []

    # 분모가 같을 때
    if denom1 == denom2:
        num = numer1 + numer2
        den = denom1
        answer = [num, den]
    # 분모가 다를 때
    else:
        div = numer1 * denom2 + numer2 * denom1
        maximum = 1
        # 약분 계산
        # 분모끼리 공약수 존재
        if denom1 % denom2 == 0 or denom2 % denom1 == 0:
            for i in range(div, 1, -1):
                if denom1 % i == 0 and denom2 % i == 0:
                    maximum = i
            if denom1 > denom2:
                denom2 *= maximum
                numer2 *= maximum
                num = numer1 + numer2
                den = denom1
                answer = [num, den]
            elif denom2 > denom1:
                denom1 *= maximum
                numer1 *= maximum
                num = numer1 + numer2
                den = denom2
                answer = [num, den]

        # 분모끼리 공약수 미존재
        else:
            num = numer1 * denom2 + numer2 * denom1
            den = denom1 * denom2
            answer = [num, den]

    print(answer)
    return answer


def solution3(numer1, denom1, numer2, denom2):
    # 세번째 코드 > 정확성 100점
    den = denom1 * denom2
    num = (numer1 * denom2) + (numer2 * denom1)

    # math.gcd 는 최대공약수를 구하는 라이브러리이다.
    # math.lcm 은 최소공배수를 구하는 라이브러리이다.
    gcd = math.gcd(num, den)
    num = num // gcd
    den = den // gcd

    answer = [num, den]
    print(answer)
    return answer

#9,2,1,3
#1, 2, 3, 4
#solution(9,2,1,3)
#solution2(1,2,3,4)
#solution2(9,2,1,3)
solution3(1,2,3,4)
