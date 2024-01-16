lietotajvards = "Arturo"
parole = "12yes"
reizes = 5
meig = 0
a=1 #mainīgais kas ja izmainīsies beiks while funkciju
b=6 #mainīgais kas ja izmainīsies beiks while funkciju
turpināt = 0
while a < b:
    print("ievadiet lietotājvārdu: ")
    lietotājvards_meig = str(input())
    
    if lietotājvards_meig == "stop" or lietotājvards_meig == "iziet":
            break#programa beidzās
    if lietotājvards_meig == lietotajvards:
        liet_vards_atb = "P"   #lietotājvārds ir pariezi uzrakstīts
    else:
        liet_vards_atb = "N" #lietotājvārds ir nepariezi uzrakstīts


    print("ievadiet paroli:")
    paroles_meig = str(input())
    print()#tukša līnija lai smukāk izskatās
    paroles_garums = len(parole)
    if len(paroles_meig) == paroles_garums:
        print("Parole ir 5 rakstzīmes gara")
    else:
        print("parole nav 5 rakstzīmes gara")
    if paroles_meig == "stop" or paroles_meig == "iziet":
            break     #programa beidzās
    if paroles_meig == parole:
        paroles_atb = "P"    # parole ir pareiza
    else:
        paroles_atb = "N"    # parole ir nepareiza\


    if paroles_atb == "P" and liet_vards_atb == "P":
        print("Lietotājvārds un parola ir pareiza!")
        print()#tukša līnija lai smukāk izskatās
        turpināt = "j"
        
        print("Parole ir 5 burtu gara")
        a= 10 #izmainās lai while funkcija beiktos
    else:
        print("Nepareiza parole vai lietotāj vārds.")
        print("Nepareizo meiģinājuma skaits: ",a)
        print()#tukša līnija lai smukāk izskatās
        a= a+1
        turpināt = "n"
    if a == 6:
        break
if turpināt == "j":
    print("pieslēgšanās veiksmīga")
    print()#tukša līnija lai smukāk izskatās
    print("Ievadiet divus skaitļus, BET abus pozitīvus UN pirmajam skaitlim jābūt mazākam kā otrajam skaitlim.")
    sk1 = int(input("Ievadiet pozitīvu pirmo veselo skaitli:"))
    sk2 = int(input("Ievadiet pozitīvu otro veselo skaitli:"))
