# %% Scissor Paper Rock

import random

mylist = {
    'Scissors': 1,
    'Paper': 2,
    'Rock': 3,
}

print('Welcome to Scissor Paper Rock Game!')
n = input('Please enter your name to continue:')
print('\n1. Scissor \n2. Paper \n3. Rock')

draw=0
comp = 0
you = 0
round = 0
statement = ''
while True:
    (a, b) = random.choice(list(mylist.items()))
    d = int(input('Choose:(Type 1 for Scissor, 2 for Paper & 3 for Rock)'))
    round += 1
    if (0 < d) & (d < 4):
        print(f'\nComputer\t: {a}')
        for (k,v) in mylist.items():
            if d == v:
                print(f'{n}\t\t: {k}')
        print('')
        print('+'+'-'*55+'+')
        print('|'+'Game Statistics'.center(55,' ')+'|')
        print('+'+'-'*55+'+')
        
        if d == b:
            draw += 1
            statement = 'Draw!'
            
        elif d == mylist['Scissors']:
            if mylist['Rock']>d:
                you += 1
                statement = 'You Won!'

        elif d == mylist['Paper']:
            if mylist['Scissors']<d:
                you += 1
                statement = 'You Won!'

        elif d == mylist['Rock']:
            if mylist['Paper']<d:
                you += 1
                statement = 'You Won!'
        else:
            comp += 1
            statement = 'You Lose!'
    else:
        print('\nInvalid Input')
        round -=1

    print('|'+f'Total Round: {round}'.center(27,' ')+'|'+f'Total Draw: {draw}'.center(27,' ')+'|')
    print('|'+f'Computer: {comp}'.center(27,' ')+'|'+f'{n}: {you}'.center(27,' ')+'|')
    print('|'+' '*55+'|')
    print('|'+' '*3+'+'+'-'*47+'+'+' '*3+'|')
    print('|'+' '*3+'|'+f'{statement}'.center(47,' ')+'|'+' '*3+'|')
    print('|'+' '*3+'+'+'-'*47+'+'+' '*3+'|')
    print('|'+' '*55+'|')
    print('+'+'-'*55+'+')

    p = input("Wanna Play Again?( If yes, Press 'y' & Enter. )")
    if p != 'y':
        break

# %%
