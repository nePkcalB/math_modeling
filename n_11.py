def check(n):

    suma = 0
    for i in range(1, n):
        if n%i == 0: suma += i

    if suma == n: return True

for i in range(1, int(input())):

    if check(i): print(i)