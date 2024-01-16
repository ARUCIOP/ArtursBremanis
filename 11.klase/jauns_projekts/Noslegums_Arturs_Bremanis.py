from datetime import datetime
def galvena(): # izprintē sākuma tekstu
    print('-----\nProgrammas sākums:\nSekojiet norādījumiem un kad vēlaties beikt programmu uzraktiet: "stop"\n-----')

def stop(iziet): # pārbauda vai ieraktīts stop un ja ir tad beidz
    if iziet == 'stop':
        print('Programma aizverās!')
        exit()

def nekas(tuksums):   # beidz programmu kad netiek nekas ierakstīts 
    if tuksums == '':
        print('Nekas netika ietaktīts.')
        print('Programma aizverās!')
        exit()

def iegust_datus(): #iegūst visus datus

    global Vards
    Vards = input('Ievadiet savu vārdu: \n') 
    stop(Vards)
    nekas(Vards)

    global eksperimenta_nosaukums
    eksperimenta_nosaukums = input('Ievadiet eksperimenta nosaukumu:\n')
    stop(eksperimenta_nosaukums)
    nekas(eksperimenta_nosaukums)

    global Vieta
    Vieta = input('kur notika šis eksperiments?:\n')
    stop(Vieta)
    nekas(Vieta)
    
    global laiks_datums
    laiks_datums = input('Vai jus gribat lai jums automātiski ievada datumu un laiku vai jūs gribat manuāli tos ieraktīt?(A/M): \n')
    stop(laiks_datums)
    nekas(laiks_datums)
    
    if laiks_datums == 'A': # izvēlās vai automātiski vai manuāli raksta datumu
        laiks_datums = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    elif laiks_datums == 'M':
        laiks_datums = input('Ievadiet šādā formātā: (gggg-mm-dd stunda:minūtes:sekundes)\n')
    else:
        print('Error: dati ievadīti nepareizi, programma tiek aizvērta!\n')
        exit()

def saglabat_datus(): # saglabā datus failā
    with open('datu.txt', 'a',encoding='UTF-8') as dati:
        dati.writelines(f'Lietotāja vārds: "{Vards.capitalize()}" Eksperimenta nosaukums: "{eksperimenta_nosaukums.capitalize()}" Eksperimenta vieta: "{Vieta.capitalize()}" Laiks un datums:"{laiks_datums}"\n')
    print('Jūsu eksperiments tika veiksmīgi pievienots!')
    
while True: # wisu palaiž atkārtoti līdz lietotājs beidz vai kļūdās
    galvena()
    iegust_datus()
    saglabat_datus()

    

