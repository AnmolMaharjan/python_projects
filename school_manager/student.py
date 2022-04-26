# %%

class Student:
    def __init__(self, first_name, last_name, roll, age, gender, major):
        self.first_name = first_name
        self.last_name = last_name
        self.roll = roll
        self.age = age
        self.gender = gender
        self.major = major

    def show_menu(self):
        print('Student Management Screen')

    def __lt__(self, other):
        return self.roll < other.roll

    def __str__(self) -> str:
        # print(f"{self.roll:<5}{self.full_name:<30}{self.age:<5}{self.gender:<10}{self.major:<15}")
        print('xu xu kaa')
        return ('-'*80)
