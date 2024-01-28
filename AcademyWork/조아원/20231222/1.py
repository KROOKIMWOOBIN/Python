# N명의 학생의 성적을 랜덤하게 입력 받아
# 오름 차순 및 내림 차순으로 정렬할 수 있는 프로그램을 만들어라
# 내장 함수 사용 금지X

num = int(input("학생 수 입력 >>> "))

jumsuList = [0 for i in range(num)]

for i in range(num) : 
    jumsuList[i] = int(input(f"{i + 1}번째 점수 입력 >>>"))

typeChoice = int(input("1. 오름차순 2. 내림차순 >>>"))

if typeChoice == 1 :
    for i in range(len(jumsuList) - 1) :
        ch = 0
        for i in range(len(jumsuList)):
            for j in range(len(jumsuList) - 1):
                if jumsuList[j] > jumsuList[j + 1]:
                    temp = jumsuList[j]
                    jumsuList[j] = jumsuList[j + 1]
                    jumsuList[j + 1] = temp
elif typeChoice == 2:
    for i in range(len(jumsuList) - 1) :
        ch = 0
        for i in range(len(jumsuList)):
            for j in range(len(jumsuList) - 1):
                if jumsuList[j] < jumsuList[j + 1]:
                    temp = jumsuList[j]
                    jumsuList[j] = jumsuList[j + 1]
                    jumsuList[j + 1] = temp
else :
    print("다시 입력해주세요")

for i in range(len(jumsuList)) :
    print(f"{i + 1}번째 학생 점수 : {jumsuList[i]}")