

List = [64, 72, 83, 72, 54]
data2 = enumerate(List)
answer = []

# a = 72
# b = 83
# c = 49

y = 49

if y not in List:
    answer.append(-1)
else:
    for i, value in data2:
        if value == y:
            print(i, y, List.index(value))
            answer.insert(i, i)
print(answer)


#programmers(2) 정답
# def solution(L, x):
#     L2 = enumerate(L)
#     answer = []
#     if x not in L:
#         answer.append(-1)
#     else:
#         for i, value in L2:
#             if value == x:
#                 print(i, x, L.index(value))
#                 answer.insert(i, i)
#     return answer
