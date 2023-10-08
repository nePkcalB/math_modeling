fibanochi = [1, 1]
[fibanochi.append(fibanochi[i-1] + fibanochi[i-2]) for i in range(2, int(input('')))]
print(' '.join(map(str, fibanochi)))