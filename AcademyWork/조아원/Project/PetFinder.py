import json
from tkinter import Button, Entry, Label, Tk

class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

class AnimalShelter:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, name, species, age):
        for animal in self.animals:
            if animal.name == name and animal.species == species and animal.age == age:
                self.animals.remove(animal)
                return True
        return False

    def search_animal(self, name):
        for animal in self.animals:
            if animal.name == name:
                return animal
        return None

class AnimalShelterGUI:
    def __init__(self, root):
        self.root = root
        self.shelter = AnimalShelter()

        # 동물 검색
        self.search_label = Label(root, text="동물 이름:")
        self.search_label.pack()

        self.search_entry = Entry(root)
        self.search_entry.pack()

        search_button = Button(root, text="동물 검색", command=self.search_animal)
        search_button.pack()

        self.result_label = Label(root, text="검색 결과가 여기에 표시됩니다.")
        self.result_label.pack()

        list_button = Button(root, text="동물 목록 조회", command=self.list_animals)
        list_button.pack()

        cancel_button = Button(root, text="조회 취소", command=self.cancel_list)
        cancel_button.pack()

        # 동물 추가
        self.add_name_label = Label(root, text="이름:")
        self.add_name_label.pack()

        self.add_name_entry = Entry(root)
        self.add_name_entry.pack()

        self.add_species_label = Label(root, text="종:")
        self.add_species_label.pack()

        self.add_species_entry = Entry(root)
        self.add_species_entry.pack()

        self.add_age_label = Label(root, text="나이:")
        self.add_age_label.pack()

        self.add_age_entry = Entry(root)
        self.add_age_entry.pack()

        add_button = Button(root, text="동물 추가", command=self.add_animal)
        add_button.pack()

        # 동물 삭제
        self.delete_name_label = Label(root, text="이름:")
        self.delete_name_label.pack()

        self.delete_name_entry = Entry(root)
        self.delete_name_entry.pack()

        self.delete_species_label = Label(root, text="종:")
        self.delete_species_label.pack()

        self.delete_species_entry = Entry(root)
        self.delete_species_entry.pack()

        self.delete_age_label = Label(root, text="나이:")
        self.delete_age_label.pack()

        self.delete_age_entry = Entry(root)
        self.delete_age_entry.pack()

        delete_button = Button(root, text="동물 삭제", command=self.delete_animal)
        delete_button.pack()

        # 데이터 저장 및 불러오기
        save_button = Button(root, text="데이터 저장", command=self.save_data)
        save_button.pack()

        load_button = Button(root, text="데이터 불러오기", command=self.load_data)
        load_button.pack()

        # 윈도우 크기 조정
        root.geometry("200x800")

    def search_animal(self):
        name = self.search_entry.get()
        animal = self.shelter.search_animal(name)
        if animal:
            result_text = f"이름: {animal.name}, 종: {animal.species}, 나이: {animal.age}"
        else:
            result_text = "검색 결과가 없습니다."
        self.result_label.configure(text=result_text)

    def add_animal(self):
        name = self.add_name_entry.get()
        species = self.add_species_entry.get()
        age = self.add_age_entry.get()

        animal = Animal(name, species, age)
        self.shelter.add_animal(animal)

        self.add_name_entry.delete(0, 'end')
        self.add_species_entry.delete(0, 'end')
        self.add_age_entry.delete(0, 'end')

    def delete_animal(self):
        name = self.delete_name_entry.get()
        species = self.delete_species_entry.get()
        age = self.delete_age_entry.get()

        success = self.shelter.remove_animal(name, species, age)
        if success:
            result_text = f"{name}이(가) 삭제되었습니다."
        else:
            result_text = "삭제할 동물이 없거나 입력한 정보가 일치하지 않습니다."
        self.result_label.configure(text=result_text)

    def save_data(self):
        animals = []
        for animal in self.shelter.animals:
            animal_dict = {
                'name': animal.name,
                'species': animal.species,
                'age': animal.age
            }
            animals.append(animal_dict)

        with open('data.json', 'w') as file:
            json.dump(animals, file)

        self.clear_entries()

        # 데이터 저장
        with open('data.json', 'w') as file:
            json.dump(animals, file)

        self.clear_entries()

    def load_data(self):
        try:
            with open('data.json', 'r') as file:
                animals = json.load(file)

            self.shelter.animals = []
            for animal in animals:
                name = animal['name']
                species = animal['species']
                age = animal['age']
                animal_obj = Animal(name, species, age)
                self.shelter.add_animal(animal_obj)

            result_text = "데이터를 불러왔습니다."
        except FileNotFoundError:
            result_text = "데이터 파일이 존재하지 않습니다."

        self.result_label.configure(text=result_text)

    def clear_entries(self):
        self.add_name_entry.delete(0, 'end')
        self.add_species_entry.delete(0, 'end')
        self.add_age_entry.delete(0, 'end')
        self.delete_name_entry.delete(0, 'end')
        self.delete_species_entry.delete(0, 'end')
        self.delete_age_entry.delete(0, 'end')

    def list_animals(self):
        animal_list = []
        for animal in self.shelter.animals:
            animal_info = f"이름: {animal.name}, 종: {animal.species}, 나이: {animal.age}"
            animal_list.append(animal_info)

        if animal_list:
            result_text = "\n".join(animal_list)
        else:
            result_text = "동물 목록이 비어있습니다."
        self.result_label.configure(text=result_text)

    def cancel_list(self):
        self.result_label.configure(text="검색 결과가 여기에 표시됩니다.")

# 메인 코드
root = Tk()
gui = AnimalShelterGUI(root)
root.mainloop()
