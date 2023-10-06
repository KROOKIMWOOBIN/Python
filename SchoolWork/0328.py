import random as r
import time as t
#--------------------------------------------
#m = random.randrange(1, 20)
#while(True) :
#    u = int(input("사용자 정답 입력 : "))
#    if(m == u) :
#        print('Correct!!!')
#        break
#    elif(u < m) :
#        print("더 큰 수 입니다.")
#    else :
#        print('더 작은 수 입니다.')
#--------------------------------------------
#score = 0
#for k in range(5) :
#    correct = False
#    tnum = 0
#    num1 = random.randint(10,99)
#    num2 = random.randint(10,99)
#    while tnum < 3 and not correct :
#        print("%d + %d = " % (num1, num2), end = '')
#        ans = int(input())
#        if ans == num1 + num2 :
#            print("Correct!!!")
#            correct = True
#            score += (20 - tnum*3)
#        else :
#            print("Try Again ---")
#        tnum += 1
#print("Score = %d" % score)
#---------------------------------------------
#m = int(input('몇으로 나누는 놀이를 할까요?'))
#print('Stgart : %d로 나누어지는 가장 가까운 수로 답하기\n' % m)
#for k in range(5) :
#    cn = int(input('Call number = '))
#    r = cn % m
#    if(m - r) < r :
#        ans = cn + (m - r)
#    else :
#        ans = cn - r
#    print('The answer is %d\n' % ans)
#---------------------------------------------
#acount = [127890, 5780, 1200170]
#sum = 0
#for i in range(3) :
#    sum += acount[i]
#print('잔고 : %d' % sum)
#----------------------------------------------
#taro= ['자유', '시작', '갈등', '풍요', '성공', '자립', '연예', '전진',
#        '극복', '회피', '선택', '안정', '희생', '불행', '인내', '유혹',
#        '파괴', '균형', '불안', '행복', '결단', '성취']
#print('전체 타로카드')
#print(taro)
#
#for i in range(5) :
#    print('%d번째 타로는 = %s' % (i + 1,taro[r.randrange(22)]))
#------------------------------------------------
#oddlist = list(range(1, 101, 2))
#print(oddlist)
#sum = 0
#for i in oddlist :
#    sum += i
#print('1 - 100까지 홀수의 합 : %d' % sum)
#-------------------------------------------------
#n = int(input('몇개의 데이터 처리 : '))
#listex = []
#sum = 0
#print('%d개의 데이터 입력 : ' % n)
#for i in range(n) :
#    listex.append(int(input()))
#    sum += listex[i]
#print('리스트 데이터의 합 : %d 평균 : %.2f\n' % (sum, sum/n))
#max = listex[0]
#min = listex[0]
#
#for i in range(0, n) :
#    if(max < listex[i]) :
#        max = listex[i]
#    if(min > listex[i]) :
#        min = listex[i]
#print('최대 값 : %d 최소 값 : %d' % (max, min))
#----------------------
#slot = [0] * 3
#user = int(input('몇번 반복하겠습니까? >>> '))
#for i in range(user) :
#    for j in range(3) :
#        slot[j] = r.randrange(7, 10)
#        print('%d ' % slot[j], end = '')
#        t.sleep(1)     
#    if(slot[0] + slot[1] + slot[2] == 21) :
#        print('\n잭팟')
#    else :
#        print('\n꽝')
#----------------------
arr = list(range(10))

print(arr[2:5])
print(arr[2:])
print(arr[:5])
print(arr[:])
print(arr[-1])
print(arr[-5:-1])
#-----------------------------------------------
arr = [20, 30, 10, 5, 20, 9]
arr.append(50)
print('.append(50) >', arr)
b = arr.pop()
print('.pop >', arr, b)
arr.insert(1, 60)
print('.insert(1, 60) > ', arr)
arr.remove(20)
print('arr.remove(20) > ', arr)
arr.clear()
print('.clear() >', arr)
#-----------------------------------------------
arr = [20, 30, 10, 5, 20, 9]
x = arr.index(30)
print('.index(30) >', x)
x = arr.count(20)
print('.count(20) >', x)
arr.sort()
print('.sort() >', arr)
arr.reverse()
print('.reverse() >', arr)

if 20 in arr :
    print('있음')
else :
    print('없음')
#----------------------------------------------------
#numbers = list(map(int, input('숫자 입력 : ').split()))
#print('numbers : ', numbers)
#-----------------------------------------------------
arr1, arr2 = map(int, ['10','20'])
print(arr1, arr2)
arr1 = list(map(int, ['10','20','30']))
print(arr1)
#-----------------------------------------------------
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
pSum = [0]
temp = 0
for i in numbers : 
    temp = temp + 1
    pSum.append(temp)
print(pSum)

for i in range(quizNo) :
    s, e = map(int, input().split())
    print(pSum[e]-pSum[s-1])

        
