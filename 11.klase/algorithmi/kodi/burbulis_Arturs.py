import random
elementi = int(input('ievadit cik garu virkni jūs vēlaties'))
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



def insertionSort(arr):
    for i in range(elementi):
        vardi = input(f'Ievadiet {i+1}. solēna vārdu: ')
        skaitlis = int(input(f'Ievadiet {i+1}. skaitli: '))
        saraksts_atzimes.append(skaitlis)
        saraksts_vardi.append(vardi)

    n = len(arr)  
      
    if n <= 1:
        return  
 
    for i in range(1, n):  
        key = arr[i]  
        j = i-1
        while j >= 0 and key < arr[j]:  
            arr[j+1] = arr[j]  
            j -= 1
        arr[j+1] = key  



def sakartot_bubble():
    for i in range(elementi):
        vardi = input(f'Ievadiet {i+1}. solēna vārdu: ')
        skaitlis = int(input(f'Ievadiet {i+1}. skaitli: '))
        saraksts_atzimes.append(skaitlis)
        saraksts_vardi.append(vardi)

        burbulis(saraksts_atzimes)
        print('sakārtos saraksts: ')
        for skaitlis in saraksts_atzimes:
            print(vardi, skaitlis, end='; ')




def sakartot_insertionSort(saraksts_atzimes):


#--------------------------ŠEIT JĀTURPINA IELIKT INCERT--------------------





#sakartot() # bubble sort
#insertionSort(saraksts_atzimes)   #incert sort         