a, b = list(map(int, input('Вводить 2 числа через пробел: ').split()))
ost, chast = 0, 0

try:
    ost = a%b
    chast = a//b

    print('Делится')
    print(f'Частное = {chast}, остаток = {ost}') if ost != 0 \
    else print(f'Частное = {chast}')

except: print('ERROR: second number is 0')
