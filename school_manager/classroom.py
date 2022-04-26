# %%

import json
from typing import List
from student import Student
from utils import clear_screen,display_message, RECORD_PATH


class ClassRoom():
    message = ''

    def __init__(self, name):
        self.__students: List[Student] = []
        self.name = name

    def get_new_roll(self):
        return self.__students.__len__()+1

    def add_student(self):
        self.message = ''
        clear_screen()
        print('4. Add Student')
        first_name = input('First Name:')
        last_name = input('Last Name:')
        roll = self.get_new_roll()
        age = int(input('Age:'))
        gender = input('Gender:')
        major = input('Major:')
        info = Student(first_name, last_name, roll, age, gender, major)
        self.__students.append(info)
        self.message = f'Student {first_name} {last_name} is added successfully.'

    def remove_student(self):
        self.list_student()
        roll = int(input('Enter Roll of a student you wanna remove:'))
        found = False
        for student in self.__students:
            if student.roll == roll:
                found = True
                self.__students.remove(student)
                self.list_student()
                self.message = f'Student {student.first_name} {student.last_name} with roll number {student.roll} is removed successfully.'
        if not found:
            print(f"Does not exist")

    def rename_class(self):
        print('-'*20)
        print('2. Rename a class')
        print('-'*20)
        self.name = input('Enter new class name:')
    
    def load_record(self, students: list):
        for std in students:
            self.__students.append(Student(**std))

    def save_record(self):
        with open(f"{RECORD_PATH}/{self.name}.json", 'w') as file:
            json.dump({
                'name': self.name,
                'students': [s.__dict__ for s in self.__students]
            }, file)

    def list_student(self):
        self.message = ''
        clear_screen()
        print('-'*80)
        print(f"{self.name} Students")
        print('-'*80)
        print(f"{'Roll':<5}{'Name':<30}{'Age':<5}{'Gender':<10}{'Major':<15}")
        print('-'*80)
        for student in self.__students:
            full_name = student.first_name + ' ' + student.last_name
            print(f"{student.roll:<5}{full_name:<30}{student.age:<5}{student.gender:<10}{student.major:<15}")
        print('-'*80)
        input('Press Enter to Continue...')

    def modify_student(self):
        self.message = ''
        clear_screen()
        self.list_student()
        roll = int(input('Enter Roll of a student you wanna modify:'))
        first_name = input('First Name:')
        last_name = input('Last Name:')
        age = input('Age:')
        gender = input('Gender:')
        major = input('Major:')
        for i in self.__students:
            if i.roll == roll:
                self.__students.remove(i)
        self.message = f'{first_name} {last_name} is modified successfully'
        return self.__students.insert(roll, Student(first_name, last_name, roll, age, gender, major))

    def __str__(self) -> str:
        return self.name

    def get_value(self):
        return '\n'.join([student.__str__() for student in self.__students])

    def show_menu(self):
        menu_items = {
            '0':{
                'title': 'Go To Menu'
            },
            '1': {
                'title': 'Rename a class',
                'action': self.rename_class
            },
            '2': {
                'title': 'Add Student',
                'action': self.add_student
            },
            '3': {
                'title': 'List Students',
                'action': self.list_student
            },
            '4': {
                'title': 'Remove Student',
                'action': self.remove_student
            },
            '5': {
                'title': 'Modify Student',
                'action': self.modify_student
            },
        }
        clear_screen()
        while True:
            clear_screen()
            print(f'2. Manage {self.name}')
            for k, v in menu_items.items():
                print(f'{k}: {v["title"]}')
            if self.message.__len__() > 0:
                display_message(self.message)
            try:
                option = input("Please select an option: ")
                if option=='0':
                    return
                menu_items[option]['action']()

            except KeyError:
                self.message = "Option not available"

