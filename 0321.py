#choice = int(input('만날까? 말까? (1/0) 입력 : '))
#print('오늘부터 1일\n') if choice == 1 else print('다음 기회에~~\n')
#-----------------------------------------------------------------
#choice = bool(int(input('만날까? 말까? (1/0) 입력 : ')))
#print('오늘부터 1일\n') if choice else print('다음 기회에~~\n')
#-----------------------------------------------------------------
#import random
#trip = random.randrange(0, 4)
#if trip == 0 :
#    print('제주도')
#elif trip == 1 :
#    print('사이판')
#else :
#    print('하와이')
#------------------------------------------------------------------
#import random
#com = random.randrange(3)
#user = int(input('가위0 바위1 보2 선택 : '))
#print('user %d, com %d' % (user,com))
#------------------------------------------------------------------
#import random
#com = random.randrange(3)
#count = 1
#while(1) :
#    user = int(input('가위0 바위1 보2 선택 : '))
#    if user <= 2 :
#        break
#    count += 1
#print('user %d, com %d, count %d' % (user,com,count))
#------------------------------------------------------------------
#import random
#com = random.randrange(3)
#count = 1
#while(1) :
#    user = int(input('가위0 바위1 보2 선택 : '))
#    if user <= 2 :
#        break
#    count += 1
#if user == com :
#    print('\n비겼습니다.\n')
#elif(user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
#    print('\n이겼습니다.\n')
#print('user %d, com %d, count %d' % (user,com,count))
#------------------------------------------------------------------
#import random
#com = random.randrange(3)
#count = 1
#while(1) :
#    user = int(input('가위0 바위1 보2 >>> '))
#    if (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1) :
#        print('사용자가 이겼습니다')
#        break
#    elif user == com :
#        print('비겼습니다')
#        count += 1
#    elif (user == 2 and com == 0) or (user == 0 and com == 1) or (user == 1 and com == 2) :
#        print('컴퓨터가 이겼습니다')
#        break
#    else :
#        print('잘못 입력되었습니다.')
#print('%d회 가위바위보 종료' % count)
#---------------------------------------------------------------------------------------
#n = int(input('양의 정수 입력 : '))
#i = 1
#sum = 0
#while i <= n :
#    if i%2 == 0 :
#        sum += i
#    i = i + 1
#print('짝수의 합 : %d' % sum)
#----------------------------------
#n = int(input('양의 정수 입력 : '))
#i = 0
#sum = 0
#for i in range(n) :
#    i += 1
#    if i%2 == 0 :
#        sum += i
#print('짝수의 합 : %d' % sum)
#-------------------------------------------------------------------
#select = input('1. 입력한 수식 계산 2. 두 수 사이의 합계 : ')
#print(eval(select))
#sum = 0
#i = eval(select[0])
#for i in range(eval(select[2])) :
#    sum += i
#    i+=1
#print(sum)
#-----------------
import os
print('내가 사용하고 있는 경로 보여줘')
print(os.getcwd())

from time import time, sleep

start = time()
sleep(1.5)
end = time()
print('실행 시간', end - start)


    