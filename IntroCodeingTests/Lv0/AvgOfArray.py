"""
Q. 정수 배열 numbers가 매개변수로 주어집니다. numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.
"""


def solution(numbers):
    answer = 0
    for i in numbers:
        answer += i
        #print(answer)

    answer = answer/len(numbers)
    print(answer)
    return answer


#numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # result 5.5
numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99] # result 94.0

solution(numbers)

"""
numpy 라이브러리를 사용한 다른 사람의 풀이도 있었지만 이렇게 합계에서 갯수를 나누는 간단한 방식의 풀이도 있었다. 
"""


def solution2(numbers):
    return sum(numbers) / len(numbers)