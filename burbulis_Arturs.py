import random
elementi = int(input('Cik garu virkni jūs vēlaties?: '))
saraksts_atzimes = []
saraksts_vardi = []

def burbulis (saraksts_atzimes):
    elementi = len(saraksts_atzimes) #kopējais elementu skaits
    for i in range(elementi):
        for j in range(0,elementi-i-1): #elements nonāk pareizajā vietā
            #izlaiž pēdējo (sakārtoto) elementu
            if saraksts_atzimes[j]>saraksts_atzimes[j+1]:
                saraksts_atzimes[j],saraksts_atzimes[j+1]=saraksts_atzimes[j+1],saraksts_atzimes[j]
                saraksts_vardi[j],saraksts_vardi[j+1]=saraksts_vardi[j+1],saraksts_vardi[j]








#############################################################################################################################################
saraksts = [7,6,5,4,3,2,1,5]
sakartots_saraksts = []
x = 1
for i in saraksts: 
        if saraksts[i] == 0:
            sakartots_saraksts.append(saraksts[i])
            x=x+1
            print(sakartots_saraksts,'------------')

#############################################################################################################################################
            


def sakartot_bubble():
    for i in range(elementi):
        vardi = input(f'Ievadiet {i+1}. solēna vārdu: ')
        skaitlis = int(input(f'Ievadiet {i+1}. skaitli: '))
        saraksts_atzimes.append(skaitlis)
        saraksts_vardi.append(vardi)

    burbulis(saraksts_atzimes)
    print('sakārtos saraksts: ')
    k=0
    for skaitlis in saraksts_atzimes:
        print(saraksts_vardi[k], skaitlis, end='; ')
        k=k+1



sakartot_bubble()
#sakartot_izveles()