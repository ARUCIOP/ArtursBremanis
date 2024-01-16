import math
'''
18.42 uz m2
2
'''
cena_rullim = float(input('Ievadiet linoleja cenu uz 1 m2: '))

vai_zin_telpas_platumu = input('Vai jau zinat telpas laukumu?(j/n)')

if vai_zin_telpas_platumu == 'n':
    telpas_garums = float(input('Cik gara ir telpa?(m2): '))#8
    telpas_platums = float(input('Cik plata ir telpa?(m2): '))#12
    telpas_laukums = telpas_garums*telpas_platums
    print('Telpas  laukums ir ',telpas_laukums,'m2')
else:
    telpas_laukums = float(input('Kāds ir telpas laukums?(m2): '))

rula_laukums = round.roof()
telpas_laukums
