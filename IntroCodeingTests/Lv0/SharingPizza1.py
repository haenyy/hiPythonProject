"""
Q. 머쓱이네 피자가게는 피자를 일곱 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 주어질 때,
모든 사람이 피자를 한 조각 이상 먹기 위해 필요한 피자의 수를 return 하는 solution 함수를 완성해보세요.

"""


def solution(n):
    answer = 0
    if n <= 7:
        answer = 1
    else:
        need_pizza = 0
        while (1):
            need_pizza += 1
            if 7 * need_pizza >= n:
                answer = need_pizza
                break
    print(answer)
    return answer


'''
solution2는 다른 사람의 풀이다. 난 몫을 구하는 연산자를 쓰지 않고 길게 풀어서 풀이했는데
몫을 구하는 연산자를 쓰면 한줄로 끝나는 것이다... 어떤 개발자가 댓글을 달았는데 당신 같은 천재들은 죽었으면 좋겠어요... 라고...

'''


def solution2(n):
    return (n - 1) // 7 + 1


# solution(7) # result 1
# solution(1) # result 1
# solution(15) # result 3
solution(24)  # result 4
solution2(8)
