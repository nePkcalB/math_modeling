def check(n):

    for i in range(2, int(n**(1/2))+1):

        if n%i == 0: return False

    return True

a = int(input())
print('')

while a > 1:

    i = 2
    while True:

        if a%i == 0 and check(i):
            print(i)
            a = a//i
            break

        i += 1
