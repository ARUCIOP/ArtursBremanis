print('--------------------------------------------------')
print('Esiet sveicināti izmaksas apreiķināšanas programmā!')
print('Šī programa uzdos jums jautājumus par jūsu pasūtījumu un tad apreiķinās izmaksas!')
print('--------------------------------------------------') 
skaits = int(input('Cik krekuls jūs vēlaties pasūtīt?: '))  #iespēja ievadīt kreklu daudzumu
print('--------------------------------------------------')
lielums = input('ievadiet krekla lielumu.(tas cenu neietekmē)\n(XS,S,M,L,XL,XXL): ')  # iespēja ievadīt krekla lielumu
if lielums == 'XS'or'S'or'M'or'L'or'XL'or'XXL':
  print('ievadītais krekla izmērs ir:',lielums,'\n--------------------------------------------------')
else:
  print('Tika ievadīti nepareizi dati.\n--------------------------------------------------')
apdruka = input('''Kādu apdrukas veidu jūs vēlaties? \n(izvēlaties un uzraktiet precīzi un vienu no šiem aprukas veidiem)\n(Teksts ir 5 eiro, zīme ir 7 eiro un fotogrāfija ir 20 eiro)\n(TEKSTS, ZIME, FOTO): ''')

if apdruka == 'TEKSTS':  #pārbauda kas tiek uzraktīts un pielāgota cena ( ja pareizi tikka uzraktīts)
  apdrukasCena = 5
elif apdruka == 'ZIME':
  apdrukasCena = 7
elif apdruka == 'FOTO':
  apdrukasCena = 20
else:
  print('--------------------------------------------------\nApdrukas veids ir ievadīts nepareizi.\n--------------------------------------------------')
  exit()

print('--------------------------------------------------')
piegade = bool(int(input('Vai jūs vēlatis iegādāties kreklus ar piegādi?\n(Ja vēlaties tad 1, ja nevēlaties tad 0): ')))  # jautā vai lietotājs vēlas izvēlēties piegādi.

if piegade == True:  # pārmaina piegādes mainīgo lai čēkā būtu redzams ka tika vai netika izvēlēta piegāde
  piegade = 'izvēlēta.'
else:
  piegade = 'neizvēlēta.'

kopejaCena = skaits * apdrukasCena  # apreiķina kopējo cenu bez piegādes un bez 5%atlaides ja pārsniedz 100 eiro
if kopejaCena < 50:  # izveidota if funkcija lai uzīnātu vai piegādes cenu ir vajadzība pievienot pie gala cenas
  piegadeCena = 15
  galaCena = kopejaCena + piegadeCena  # ja izvēlēta piegāde tad ja nepārsniedz 50 eiro tā tiek pieskaitīta
else:  # ja nav izvēlēta piegāde tad ja pārsniedz 50 eiro tā netiek pieskaitīta
  piegadeCena = 0
  galaCena = kopejaCena

if galaCena > 100:  # ar if funkciju apreiķina vai ir nepiečiešama 5% atlaide gala cenai
  atlaide = '5%'  # piemēro atlaidi kā 5% lai uz čeka tas tiktu parādīts
  galaCena = galaCena - (galaCena / 100 * 5)  #gala cenai tiek atņempti 5%
else:
  atlaide = '0%'  # piemēro atlaidi kā 0% lai uz čeka tas tiktu parādīts

print('--------------------------------------------------\nJūsu kopējās izmaksas:\nPasūtīts/ti', skaits, ' krekls/li ar lielumu',lielums, '\nIzvēlētā apdruka ir', apdruka, '\nPiegāde ir',piegade,'\n--------------------------------------------------','\nJūsu čeka apreiķini:\nkrekla skaits=', skaits,'\n*\napdrukas veida cena=', apdrukasCena, '\n+\npiegādes cena=',piegadeCena, '\n+\ndotā atlaide=', atlaide,'\n=','\nJūsu kopējās izmaksas:', galaCena, 'eiro.\n--------------------------------------------------')  #parādīts kas ir izvēlēts
#print('Jūsu čeka apreiķini:\nkrekla skaits=', skaits,'\n*\napdrukas veida cena=', apdrukasCena, '\n+\npiegādes cena=',piegadeCena, '\n+\ndotā atlaide=', atlaide,'\n=','\nJūsu kopējās izmaksas:', galaCena, 'eiro.\n--------------------------------------------------')  # parādīta ķā veidojas gala cena

galajaut = input('Vai jūs vēlaties pasūtīt šo pašu pasūtījumu vēlreiz? (j/n): ')  #tie uzjautāts lietotājs vai vēlās vēlreiz pasūtīt šo pašu
if galajaut == 'j':
  galaCena = kopejaCena * 2 + piegadeCena  #sareizina gala cenu ar 2 bet ja iepriekš nepārniedza 550 eiro tad tikkai 1 reizi pieskaita piegādes cenu jo piegādās ar to pašu cenu ( pet kā ir pasūtīti 2 dažādi pasūtījumi ja abi kopā pārniedz 50 tas nenozīmē ka piegāde tiks ņempta nost)
  galaCena = galaCena - (galaCena / 100 * 5)  # noņem 5%
  print('Jūsu kopējās izmaksas par diviem pasūtījumiem:', galaCena,
        'eiro.')  #parāda 2X kopējo cenu
  print('--------------------------------------------------\nIzbaudiet atlikušo dienu!!!')

elif galajaut == 'n':
  citsPasutiums = input('Vai vēlaties pasūtīt cita veida pasūtījumu?(j/n): ')  #uzjautā vai vēlas cita veida pasūtījumu nevis tādu pašu
  
  if citsPasutiums == 'j':
    print('Tad lūdzu pieraktiet jūsu Gala cenu un sāciet programmu no jauna. (:')
  else:
    print('--------------------------------------------------\nIzbaudiet atlikušo dienu!!!')
