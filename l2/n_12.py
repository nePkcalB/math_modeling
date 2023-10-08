
def main(year):

    if year >= 394:
        print(f'OL 292.{year-394}')    
        return 0
    
    prom = year + 776
    print(f'OL {prom//4}.{prom%4}')

if __name__ == '__main__':
    main(int(input()))
