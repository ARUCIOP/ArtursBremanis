print('--------------------------------------------------\nEsiet sveicināti izmaksas apreiķināšanas programmā!\nŠī programa uzdos jums jautājumus par jūsu pasūtījumu un tad apreiķinās izmaksas!\n--------------------------------------------------')
skaits = int(input('Cik krekuls jūs vēlaties pasūtīt?: '))  #iespēja ievadīt kreklu daudzumu
exit() if skaits <= 0 else ...
lielums = input('--------------------------------------------------\nievadiet krekla lielumu.(tas cenu neietekmē)\n(XS,S,M,L,XL,XXL): ')  # iespēja ievadīt krekla lielumu
if lielums == 'XS'or'S'or'M'or'L'or'XL'or'XXL': print('ievadītais krekla izmērs ir:',lielums,'\n--------------------------------------------------')
else: print('Tika ievadīti nepareizi dati.\n--------------------------------------------------')
apdruka = input('Kādu apdrukas veidu jūs vēlaties? Teksts ir 5 eiro, zīme ir 7 eiro un fotogrāfija ir 20 eiro.\n(izvēlaties un uzraktiet precīzi un vienu no šiem aprukas veidiem)\n(TEKSTS, ZIME, FOTO): ')
if apdruka == 'TEKSTS': apdrukasCena = 5
elif apdruka == 'ZIME': apdrukasCena = 7
elif apdruka == 'FOTO': apdrukasCena = 20
else: print('--------------------------------------------------\nApdrukas veids ir ievadīts nepareizi.\n--------------------------------------------------'),exit()
piegade = bool(int(input('--------------------------------------------------\nVai jūs vēlatis iegādāties kreklus ar piegādi?\n(Ja vēlaties tad 1, ja nevēlaties tad 0): ')))  # jautā vai lietotājs vēlas izvēlēties piegādi.
piegade = 'izveleta' if [piegade==True] else 'neizvēlēta' # pārmaina piegādes mainīgo lai čēkā būtu redzams ka tika vai netika izvēlēta piegāde
kopejaCena = skaits * apdrukasCena  # apreiķina kopējo cenu bez piegādes un bez 5%atlaides ja pārsniedz 100 eiro
if kopejaCena < 50:  piegadeCena = 15; galaCena = kopejaCena + piegadeCena  # ja izvēlēta piegāde tad ja nepārsniedz 50 eiro tā tiek pieskaitīta# izveidota if funkcija lai uzīnātu vai piegādes cenu ir vajadzība pievienot pie gala cenas
else:  piegadeCena = 0 ; galaCena = kopejaCena; 
atlaide = '5%' if galaCena>100 else '0%' # ja nav izvēlēta piegāde tad ja pārsniedz 50 eiro tā netiek pieskaitīta
print('--------------------------------------------------\nJūsu kopējās izmaksas:\nPasūtīts/ti', skaits, ' krekls/li ar lielumu',lielums, '\nIzvēlētā apdruka ir', apdruka, '\nPiegāde ir',piegade,'\n--------------------------------------------------\nJūsu čeka apreiķini:\nkrekla skaits=', skaits,'\n*\napdrukas veida cena=', apdrukasCena, '\n+\npiegādes cena=',piegadeCena,'\n+\ndotā atlaide=', atlaide,'\n=\nJūsu kopējās izmaksas:',galaCena- (galaCena/100*5) if galaCena>100 else galaCena,'eiro.\n--------------------------------------------------')  #parādīts kas ir izvēlēts
galajaut = input('Vai jūs vēlaties pasūtīt tieši šo pašu pasūtījumu vēlreiz? (j/n): ')  #tie uzjautāts lietotājs vai vēlās vēlreiz pasūtīt šo pašu
if galajaut == 'j': print('Jūsu kopējās izmaksas par diviem pasūtījumiem:',(kopejaCena * 2 + piegadeCena) - ((kopejaCena * 2 + piegadeCena) / 100 * 5),'eiro.\n--------------------------------------------------\nIzbaudiet atlikušo dienu!!!')  #parāda 2X kopējo cenu
elif galajaut == 'n':
  citsPasutiums = input('Vai vēlaties pasūtīt cita veida pasūtījumu?(j/n): ')  #uzjautā vai vēlas cita veida pasūtījumu nevis tādu pašu
  if citsPasutiums == 'j': print('Tad lūdzu pieraktiet jūsu Gala cenu un sāciet programmu no jauna. (:')
  elif citsPasutiums == 'n': print('Izbaudiet atlikušo dienu!!!')
  else: print('Ir ievadīti dati kas nav prasīti!')
else: print('Ir ievadīti dati kas nav prasīti!')