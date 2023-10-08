
def main(a, b, c):

    if max(a, b, c) >= (sum([a, b, c]) - max(a, b, c)):
        print('Такого треугольника не существует')
        return 0
    
    if max(a, b, c)**2 == min(a, b, c)**2 + (sum([a, b, c]) - max(a, b, c) - min(a, b, c))**2:
        print('Прямоугольный треугольник')
        return 0

    if max(a, b, c)**2 > min(a, b, c)**2 + (sum([a, b, c]) - max(a, b, c) - min(a, b, c))**2:
        print('Тупоугольный треугольник')
        return 0

    if max(a, b, c)**2 < min(a, b, c)**2 + (sum([a, b, c]) - max(a, b, c) - min(a, b, c))**2:
        print('Остроугольный треугольник')
        return 0


if __name__ == '__main__':
    a, b, c = list(map(int, input('').split()))
    main(a, b, c)

