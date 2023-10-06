# 사용자로부터 문장 입력 받기
sentence = input("문장을 입력하세요 : ")

# 문장을 공백을 기준으로 단어로 분리
words = sentence.split()

# 단어 등장 횟수를 저장할 딕셔너리 생성
word_count = {}

# 단어 등장 횟수 계산
for word in words:
    # 단어가 이미 딕셔너리에 있는지 확인하고, 없으면 1로 초기화
    if word not in word_count:
        word_count[word] = 1
    else:
        # 이미 있는 단어라면 등장 횟수를 1 증가
        word_count[word] += 1

# 결과 출력
print("각 단어의 등장 횟수:")
for word, count in word_count.items():
    print(f"{word}: {count}번")