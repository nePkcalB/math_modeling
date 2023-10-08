a, b, c = list(map(int, input('').split()))
D = b**2 - 4*a*c

if D<0: print('Корней нет')
else: 
    
    x1 = (-b + D**(1/2))/2*a
    x2 = (-b - D**(1/2))/2*a
    
    print(f'x = {x1}') if x1 == x2 else\
    print(f'x1 = {x1}, x2 = {x2}')