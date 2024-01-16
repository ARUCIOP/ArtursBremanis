import math
apskatit = 'j'
while apskatit == 'j':
    prece = input("ievadiet preces nosaukumu: ")
    preces_cena = float(input("ievadiet preces cenu (eiro): "))
    if preces_cena < 0: #ievietots lai pārbaudītu vai nav cena nav negatīva un nav 0.
        print("Error. Cena nevar būt negatīva")
        exit

    preces_daudzums = int(input("ievadiet preces daudzumu: "))
    if preces_daudzums < 0: #ievietots lai pārbaudītu vai nav daudzums nav negatīvs un nav 0.
        print("Error. daudzums nevar būt negatīvs vai 0")
        exit

    kop_preces_cena = preces_cena*preces_daudzums #kopējā cena bez atlaides
    print("Bez atlaides kopā maksā: ",kop_preces_cena,"(",preces_cena,"x",preces_daudzums,")")
    rimi = kop_preces_cena*0.7# Rimi 30% atlaides aprēķins 

    m_karte = input("Vai jums it Maximas veikala atlaižu karte? (j/n): ")
    if m_karte == "j":#ja ir atlaižu karte tad izvēlās maximas veikala cenu ar atlaidi.
        maxima = kop_preces_cena*0.6
        print_maximas_text = "ar atlaidi"#mainīgais kas izmainīs print funkcijas tekstu lai pielāgotos situācijai(ir vai nav atlaižu kartes)
    else: #ja nav atlaižu kartes dod parasto maximas cenu
        maxima = kop_preces_cena 
        print_maximas_text = "bez atlaides"

    TOP_karte = input("Vai jums it TOP veikala atlaižu karte? (j/n): ")
    if TOP_karte == "j":#ja ir atlaižu karte tad izvēlās TOP veikala cenu ar atlaidi.
        TOP = kop_preces_cena*0.5
    else:#ja nav atlaižu kartes dod parasto maximas cenu
        TOP = kop_preces_cena*0.8

    if preces_daudzums > 2:#parbauja ja ir vairāk kā 2 preces tad dot cenu ar 30% atlaidi, ja nē tad parasto cenu bez atlaides
        rimi_mini = kop_preces_cena*0.7
    else:
        rimi_mini = kop_preces_cena

    mini_vesko = (preces_daudzums- math.floor(preces_daudzums/2) )*preces_cena

    print("Kopējā cena ar 30%"" atlaidi rimi veikalā: ","%.2f"%rimi)#pēc 30% ieliktas divas dubūtltās pēdiņas lai nobeigtu un uzsāktu textu jo % zīme iekrāsojas tā kā kāda funkcija ja tās divas dubūltāspēdiņas nav ieliktas
    print("Kopējā cena ",print_maximas_text,"veikalā: ","%.2f"%maxima)
    print("Kopējā cena veikalā: ","%.2f"%TOP)
    print("Kopējā cena veikalā: ","%.2f"%rimi_mini)
    print("Kopējā cena veikalā: ","%.2f"%mini_vesko)

    apskatit = str(input("Vai gribat turpināt apskatīt cenas?(j/n)"))
else:
    print('Paldies par iepirkšanos!!')
    exit

