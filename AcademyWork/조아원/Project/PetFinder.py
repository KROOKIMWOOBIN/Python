# 프로젝트
# 프로젝트 명 : 펫파인더
# 사용할 언어 : Python
# 사용할 라이브러리 : 미정
# <<< 프로젝트 설명 >>>
# 사용자가 애완동물의 특징을 입력 해서 지도에 표시

# 1. 라이브러리 사용 여부
# 2. 구글 지도
# 3. GUI O

# 알고리즘(단계별로 문제를 해결할 수 있는 걸) 
# - GUI로 구성
# 1. 사용자가 애완동물의 특징을 입력
# 2. 지도에 특징과 같이 표시

# 종류 및 생김새, 성별, 나이, 이미지 <<< 사용자가 입력
# 지도에 정보와 같이 표시
# ----------------------------------------------------

# 첫 제출 11월 29일 <- 11월 24일까지 제작

import tkinter as tk

def show_map():
    # 입력된 애완동물 종 및 특징, 위치 정보 가져오기
    pet_species = pet_species_entry.get()
    pet_description = pet_description_entry.get()
    location = location_entry.get()
    
    # 여기에서 Google 지도 API를 사용하여 위치를 표시하면 됩니다.
    # 예: print(f"애완동물 종: {pet_species}, 특징: {pet_description}, 위치: {location}")

# 메인 윈도우 생성
root = tk.Tk() # 새로운 창을 나는 만들겠다.
root.title("PetFinder") # 제목
root.geometry("400x300") # 화면 크기

# 애완동물 종 라벨과 입력 필드 배치
pet_species_label = tk.Label(root, text="애완동물 종")
pet_species_label.grid(row=0, column=0, padx=10, pady=10)
pet_species_entry = tk.Entry(root)
pet_species_entry.grid(row=0, column=1, padx=10, pady=10)

# 애완동물 특징 라벨과 입력 필드 배치
pet_description_label = tk.Label(root, text="애완동물 특징")
pet_description_label.grid(row=1, column=0, padx=10, pady=10)
pet_description_entry = tk.Entry(root)
pet_description_entry.grid(row=1, column=1, padx=10, pady=10)

# 위치 라벨과 입력 필드 배치
location_label = tk.Label(root, text="잃어버린 위치")
location_label.grid(row=2, column=0, padx=10, pady=10)
location_entry = tk.Entry(root)
location_entry.grid(row=2, column=1, padx=10, pady=10)

# 위치 표시 버튼 추가
show_map_button = tk.Button(root, text="위치 표시하기", command=show_map)
show_map_button.grid(row=3, columnspan=2, padx=10, pady=10)

root.mainloop()


