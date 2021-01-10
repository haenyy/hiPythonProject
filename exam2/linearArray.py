List = [20, 37, 58, 72, 91]
x = 65

data = enumerate(List)
for i, value in data:
    # print(i, value)
    if value > x:
        print('value > x, i =', i, 'value =', value, ', x = ', x)
        List.insert(i, x)
        break
print(List)

#     programmers(1) 정답
# def solution(L, x):
#     data = enumerate(L)
#     for i, value in data:
#          if value > x:
#             print('value > x, i =', i, 'value =', value, ', x = ', x)
#             L.insert(i, x)
#             break
#     answer = L
#     return answer

'''
L = ['Bob', 'Cat', 'Spam', 'Programmers']
print(L)
print(L[1])
print(L[-2])

# 원소 덧붙이기
# 끝에서 꺼내기
L.append('New')
print(L)
L.pop()
print(L)

# 원소 삽입하기
# 원소 삭제하기

Li = [20, 37, 58, 72, 91]

print(Li)
Li.insert(3, 65)
print(Li)
del (Li[2])
print(Li)
Li.pop(2)
print(Li)

# del(L[2])와 Li.pop()의 차이점?


# 원소 탐색하기

L.index('Spam')
print(L.index('Spam'))
'''
