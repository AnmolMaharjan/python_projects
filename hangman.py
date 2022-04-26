# %% Hangman M

import random
from typing import List
import os
import time

class Hangman:

    def __init__(self):
        word_word = ['AnmolMaharjan', 'MonkeyDLuffy', 'TrafalgarDWaterLaw', 'RedHairShanks', 'GolDRoger', 'ConnectingDots', 'SusanMaharjan', 'RoronoaZoro','NepalFlag', 'VinsmokeSanji', 'NicoRobin', 'BoaHancock', 'TonyTonyChopper', 'GodUsopp', 'EdwardNewgateWhitebeard', 'DonquixoteDoflamingo', 'PortgasDAce', 'DraculeMihawk', 'MonkeyDDragon']
        fill_n = [1, 1, 2, 1, 2, 3]
        self.filler = random.choice(fill_n)
        self.choice = random.choice(word_word)
        self.choice_len = len(self.choice)
        self.choice_letter_list = []
        
        self.correct_chosed_list = []
        
        self.wrong_chosed_list = []
        self.attempts_list = []
        self.chances = 5

        for char in self.choice:
            self.choice_letter_list.append(char.upper())

        self.fill = random.sample(self.choice_letter_list, self.filler)
        self.correct_chosed_list.extend(self.fill)
        self.attempts_list.extend(self.fill)

    def intro(self):
        HANGMAN_GRAPHICS = (
            ((0, 4), (4, 4), (4, 8), (4, 4), (4, 4), (4, 9)),
            ((0, 4), (4, 4), (3, 4), (2, 4), (3, 6), (2, 4), (3, 4), (4, 4)),
            ((0, 12), (2, 12), (2, 7), (1, 4), (2, 4)),
            ((0, 12), (2, 12), (2, 4), (1, 7), (2, 4), (3, 7)),
            ((0, 4), (4, 4), (2, 4), (4, 4), (2, 4), (2, 6), (3, 4), (4, 4)),
            ((0, 4), (4, 4), (2, 4), (4, 4), (2, 4), (3, 5), (4, 10)),
            ((0, 0), ),
            ((0, 0), ),
            ((0, 4), (8, 4), (4, 8), (4, 4), (4, 4)),
            ((0, 6), (4, 6), (3, 4), (2, 4), (3, 6), (2, 4)),
            ((0, 16), (2, 12), (2, 7), (1, 4)),
            ((0, 4), (2, 4), (2, 4), (2, 12), (2, 4), (1, 7)),
            ((0, 4), (8, 4), (2, 4), (4, 4), (2, 4), (2, 6)),
            ((0, 4), (8, 4), (2, 4), (4, 4), (2, 4), (3, 5)),
        )

        for line in HANGMAN_GRAPHICS:
            for blank, fill in line:
                print(' ' * blank, '|' * fill, end='', sep='')
            print()

    def hangman(self):
        print(f'Total Attempts: {self.attempts_list.__len__()-self.filler}')
        print(f'Total Correct Guesses: {len(self.correct_chosed_list)-self.filler}')
        print(f'Total Wrong Guesses: {len(self.wrong_chosed_list)}')
        print(f'Remaining Lives: {self.chances}')
        print('+'+'-'*self.choice_len*4+'+')
        print('|'+' '*self.choice_len, end='')
        for i in self.choice_letter_list:
            if i in self.correct_chosed_list:
                print(i, end=' ')
            else:
                print('_', end=' ')
        print(' '*self.choice_len, end='')
        print('|')
        print('+'+'-'*self.choice_len*4+'+')
        print('Letters You\'ve Entered:')
        for i in sorted(self.attempts_list):
            print(i, end=' ')
        print('')

    def input(self):
        self.user_input = (input('Enter a letter:')).upper()

    def correct_input(self):
        self.correct_chosed_list.append(self.user_input)
        self.attempts_list.append(self.user_input)
        print('\nCorrect!\n')

    def wrong_input(self):
        self.wrong_chosed_list.append(self.user_input)
        self.attempts_list.append(self.user_input)
        print('\nWrong!\n')
        self.chances -= 1

    def play(self):
        self.intro()
        input('\nPress Enter to Continue...')
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            self.hangman()
            if len(self.correct_chosed_list) == len(sorted(set(self.choice_letter_list))):
                print('You win!')
                break
            if self.chances == 0:
                print('Game Over!')
                print('You Lose!')
                print(f'Correct Word = {self.choice}')
                break
            self.input()
            if self.user_input in self.attempts_list:
                print('\nAlready Entered\n')
                time.sleep(3)
            elif self.user_input in self.choice_letter_list:
                self.correct_input()
            else:
                self.wrong_input()


if __name__ == '__main__':
    game = Hangman()
    game.play()
