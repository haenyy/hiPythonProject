"""
Q. 머쓱이는 추운 날에도 아이스 아메리카노만 마십니다. 아이스 아메리카노는 한잔에 5,500원입니다.
머쓱이가 가지고 있는 돈 money가 매개변수로 주어질 때,
머쓱이가 최대로 마실 수 있는 아메리카노의 잔 수와 남는 돈을 순서대로 담은 배열을 return 하도록 solution 함수를 완성해보세요.

"""

'''
실제 코테로 풀 때는 int로 형변환을 굳이 하지 않아도 됐지만 ','이 포함되는 문자열형에서 형변환을 시키다 보니 코드가 살짝 변경됐다.
실제로는 divmod() 한줄로 끝나는 쉬운 문제였다.
'''

def solution(money):
    money2 = int(money)
    cups, change = divmod(money2, 5500)
    answer = [cups, change]
    print(answer)
    return answer

# money = 2000
# money = 5500  # result [1,0]
money = 15000 # result [2,4000]
solution(money)


'''
해당 문제 풀이는 제일 많은 사람이 적용한 방법을 가져와봤다. divmod() 메서드를 사용하지 않고 단순 연산자로만 처리한 모습이다.
여기서 변수 할당을 하지않으면 return 문에 한 줄만으로도 적용 가능하다!
'''


def solution2(money):

    answer = [money // 5500, money % 5500]
    return answer