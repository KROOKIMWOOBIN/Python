#import

#------------------------------------------------------------------------------------------------------
#code
#파일 불러와서 읽기
file_path = "text/1.txt"

data_dict = {}

with open(file_path, "r") as f:
    for line in f:
        id, *data = line.strip().split(":")
        data_dict[id] = tuple(data)

smax = 0
midx = 0

for i in data_dict:
    print(i, ':', data_dict[i])

for i in data_dict :
    if int(data_dict[i][1]) > smax :
        smax = int(data_dict[i][1])
        midx = i
print('최대 수강하는 강좌의 정보 = ', midx, ':', data_dict[midx])

snumList = []

for i in data_dict :
    idata = int(data_dict[i][1])
    snumList.append(idata)
print('리스트 함수이용 : 최대 수강인원은 = ', max(snumList))
#------------------------------------------------------------------------------------------------------
# 컴프리헨션 구문
numbers = [n for n in range(5, 99, 5)]
for i in range(len(numbers)) :
    print(numbers[i], end=' ')
#------------------------------------------------------------------------------------------------------
# zip() 함수
menulist = ['기본햄버거', '치즈햄버거', '불고기버거', '와퍼킹버거']
pricelist = [4000, 4500, 5000, 7000]
tlist = list(zip(menulist, pricelist)) # 튜플 리스트
dlist = dict(zip(menulist, pricelist)) # 딕셔너리 리스트
print("\n튜플 리스트 ->",tlist)
print("\n딕셔너리 리스트 ->",dlist)
#------------------------------------------------------------------------------------------------------
# 얅은 복사 -> 동일한 메모리 공간 보유
oldList = [1, 2, 3]
newList = oldList
oldList[0] = 4
oldList.append(5)
print(oldList)
# 깊은 복사 -> 메모리 공간을 복사하여  새로 만듬
oldList = [1,2,3]
newList = oldList[:]
print(newList)
oldList[0] = 4
oldList.append(5)
print(newList)

st1 = '문자열'
st2 = '리스트'

print(st1)
print(st1[0],st1[1],st1[2])
print(st1 + st2)
print(st2 * 3)