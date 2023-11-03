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

def show_pet_info(event):
    item = canvas.find_withtag("current")[0]
    pet_info = pet_info_dict[item]
    info_label.config(text=pet_info)

def show_map():
    pet_species = pet_species_entry.get()
    pet_description = pet_description_entry.get()
    location = location_entry.get()
    x, y = map(int, location.split(','))
    oval_id = canvas.create_oval(x, y, x + 10, y + 10, fill="red")
    pet_info = f"애완동물 종: {pet_species}\n애완동물 특징: {pet_description}"
    pet_info_dict[oval_id] = pet_info
    canvas.tag_bind(oval_id, '<Enter>', show_pet_info)

root = tk.Tk()
root.title("PetFinder")
root.geometry("1000x700")

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=600, height=500)
canvas.pack()

map_image = tk.PhotoImage(file="C:/Users/CS/Desktop/Python/AcademyWork/조아원/Project/img.GIF")
canvas.create_image(0, 0, anchor="nw", image=map_image)

pet_species_label = tk.Label(frame, text="애완동물 종")
pet_species_label.pack(side="left", padx=10, pady=10)
pet_species_entry = tk.Entry(frame)
pet_species_entry.pack(side="left", padx=10, pady=10)

pet_description_label = tk.Label(frame, text="애완동물 특징")
pet_description_label.pack(side="left", padx=10, pady=10)
pet_description_entry = tk.Entry(frame)
pet_description_entry.pack(side="left", padx=10, pady=10)

location_label = tk.Label(frame, text="잃어버린 위치")
location_label.pack(side="left", padx=10, pady=10)
location_entry = tk.Entry(frame)
location_entry.pack(side="left", padx=10, pady=10)

show_map_button = tk.Button(root, text="위치 표시하기", command=show_map)
show_map_button.pack(pady=10)

info_label = tk.Label(root, text="애완동물 정보가 여기에 표시됩니다.")
info_label.pack(pady=10)

pet_info_dict = {}

root.mainloop()


