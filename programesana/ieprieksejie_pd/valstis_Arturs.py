valstis_ar_iedzivotajiem={
    'Latvija':1.884,
    'Lietuva':1.801,
    'Igaunija':1.331,
    'Polija':33.75,
    'Spanija':47.42,
    'Somija':5.54,
    'Zviedija':10.42,
    'Norvegija':5.408,
    'Vacija':83.2,
    'Francija':67.75,
}
turpinat = 'j'
while turpinat == 'j':#atkārto kamēr izvēlās stop
    jautajums = (int(input(' 1: Parādīt augoši sakārtotas valstis pēc nosaukumiem\n 2: Parādīt dilstoši sakārtotas valstis pēc nosaukumiem\n 3: Parādīt valstu iedzīvotāju skaitu augošā secībā\n 4: Parādīt valstu iedzīvotāju skaits dilstošā secībā\n 5: Pievienot jaunu valsti un to iedzīvotāju skaitu\n 6: Apskatīt visas valstis\n 7: APSTĀDINĀT PROGRAMMU\n')))
    print('**************************************************************')
    print('Jūs izvēlējāties: ',jautajums)

    if jautajums == 1:
        print('Parādītas valstis augošā secībā.:')
        valstis_aug = sorted(valstis_ar_iedzivotajiem.items())#sakārto pēc atslegas augošā secībā
        for k, d in valstis_aug:
            print(k + ':', d)
        print('**************************************************************')

    elif jautajums == 2:
        print('Parādītas valstis dilstošā secībā.:')
        valstis_dilst = sorted(valstis_ar_iedzivotajiem.items(),reverse=True)#sakārto pēc atslegas dilstošā secībā
        for k, d in valstis_dilst:
            print(k + ':', d)
        print('**************************************************************')

    elif jautajums == 3:
        print('Parādīts valstu iedzīvotāju skaits augošā secībā.:')
        iedzivotaju_aug = sorted(valstis_ar_iedzivotajiem.items(), key=lambda item: item[1])#sakārto pēc iedzīvotāju skaita augošā secībā
        for k, d in iedzivotaju_aug:
            print(k + ':', d)
        print('**************************************************************')

    elif jautajums == 4:
        print('Parādīts valstu iedzīvotāju skaits dilstošā secībā.:')
        iedzivotaju_dilst = sorted(valstis_ar_iedzivotajiem.items(), key=lambda item: item[1],reverse=True)#sakārto pēc iedzīvotāju skaita dilstošā secībā
        for k, d in iedzivotaju_dilst:
            print(k + ':', d)
        print('**************************************************************')
    elif jautajums == 5:
        valstis_ar_iedzivotajiem[(input('Ievadi valsts nosaukumu bez garumzīmēm un pirmo lielo burtu.: '))] = float(input('Ievadi šīs valsts iedzīvotāju skaitus milijonos: '))#atļauj pievienot valsti un to iedzīvotāju skaitu
        
        print('**************************************************************')
        print('Valsts ar iedzīvotājus skaitu veiksmīgi pievienota')
        print('**************************************************************')
        for k, d in valstis_ar_iedzivotajiem.items():
            print(k + ':', d)
        print('**************************************************************')

    elif jautajums == 6:
        for k, d in valstis_ar_iedzivotajiem.items():
            print(k + ':', d)

    elif jautajums == '7':

        print('Jūs izvēlējāties "7" tātad programa ir apstādīnāta.')
        print('**************************************************************')
        turpinat = 'n'
        exit

    else:
        print('error:programma beidzas.')
        print('**************************************************************')
        turpinat = 'n'
        exit