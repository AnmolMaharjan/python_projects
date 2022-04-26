# %% Grocery Bill

from turtle import update


t = {
    'Milk_tea': 20,
    'Black_tea': 10,
    'Milk_coffee': 50,
    'Black_coffee': 40,
    'Lemon tea': 20,
    'Hot_lemon': 20,
    'Doughnut': 20,
    'Sel': 20,
    'Puff': 10,
    'Bun': 10,
    'Biscuit': 10
}

print('Menu:')
for i, (k,v) in enumerate(t.items()):
    print(f'{str(i+1):<5}' +f'{k:<15}' +str(v).center(10, ' '))

try:
    r = 0
    b=[]
    print("")
    print("")
    print('-'*51)
    print("")
    print("")
    print(' '*15 +'ANMOL STORE'.center(21, ' ') + f"{'April 4, 2022':<15}")
    print(' '*15 +'Thecho, Lalitpur'.center(21, ' ') + f"{'9860026488':<15}")
    print('-'*51)
    print('S.N.'.center(6, ' ')+f"{'Particulars':<15}" + 'Rate'.center(10, ' ') + 'Qty'.center(10, ' ') + 'Amount'.center(10, ' '))
    print('-'*51)
    n = int(input('\nBought Item number:'))
    while n != 0:
        n = int(input('\nBought Item number:'))
        for i, (k,v) in enumerate(t.items()):
            if n==i+1:
                r += v
                b.append((k, v))
                q=1
                print(str(i+1).center(6, ' ') +f"{k:<15}" + str(v).center(10, ' ')  + str(q).center(10, ' ')  + str(v).center(10, ' '))
    # print("")
    # print('-'*51)
    # print(' '*31+' '+'Total'.center(10, ' ')+str(r).center(10, ' '))

except ValueError:
    print('Please enter numbers from above list Only!')

print("")
print('-'*51)
print(' '*31+' '+'Total'.center(10, ' ')+str(r).center(10, ' '))


# %%
0