import random
elementi = int(input('ievadit cik garu virkni jūs vēlaties'))
saraksts = []


def burbulis (saraksts):
    elementi = len(saraksts) #kopējais elementu skaits
    for i in range(elementi):
        for j in range(0,elementi-i-1): #elements nonāk pareizajā vietā
            #izlaiž pēdējo (sakārtoto) elementu
            if saraksts[j]>saraksts[j+1]:
                saraksts[j],saraksts[j+1]=saraksts[j+1],saraksts[j]


def sakartot():
    for i in range(elementi):
        skaitlis = int(input(f'Ievadiet {i+1}.skaitli: '))
        saraksts.append(skaitlis)

    burbulis(saraksts)
    print('sakārtos saraksts: ')
    for skaitlis in saraksts:
        print(skaitlis, end='; ')
sakartot()