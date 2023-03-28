import random
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
m = int(input('몇으로 나누는 놀이를 할까요?'))
print('Stgart : %d로 나누어지는 가장 가까운 수로 답하기\n' % m)
for k in range(5) :
    cn = int(input('Call number = '))
    r = cn % m
    if(m - r) < r :
        ans = cn + (m - r)
    else :
        ans = cn - r
    print('The answer is %d\n' % ans)

