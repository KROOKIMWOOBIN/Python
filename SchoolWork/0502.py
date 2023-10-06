'''
정리
1. 딕셔너리 사용법
ex_dict = dict(a = 1, b = 2, c = 3)
'''
import random as r
import time as t
#람다식으로 월 지출 금액 구하기
'''
cpay1 = [23900, 65000, 78000, 20100, 600]
cpay2=[123450, 25610, 658990, 25000, 678500]
cpay3=[25670, 4520, 3300, 29000, 1000]
ctotal = list(map(lambda a, b, c : a + b + c, cpay1, cpay2, cpay3))

print(ctotal)
for k in range(5) : 
    print(k + 1, '월 지출', ctotal[k], '원')
'''
# 사다리 타기 게임
'''
def sadari(st) :
    s = r.randrange(st)
    return s

sdr = [0]
sdr = input('사다리 타기 항목 입력 >>> ').split()

for k in range(len(sdr)) :
    hit = sadari(len(sdr))
    t.sleep(1)
    print(k + 1,'번은', sdr[hit])
    del(sdr[hit])
'''
# 랜덤 로또번호
'''
def buyautolotto() :
    lotto = []
    for i in range(5) :
        num6 = set(r.sample(list( range(1, 46)), 6))
        lotto.append(num6)
    return lotto

def printnums(nums) : 
    for num in sorted(nums) :
        print('%5d' % num, end = ' ')
    print()

def printlotto(lotto) : 
    for i, item in enumerate(lotto) :
        print('%c 자 동 ' % (ord('A') + i), end = "")
        printnums(item)
    print()

def setwinlotto() :
    global winnum
    winnum = set(r.sample(list(range(1, 46)), 6))

def getwinner(lotto) :
    a = True # 반복문 조건
    count = 0
    while a :
        count = count + 1 # 로또 횟수
        lotto = buyautolotto() # 새로 구매
        print('로또 제',count, '회')
        for i, item in enumerate(lotto) : # 리스트 길이만큼 동작하는데 item에 로또 인덱스 값의
                                          # 데이터를 넣음
            print('%c' % (ord('A') + i), end = ' ') # ord 하나의 문자를 유니코드 정수를 변환시킴
            win = winnum.intersection(item) # 교집합하여 당첨 여부 검사
            if win :
                wincnt = len(win) # win의 길이 넣음
                print('당첨 번호 개수 %d,' % wincnt, end = '')
                printnums(win) # 당첨 번호 출력
                if(wincnt >= 2) :
                    a = False
            else :
                print('꽝')


setwinlotto() # 당첨번호
print('당첨 번호 : ', winnum) # winnum은 전역변수
lotto = buyautolotto() # 랜덤 로또 넣어줌
printlotto(lotto)
getwinner(lotto)
'''
# 피보나치수열 1부터 13까지 출력하는 재귀함수
'''
def fibo(n) :
    if n < 2 :
        return 1
    return fibo(n - 1) + fibo(n - 2)

for i in range(13) :
    print('%d개월 후 토끼의 수 = %d' % (i ,fibo(i)))
'''
# 웹브라우저 활용방법
'''
import webbrowser

while True :
    print('0 : 전체')
    print('1 : 이미지')
    print('2 : 뉴스')
    print('3 : 동영상')
    category = int(input('Input category :'))

    if category not in  [0,1,2,3] :
        print('The end of search~~~')
        break
    else :
        sword = input('키워드 입력 : ')
       
        urlex = 'https://www.google.com/search?q='+sword
        if category == 1 :
            urlex += '&source=lnms&tbm=isch&sa=X&ved=2ahUKEwih5tiL96r-AhXJrlYBHTR1DFoQ_AUoAXoECAEQAw&biw=1920&bih=969&dpr=1'
        if category == 2 :
            urlex += '&source=lmns&tbm=nws&bih=969&biw=1920&hl=en&sa=X&ved=2ahUKEwiFtdfA96r-AhX_t1YBHYHdAa4Q_AUoAnoECAEQAg'
        if category == 3:
            urlex += '&hl=en&tbm=vid&source=lnms&sa=X&ved=2ahUKEwj61d3F96r-AhWDmlYBHSBbDYcQ_AUoA3oECAIQBQ&biw=1920&bih=969&dpr=1'
        webbrowser.open_new(urlex)
'''
