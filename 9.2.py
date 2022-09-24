def kolvo(num, a=0):
    return kolvo(num // 10, a + 1) if num else a
 
print(kolvo(int(input())))