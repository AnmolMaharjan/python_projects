
# %% School Manager

from typing import List
from utils import clear_screen,display_message, RECORD_PATH
from classroom import ClassRoom
import os
import json


class SchoolManager(ClassRoom):
    message = ''
    def __init__(self) -> None:
        self.class_list: List[ClassRoom] = []
        if os.path.exists(RECORD_PATH):
            for file_path in os.listdir(RECORD_PATH):
                if file_path.endswith('.json'):
                    with open(f"{RECORD_PATH}/{file_path}", 'r', encoding='utf-8') as file:
                        class_data = json.load(file)
                    class_room = ClassRoom(class_data['name'])
                    class_room.load_record(class_data['students'])
                    self.class_list.append(class_room)
        else:
            os.mkdir(RECORD_PATH)

    def create_class(self):
        self.message = ''
        print('-'*20)
        print('1. Create a Class')
        print('-'*20)
        class_name = input('Enter Class Name:')
        print('-'*20)
        if class_name in [c.name for c in self.class_list]:
            self.message = f"The class with name {class_name} already exists"
            return
        self.class_list.append(ClassRoom(class_name))
        self.message = f"Class '{class_name}' created Successfully"

    def delete_class(self):
        self.message = ''
        found = False
        print('-'*20)
        print('3. Delete a Class')
        print('-'*20)
        if self.class_list.__len__() == 0:
            print('No Any Classes')
            input('Press Enter to Continue...')
            return
        print('0. Go To Main Menu:')
        for i, cls in enumerate(self.class_list):
            print(f'{i+1}. {cls}')
        delete = int(input('Select a class option you wanna delete.'))
        if delete == 0:
            return
        for i, cls in enumerate(self.class_list):
            if i == delete-1:
                found = True
                os.remove(f'{RECORD_PATH}/{cls.name}.json')
                self.class_list.remove(cls)
                self.message = f'{cls.name} removed successfully'
                break
        if not found:
            self.message = '404 not found!'

    def manage_class(self):
        while True:
            self.message = ''
            print('-'*20)
            print('2. Manage a Class')
            print('-'*20)
            print('0. Go to main menu')
            for i, clsroom in enumerate(self.class_list):
                print(f'''{i+1}.''' + ' ' + f'''{clsroom.name}''')
            try:
                option = int(input('Please select an option:'))
                if option == 0:
                    self.message = ''
                    return
                self.class_list[option-1].show_menu()
            except(ValueError, IndexError):
                self.message = 'Invalid Input!'
        

    def quit(self):
        for cls in self.class_list:
                    print(cls.name + 'saved')
                    cls.save_record()
        print('Exiting...')
        exit()

    

    def show_menu(self):
        menu_items = {
            '0': {
                'title': 'Quit application',
                'action': self.quit
            },
            '1': {
                'title': 'Create a class',
                'action': self.create_class
            },
            '2': {
                'title': 'Manage a class',
                'action': self.manage_class
            },
            '3': {
                'title': 'Delete a class',
                'action': self.delete_class
            }
        }
        while True:
            clear_screen()
            print(f'School Management System')
            for k, v in menu_items.items():
                print(f'{k}: {v["title"]}')
            if self.message.__len__()>0:
                display_message(self.message)
            try:
                option = input("Please select an option: ")
                menu_items[option]['action']()

            except KeyError:
                self.message = "Option not available"
        
if __name__ == '__main__':
    menu = SchoolManager()
    menu.show_menu()

# %%
