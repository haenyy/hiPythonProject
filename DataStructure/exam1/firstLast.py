from array import *


def solution(x, y):
    answer = y + x

    print('y = ', y, ', x = ', x, ', answer = ', answer)


earray = array('i', [5, 3, 8, 2])

a = earray[-1]  # 리스트의 제일 마지막 요소를 가져올 수 있는 가장 짧은것
b = earray[0]
c = earray[1]
d = earray[2]
e = earray[3]
print(a, b, c, d, e)

solution(a, b)
