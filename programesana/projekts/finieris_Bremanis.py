import math
garums = float(input('Lūzdu ievadiet podesta garumu (cm).: '))
platums = float(input('Lūzdu ievadiet podesta platumu (cm).: '))
augstums = float(input('Lūzdu ievadiet podesta augstumu (cm).: '))
skaits = int(input('Lūzdu ievadiet podesta skaitu.: '))
podestaLielums = ((garums/100)*(platums/100))
podesta_laukums_kopa = podestaLielums*skaits
finiera_lielums = ((12.5*25.0)/100)
matrealaApreikins = math.ceil(podesta_laukums_kopa/finiera_lielums)
listesApreikins = (garums+platums)*2
print('Jūs pasūdījāt',skaits,'podestu/us ar izmēru',podesta_laukums_kopa,'kvadrātmetri.')
print('Priekš',podesta_laukums_kopa,'kvardātmetra/iem būs nepieciešams/mi',matrealaApreikins,' bērza saplāksnis/ņi.')
print('Priekš',podesta_laukums_kopa, 'kvardātmetra/iem būs nepiecišama līste kas būs',listesApreikins,'cm garumā.')


biezums = float(input('Lūdzu ievadiet finiera biežumu.(12,15,18,21): '))
if biezums==12:    #dabūjam finiera biezuma cenu lai vēlā k izreiķinātu cik būs jā maksā.
    cena_finierim=57.39
elif biezums==15:
    cena_finierim=65.13
elif biezums==18:
    cena_finierim=74.75
elif biezums==21:
    cena_finierim=85.99
else:
    print('ievadīts nepareizi!!')
    exit


finieraIzmaksas = matrealaApreikins*cena_finierim
finieraIzmaksasArPVN = finieraIzmaksas+((finieraIzmaksas/100)*21)#izreiķina PVN
print('Izmaksas prieķš',matrealaApreikins,'daudzuma bērza finiera plāksnēm būs jāmaksā: ',finieraIzmaksas,'Eiro')
print('Klientiem būtu jāmaksā(Ar PVN): ',finieraIzmaksasArPVN)


profilu_daudzums = int(input('Ievadiet cik daudz profilu jūs iegādāsieties.:'))
profilu_cena = profilu_daudzums*7.86
print(profilu_daudzums,'profilu makās',profilu_cena,'eiro.')
profilu_cena_Ar_PVN = profilu_cena+((profilu_cena/100)*21)#izreiķina PVN
print('Klientiem ar PVN jāmaksā',profilu_cena_Ar_PVN)


sturu_daudzums = int(input('Ievadiet cik daudz stūru savienojumus jūs iegādāsieties.:'))
sturu_cena = profilu_daudzums*0.44 
print(sturu_daudzums,'profilu makās',sturu_cena,'eiro.')
sturu_cena_Ar_PVN = sturu_cena+((sturu_cena/100)*21)#izreiķina PVN
print('Klientiem ar PVN jāmaksā',sturu_cena_Ar_PVN)