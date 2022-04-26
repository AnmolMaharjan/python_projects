
# %% Tic Tac Toe

import os
import random
import time

class TicTacToe():

    def __init__(self):
        self.mylist = [['  ','  ','  '],['  ','  ','  '],['  ','  ','  ']]
        
    def user(self, str):
        user_in = int(input(f'Player {self.turn} (Enter a position):'))
        for i, k in enumerate(self.mylist):
            if 0 == i:
                for j, v in enumerate(k):
                    if user_in-1 == j:
                        if self.mylist[i][j] != '  ':
                            print('Already Entered')
                            time.sleep(1)
                            self.user(str)
                        else:
                            self.mylist[i].pop(j)
                            self.mylist[i].insert(j, str)
            elif 1 == i:
                for j, v in enumerate(k):
                    if user_in-4 == j:
                        if self.mylist[i][j] != '  ':
                            print('Already Entered')
                            time.sleep(1)
                            self.user(str)
                        else:
                            self.mylist[i].pop(j)
                            self.mylist[i].insert(j, str)
            # elif 2 == i:
            else:
                for j, v in enumerate(k):
                    if user_in-7 == j:
                        if self.mylist[i][j] != '  ':
                            print('Already Entered')
                            time.sleep(1)
                            self.user(str)
                        else:
                            self.mylist[i].pop(j)
                            self.mylist[i].insert(j, str)

    def format(self):
        print('\nPositions:')
        format_list = [[1,2,3],[4,5,6],[7,8,9]]
        print('')
        print(('\n'+'-'*11+'\n').join([' | '.join([str(v) for v in x]) for x in format_list]))
        print('')
        

    def board(self):
        print('')
        print(('\n'+'-'*11+'\n').join([' |'.join([str(v) for v in x]) for x in self.mylist]))
        print('')

    def first_turn(self):
        while True:
            first =  input("Who goes first? (Player 1/2) :\t")
            if (first == '1') | (first == '2' ):
                self.turn = int(first)
                break
            else:
                print('Invalid Input!')

    def swap_turn(self):
        self.turn = 1 if self.turn == 2 else 2
    
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def win_lose(self):
        win = False
        draw = 9
        for i in range(3):
            if (self.mylist[i][0] == self.mylist[i][1] == self.mylist[i][2] != '  ' or self.mylist[0][i] == self.mylist[1][i] == self.mylist[2][i] != '  '):
                win = True
                break

        if self.mylist[0][0] == self.mylist[1][1] == self.mylist[2][2] != '  ':
            win = True

        if self.mylist[0][2] == self.mylist[1][1] == self.mylist[2][0] != '  ':
            win = True
        
        if win:
            print(f'Player {self.turn} Wins!')
            exit()

        for i in range(3):
            for j in range(3):
                if self.mylist[i][j] != '  ':
                    draw -= 1
                if draw == 0:
                    print('Draw!')
                    self.__init__()
                    self.play()
            

    def play(self):

        print("Player 1 = 'o'")
        print("Player 2 = 'x' ")

        self.first_turn()

        self.format()
        self.board()

        while True:
            while self.turn == 2:
                self.user(' x')
                break
            while self.turn == 1:
                self.user(' o')
                break
            self.clear()
            print("Player 1 = 'o'")
            print("Player 2 = 'x' ")
            self.format()
            self.board()
            self.win_lose()
            self.swap_turn()

if __name__ == '__main__':
    game = TicTacToe()
    game.play()

# %%
