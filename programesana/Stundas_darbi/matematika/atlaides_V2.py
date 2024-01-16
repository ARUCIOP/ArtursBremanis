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
    atl_kart_max = input("Vai jums ir veikala maksima atlaižu karte?(j/n)")
    atl_kart_top = input("Vai jums ir veikala TOP atlaižu karte?(j/n)")
    kop_preces_cena = preces_cena*preces_daudzums #kopējā cena bez atlaides

    if atl_kart_max == "j":#ja ir atlaižu karte tad izvēlās maximas veikala cenu ar atlaidi.
        maxima = kop_preces_cena*0.6
        print_maximas_text = "ar atlaidi"#mainīgais kas izmainīs print funkcijas tekstu lai pielāgotos situācijai(ir vai nav atlaižu kartes)
    else: #ja nav atlaižu kartes dod parasto maximas cenu
        maxima = kop_preces_cena 
        print_maximas_text = "bez atlaides"
    if atl_kart_top == "j":#ja ir atlaižu karte tad izvēlās TOP veikala cenu ar atlaidi.
        TOP = kop_preces_cena*0.5
    else:#ja nav atlaižu kartes dod parasto maximas cenu
        TOP = kop_preces_cena*0.8

    if preces_daudzums > 2:#parbauja ja ir vairāk kā 2 preces tad dot cenu ar 30% atlaidi, ja nē tad parasto cenu bez atlaides
        rimi_mini = kop_preces_cena*0.7
    else:
        rimi_mini = kop_preces_cena

    mini_vesko = (preces_daudzums- math.floor(preces_daudzums/2) )*preces_cena
    

        
    
    
    
    
    
    
    
    
    












    
    
    apskatit = str(input("Vai gribat turpināt apskatīt cenas?(j/n)"))
else:
    print('Paldies par cenu salīdzināšanu!')
    exit