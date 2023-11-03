'''

Q. 중앙값은 어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미합니다.
예를 들어 1, 2, 7, 10, 11의 중앙값은 7입니다.
정수 배열 array가 매개변수로 주어질 때, 중앙값을 return 하도록 solution 함수를 완성해보세요.

'''
def solution(array):

    arr = sorted(array)

    answer = 0

    if len(arr) % 2 == 0:   # 짝수
        idx = len(arr) // 2
        print(arr)
        print(arr[idx])
        med = (arr[idx-1] + arr[idx]) // 2
        print("med?", med)


    else:   # 홀수
        idx = len(arr) // 2
        print(arr)
        print(arr[idx])
        answer = arr[idx]


    return answer


#array = [1, 2, 7, 10, 11]
array = [9, -1, 0, 4, 23, 6]

solution(array)