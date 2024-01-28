'''
연산 ⊕는 두 정수에 대한 연산으로 두 정수를 붙여서 쓴 값을 반환합니다. 예를 들면 다음과 같습니다.

12 ⊕ 3 = 123
3 ⊕ 12 = 312
양의 정수 a와 b가 주어졌을 때, a ⊕ b와 2 * a * b 중 더 큰 값을 return하는 solution 함수를 완성해 주세요.

단, a ⊕ b와 2 * a * b가 같으면 a ⊕ b를 return 합니다.
'''
'''
def solution(a, b):
    answer = 0

    num1 = int(str(a) + str(b)) # int는 숫자로 변환 str은 문자로 변환
    num2 = 2 * a * b 

    if num1 == num2 :
        return num1
    elif num1 > num2 :
        return num1
    elif num2 > num1 :
        return num2
'''

# check에 a가 b보다 크면 [True]을 리턴 아니면 [False]을 리턴
# check = [True] if a > b else [False]

'''
오늘 해야 할 일이 담긴 문자열 배열 todo_list와 각각의 일을 지금 마쳤는지를 나타내는 
boolean 배열 finished가 매개변수로 주어질 때, todo_list에서 아직 마치지 못한 일들을 순서대로 담은 
문자열 배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ todo_list의 길이 1 ≤ 100
2 ≤ todo_list의 원소의 길이 ≤ 20
todo_list의 원소는 영소문자로만 이루어져 있습니다.
todo_list의 원소는 모두 서로 다릅니다.
finished[i]는 true 또는 false이고 true는 todo_list[i]를 마쳤음을, false는 아직 마치지 못했음을 나타냅니다.
아직 마치지 못한 일이 적어도 하나 있습니다.
'''
'''
def solution(todo_list, finished):
    answer = []

    for i in range(len(todo_list)) :
        if not finished[i] :
            answer.append(todo_list[i])

    return answer
    '''
# append는 배열에 값을 맨 뒤에 추가
# if not은 finished에 값이 true인지 false인지 참별인데 false만 실행되도록
'''
todo_list    ["problemsolving", "practiceguitar", "swim", "studygraph"]           
finished     [true, false, true, false]
result       ["practiceguitar", "studygraph"]
'''


'''
정수 배열 arr과 delete_list가 있습니다. 
arr의 원소 중 delete_list의 원소를 모두 삭제하고 
남은 원소들은 기존의 arr에 있던 순서를 유지한 
배열을 return 하는 solution 함수를 작성해 주세요.

제한사항
1 ≤ arr의 길이 ≤ 100
1 ≤ arr의 원소 ≤ 1,000
arr의 원소는 모두 서로 다릅니다.
1 ≤ delete_list의 길이 ≤ 100
1 ≤ delete_list의 원소 ≤ 1,000
delete_list의 원소는 모두 서로 다릅니다.

입출력 예
arr	                        delete_list	                    result
[293, 1000, 395, 678, 94]	[94, 777, 104, 1000, 1, 12]	    [293, 395, 678]
[110, 66, 439, 785, 1]	    [377, 823, 119, 43]	            [110, 66, 439, 785, 1]
'''
# 가장 좋은 코딩은 다른 사람이 알아보기 쉬운 코드
# 1번 방식
'''
def solution(arr, delete_list):
    answer = []

    for num in arr :
        if num not in delete_list :
            answer.append(num)

    return answer

# 2번 방식
def solution(arr, delete_list):
    return [num for num in arr if num not in delete_list]
'''
'''
정수가 담긴 리스트 num_list가 주어질 때, 
num_list의 원소 중 짝수와 홀수의 개수를 담은 배열을 return 하도록 
solution 함수를 완성해보세요.
'''
'''
def solution(num_list):
    answer = [0, 0]
    for i in num_list:
        if i%2==0:
            answer[0] = answer[0] + 1
        else:
            answer[1] = answer[1] + 1
    return answer
'''
'''
i팩토리얼 (i!)은 1부터 i까지 정수의 곱을 의미합니다. 
예를들어 5! = 5 * 4 * 3 * 2 * 1 = 120 입니다. 
정수 n이 주어질 때 다음 조건을 만족하는 가장 큰 정수 i를 
return 하도록 solution 함수를 완성해주세요.

i! ≤ n
제한사항
0 < n ≤ 3,628,800
입출력 예
n	        result
3628800	    10
7	        3
'''
def solution(n):
    answer = 0
    return answer