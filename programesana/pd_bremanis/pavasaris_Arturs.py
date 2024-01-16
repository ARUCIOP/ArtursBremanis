import math
print('Faktoriāla apreiķināšana')
n=1
turpinat = 'j'
def zvaigznites(zvaigznites):
    return '*******************************************************'


def atstarpes(n):
     return print(),print()


def factorial(skaitlis):

        if skaitlis<=0 or skaitlis>=13:
            return 1
        else:
            return skaitlis * factorial(skaitlis-1)
        



while turpinat == 'j':#turpinās kamēr atbildēs ar j uz jautājumu vai turpinās
    print(zvaigznites(zvaigznites))#izsauc zvaigznes funkciju
    
    skaitlis=int(input("Ievadiet veselu pozitīvu skaitli(mazāku par 13)\n"))
    print('Faktoriāls:',factorial(skaitlis)) #izsauc faktoriāla apreķina funkciju
    turpinat = input('Vai jūs vēlaties turpināt?(j/n)')
    if turpinat == 'j': #pārbauda vai vēl turpina ja nē tad pasaka paldies
         continue
    else:
        print('Paldies!')
    print(atstarpes(n))#izsauc atstarpes funkciju (p.s. es nevarēju dabūt (None, None) nost, bet tāpat tā strādā)
    

