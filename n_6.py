for y in range(1, 11):

    try: print(stroka)
    except: pass
    
    stroka = ''
    for x in range(1, 10):

        stroka += f'{x*y} '