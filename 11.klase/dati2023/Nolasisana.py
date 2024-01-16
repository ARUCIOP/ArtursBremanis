fail_nosaukums = 'Mana_klase.txt'



#atvērt un lasīt failu
try:
    with open(fail_nosaukums,'r',encoding='UTF-8') as fails:
        for rindina in fails:
            dati = rindina.split()
            #pārbaudīt vai pietiek datu
            if len(dati) >= 3:
                vards = dati[0]
                uzvardsvards = dati[1]
                vecums = dati[2]


                print(f'Vards: {vards}  Uzvārds: {uzvardsvards}  Vecums: {vecums}')
            else:
                print('Kļūda....')

except FileNotFoundError:
    print('errors fails"{faila_nosaukums}" netika atrasts')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')