import random
#----------------------------------------------------------
# 구분합
# 배열의 0번지 1번지 더하고 다음은 1번지 2번지 더한 값
# 예 입력이 2 4 일 경우 데이터가 5 4 3 2 1 일때 답 9
#----------------------------------------------------------
#exlist = []

#for i in range(20) :
#    exlist.append(random.randrange(0, 100))

#exlist.sort()
#print(exlist)
#i = int(input('몇번째 데이터를 원하시나요 >>> '))
#data = exlist[i - 1]
#print(i,'번째 데이터 = ',data)
#----------------------------------------------------------
#count = 1
#exlist2 = []
#while count <= 10 :
#    num = random.randrange(0, 51)
#    if num not in exlist2 :
#        exlist2.append(num)
#        count += 1
#print(exlist2)
#
#for i in range(2) : # 가장 작은 값 삭제 2번 반복
#    mvalue = min(exlist2) # 작은 값을 찾아 mvalue에 넣어줌
#    di = exlist2.index(mvalue) # 값의 위치를 찾아 di에 넣음
#    del(exlist2[di]) # 그 값이 있는 위치 삭제
#    print('삭제할 값 >>> ', mvalue)
#print(exlist2)
#----------------------------------------------------------
#list1 = []
#list2 = []
#value = 1
#for i in range(0, 3) :
#    for j in range(0, 4) :
#        list1.append(value)
#        value += 1
#    list2.append(list1)
#    list1 = []
#for i in range(0, 3) :
#    for j in range(0, 4) :
#        print("%d " % list2[i][j], end = "") # 엔터 값을 없애줌
#    print("")
#----------------------------------------------------------
#list1 = []
#list2 = []
#value = 0
#for i in range(0, 3) :
#    for j in range(0, 4) :
#        list1.append(value)
#        value += 5
#    list2.append(list1)
#    list1 = []
#for i in range(0, 3) :
#    for j in range(0, 4) :
#        print("%d " % list2[i][j], end = "")
#    print("")
#----------------------------------------------------------
n = int(input("입력 >>> "))

table = [[0]*n for i in range(n)]