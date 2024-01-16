file_name = 'dzest.txt'
jautajums = input('Ko gribi ierakstīt failā?: ') 

try:
    with open(file_name,'a',encoding='UTF-8') as fails: #atver rakstīšanai
        fails.write('\n'+jautajums)
    print(f'Rindas ar vārdu"{jautajums}" ir veiksmīgi ieraktīta faila"{file_name}".')


except FileNotFoundError:
    print('Kļūda: data "{file_name}"nav atrasts')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda - {e}')