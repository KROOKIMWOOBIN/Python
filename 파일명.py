
import os
import tkinter as tk
import json

def show_pet_info(event):
    item = canvas.find_withtag("current")[0]
    pet_info_list = pet_info_dict[item]
    pet_info = '\n'.join(pet_info_list)
    info_label.config(text=pet_info)

def delete_pet_info():
    selected_items = canvas.find_withtag("selected")
    
    if selected_items:
        for item in selected_items:
            canvas.delete(item)
            pet_info_dict.pop(item)
        info_label.config(text="여기에 표시됩니다.")
    else:
        info_label.config(text="삭제할 항목을 선택해주세요.")

    # 입력 내용 초기화
    pet_species_entry.delete(0, 'end')
    pet_description_entry.delete(0, 'end')
    location_entry.delete(0, 'end')

def show_map():
    pet_species = pet_species_entry.get()
    pet_description = pet_description_entry.get()
    location = location_entry.get()
    x, y = map(int, location.split(','))
    oval_id = canvas.create_oval(x, y, x + 10, y + 10, fill="red", tags="selected")
    
    if oval_id in pet_info_dict:
        pet_info_dict[oval_id].append({"애완동물 종": pet_species, "애완동물 특징": pet_description})
    else:
        pet_info_dict[oval_id] = [{"애완동물 종": pet_species, "애완동물 특징": pet_description}]
    
    canvas.tag_bind(oval_id, '<Enter>', show_pet_info)

    # 입력 내용 초기화
    pet_species_entry.delete(0, 'end')
    pet_description_entry.delete(0, 'end')
    location_entry.delete(0, 'end')

def save_data():
    filename = "data.json"
    with open(filename, "w") as file:
        json.dump(pet_info_dict, file, indent=4, ensure_ascii=False)

def load_data():
    filename = "data.json"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            loaded_data = json.load(file)
            pet_info_dict.clear()  # 기존 데이터 삭제
            pet_info_dict.update(loaded_data)

root = tk.Tk()
root.title("PetFinder")
root.geometry("1000x800")

frame = tk.Frame(root)
frame.pack()

canvas = tk.Canvas(frame, width=600, height=500)
canvas.pack()

map_image = tk.PhotoImage(file="C:/Users/CS/Desktop/Python/AcademyWork/조아원/Project/img.GIF")
resized_image = map_image.subsample(1, 1)  # 이미지 크기 조정
canvas.create_image(0, 0, anchor="nw", image=resized_image)

pet_species_label = tk.Label(frame, text="애완동물 종")
pet_species_label.pack(side="left", padx=10, pady=10)
pet_species_entry = tk.Entry(frame)
pet_species_entry.pack(side="left", padx=10, pady=10)

pet_description_label = tk.Label(frame, text="애완동물 특징")
pet_description_label.pack(side="left", padx=10, pady=10)
pet_description_entry = tk.Entry(frame)
pet_description_entry.pack(side="left", padx=10, pady=10)

location_label = tk.Label(frame, text="잃어버린 위치(예시 100,100)")
location_label.pack(side="left", padx=10, pady=10)
location_entry = tk.Entry(frame)
location_entry.pack(side="left", padx=10, pady=10)

show_map_button = tk.Button(root, text="위치 표시하기", command=show_map)
show_map_button.pack(pady=10)

delete_button = tk.Button(root, text="정보 삭제", command=delete_pet_info)
delete_button.pack(pady=10)

info_label = tk.Label(root, text="정보가 여기에 표시됩니다.")
info_label.pack(pady=10)

save_button = tk.Button(root, text="데이터 저장하기", command=save_data)
save_button.pack(pady=10)

load_button = tk.Button(root, text="데이터 불러오기", command=load_data)
load_button.pack(pady=10)

pet_info_dict = {}
load_data()

root.mainloop()
