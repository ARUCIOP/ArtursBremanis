vardnica = input('Ievadiet vārdu virkni: ')
sakartota_vard = vardnica.split()


x = len(sakartota_vard)
print(sakartota_vard)
file_name = input('kā jūs gribat nosaukt failu:')
file_name = file_name + '.txt'
try:
    with open(file_name,'w',encoding='UTF-8') as fails:
        for x in sakartota_vard:            
            print(str(sakartota_vard))
    print(f'vārdnīce ir ieraktīta "{file_name}" failā.')


except FileNotFoundError:
    print('Kļūda: data "{file_name}"nav atrasts')
except Exception as e:
   print(f'Kļūda: Neparedzēta kļūda - {e}')