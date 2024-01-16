import pprint  #šis ir lai būtu iespējama funkcija pprint kas izprintē datus vertikāli
#auguma garumi: 172 185 164 184 162 164 165 167 177 184 165 180
augums_cm ={
    1:172,
    2:185,
    3:164,
    4:184,
    5:162,
    6:164,
    7:165,
    8:167,
    9:177,
    10:184,
    11:165,
    12:180
}
print('Saraksts ar skolēnu augumiem: ')
pprint.pprint(augums_cm) #pprint izprintē vertikāli datus
videja_vertiba = sum(augums_cm)/12
print('Šo datu vidējā vērtība :',videja_vertiba)


print('**************************************************')
atbilde = input('Vai jūs vēlaties pievienot skolēnu garumu?(uzrakstot "stop" programma beigsies)(j/n): ')
if atbilde == 'stop':#kad atbildē uzrakstīts stop izpildās ši funkcija
    print('Programma ir apstādināta.')
    exit()

while atbilde=='j':
    augums_cm[int(input('Ievadi personas kārtas skaitli (kas ir par vienu lielāks nekā pedējais): '))] = int(input('Ievadi jaunās personas garumu: '))
    #līija virs atļauj ievadīt lietotājam skolnieka augumu un viņ kārtas skaitli kas tiks pievienota vārdnīcai
    print('**************************************************')
    atbilde = input('Vai jūs vēlaties turpināt pievienot skolēnu garumu?(uzrakstot "stop" programma beigsies)(j/n): ')
    if atbilde == 'stop':#kad atbildē uzrakstīts stop izpildās ši funkcija
        print('Programma ir apstādināta.')
        exit()
print('**************************************************')
atbilde = input('Vai jūs vēlaties izdzēst skolēnu garumu?(uzrakstot "stop" programma beigsies)(j/n): ')
if atbilde == 'stop':#kad atbildē uzrakstīts stop izpildās ši funkcija
    print('Programma ir apstādināta.')
    exit()

while atbilde=='j':  
    kārtas_skaitlis = int(input('Ievadiet skolnieka kārtas skaitli ko vēlatis izdzēst.: '))
    print('Jūs izdzēsāt ',kārtas_skaitlis,':',augums_cm[kārtas_skaitlis])
    augums_cm.pop(kārtas_skaitlis)
    print('**************************************************')
    atbilde = input('Vai jūs vēlaties turpināt izdzēst skolēnu garumu?(uzrakstot "stop" programma beigsies)(j/n): ')
    if atbilde == 'stop':#kad atbildē uzrakstīts stop izpildās ši funkcija
        print('Programma ir apstādināta.')
        exit()
print('**************************************************')
print('Šis ir jūsu jaunais saraksts: ')
pprint.pprint(augums_cm)#pprint izprintē vertikāli datus
videja_vertiba = sum(augums_cm)/int(input('Ievadiet cik kopā ir skolēnu.:'))
print('Šo datu vidējā vērtība :',videja_vertiba)

