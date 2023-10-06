from random import randrange
from random import sample
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
# 마방진
#n = int(input("입력 >>> "))

#table = [[0]*n for k in range(n)]

#i = 0
#j = n//2
#table[i][j] = 1
#count = 2
#while count <= n * n :
#    row = i - 1
#    col = j - 1
#    if row < 0 :
#        row = n - 1
#    if col < 0 :
#        col = n - 1
#    if table[row][col] != 0 : 
#         i += 1
#    else :
#        i = row
#        j = col
#    table[i][j] = count
#    count += 1
#print("magic number = ", sum(table[0]))
#print("----------------------------------------------")
#for row in table :
#    print(row)
#print("----------------------------------------------")
#print("magic number = ", sum(table[0]))
#for row in range(n) :
#    for col in range(n) :
#        print('%3d' % table[row][col], end='')
#    print()
#----------------------------------------------------------
# 튜플은 읽기만 가능하고 삭제는 전체삭제만 가능
# 튜플과 리스트는 변환이 가능하다. 예) list tupple
#menu = ('기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거')
#price = (4000, 4500, 5000, 7000)
#print("------------------------------------")
#for i in range(len(menu)) :
#    print(i+1,':',menu[i],':',price[i])
#print("------------------------------------")
#imenu = list(menu)
#iprice = list(price)
#imenu.append('새우버거')
#iprice.append(5500)
#menu = tuple(imenu)
#price = tuple(iprice)
#for i in range(len(menu)) :
#    print(i+1,':',menu[i],':',price[i])
#print("------------------------------------")
#----------------------------------------------------------
#mdict_list = {'기본햄버거':4000,'치즈햄버거':4500,'불고기버거':5500,'와퍼킹버거':7000}
#print(mdict_list.items()) # 추가
#mdict_list['새우버거'] = 5500 
#print(mdict_list.items()) # 삭제
#del mdict_list['기본햄버거']
#print(mdict_list.items()) 
#mdict_list['나이키버거'] = 2000 # 추가
#print(mdict_list.items()) 
#for i, j in mdict_list.items() : # 키와 값 출력 key:value
#    print(i,':',j)
#----------------------------------------------------------
#s1 = {0, 1, 3, 5, 7}
#s2 = set()
#s2.add(2), s2.add(4), s2.add(6), s2.add(8), s2.add(0)

#print('{0}과 {1}의 합집합 = {2}'.format(s1, s2, (s1|s2)))
#print('{0}과 {1}의 교집합 = {2}'.format(s1, s2, (s1&s2)))
#print('{0}과 {1}의 차집합 = {2}'.format(s1, s2, (s1-s2)))
#----------------------------------------------------------

mylotto = set()
while True :
    num = randrange(1, 46)
    print(num," ", end ='')
    mylotto.add(num)
    if len(mylotto) == 6 :
        break
print("\n집합 : {}".format(mylotto))
print("정렬리스트 : {}".format(sorted(mylotto)))

print("\nsample로 번호리스트 만들기")
lotto = sample(range(1, 46), 6)
print("sample 함수 리스트 : {}".format(lotto))
print("sample 함수 정렬리스트 : {}".format(sorted(lotto)))

# listex.sort() 정렬 바뀌고 저장됨
# sorted(listex) 정렬 되지만 저장은 안됨 따로 넣어줘야지 저장됨