sayi = 1
liste = []
while True:
    for i in range(1,20):
        if sayi%i==0:
            liste.append(sayi)
            print(liste[-1])
        elif sayi%i != 0:
            sayi +=1
            i = 1


