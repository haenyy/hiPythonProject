"""
Q. 문자열 my_string과 문자 letter이 매개변수로 주어집니다.
my_string에서 letter를 제거한 문자열을 return하도록 solution 함수를 완성해주세요.
(대소문자 구분)
"""


# 정확성 75%
def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i == letter:
            answer = my_string.replace(i, '')
    print(answer)
    return answer


# 정확성 100%
def solution2(my_string, letter):
    answer = ''
    for i in my_string:
        answer = my_string.replace(letter, '')
    return answer


'''
처음에 내가 짠 코드는 if문을 사용하여 my_string의 문자와 파라미터로 입력받은 letter를 비교하여 같으면 
공백으로 대체하는 것이었다. 코드 제출 시 75% 정확성이 나와서 다시 짠 코드는 아예 if문을 제거한 코드였다.
my_string 을 for문으로 돌리며 letter와 일치하는 문자를 공백으로 대체하는 코드다.
이렇게 하니 정확성 100%가 나왔는데 생각해보니 if문을 사용할거면 letter와 일치하지 않는 문자열을 찾아서
append나 += 처리를 하는것이 나아보인다.
'''

# my_string = "abcdef" # BCBdbe
my_string = "BCBdbe"
letter = "B"  # B
# result = "abcde"  Cdbe

solution(my_string, letter)
solution2(my_string, letter)
