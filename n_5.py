words = ['покрытая ...', 'кожиц..й', 'держится на ...', 
         'ножк..', 'затянута ...', 'нижняя ...',  'шляпк..']

s = f'Шляпка гриба, {words[0]} {words[1]}, '
s += f'{words[2]} {words[3]} . Снизу шляпка {words[4]} '
s += f'пленкой. Когда ее уберешь, откроется {words[5]} '
s += f'сторона {words[6]} .'

print(s)

for i in range(len(words)):
    stroka = input(f'{words[i]}: ')
    words[i] = words[i].replace('...', stroka, 1)
    words[i] = words[i].replace('..', stroka, 1)

s = f'Шляпка гриба, {words[0]} {words[1]}, '
s += f'{words[2]} {words[3]}. Снизу шляпка {words[4]} '
s += f'пленкой. Когда ее уберешь, откроется {words[5]} '
s += f'сторона {words[6]}.'

print(s)