import csv

sakotnejie_dati_fails = 'Sakuma_dati.csv'
jaunie_dati_fails = 'jaunie_dati.csv'

#atvērt un nolasīt datus
try:
    with open(sakotnejie_dati_fails,'r',encoding='UTF-8') as sakotnejais_fails:
        lasitajs = csv.DictReader(sakotnejais_fails)
        sakotnejie_dati = list(lasitajs)

        #atjaunošana

        for persona in sakotnejie_dati:
            persona['Vecums'] = int(persona['Vecums'])+1

        
        #ieraksrta jaunus datus jaunā failā

    with open(jaunie_dati_fails,'w', encoding='UTF-8', newline='')as jauns_fails:
        raktitajs = csv.DictWriter(jauns_fails, fieldnames=['Vards','Uzvards','Vecums'])
        raktitajs.writeheader()
        raktitajs.writerow(sakotnejie_dati)
        print(f'dati ir atjaunināti un saglabāti failā"{jaunie_dati_fails}".')


except FileNotFoundError:
    print('errors fails"{sakotnejie_dati_fails}" netika atrasts')
except Exception as e:
    print(f'Kļūda: neparedzēta kļūda - {e}')