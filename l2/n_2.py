a = int(input('первый член: '))
q = int(input('знаменатель: '))
k = int(input('количество : '))

[print(a*(q**(i))) for i in range(k)]