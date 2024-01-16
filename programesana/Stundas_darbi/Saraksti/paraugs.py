mans_sarakstst = ["svece",2,"sāli"]# svece būs kā 0 jo sāks skaitīt no nules!!!!!!
TAVS_sarakstst = ["karstmaize","brauniji","kafija"]

liels_sarakstst = mans_sarakstst +TAVS_sarakstst #savieno sarakstu kopā vienā
print(liels_sarakstst)

print("***")
#nokopēt saraksta vērtības un ielikt tās jaunā sarakstā.
mILZIS = ["zupa","dzērveni","taustatūra"]
jauns = list(mILZIS)#izvēlās kuru list kopēs
print(mILZIS)
print(jauns)


#izveidot sarakstu ar 4 krāsām ar 4 krāsu nosaukumiem. Atrast katra elementa garumnu.
krasas = ["zils","zaļš","dzeltens","melns",]
jauns_saraksts = [] #tukš saraksts
for krasa in krasas:
    burti = 0 #katru teizi palaižot sarakstu atgriežas uz 0 !!!!!<!<!<!<!<!!<!<<!<!<!<!!!!svarīgi!!!!!!!!!!!!!!!!!!!!!!!>!>!>!>!>!>!>!>!>!>!>
    for burts in krasa:
        burti +=1
        #vai burti = burti + 1
    pagaidu_saraksts = [krasa, burti]
    jauns_saraksts.append(pagaidu_saraksts)

print(jauns_saraksts)
#Vaidojas: [['zils', 4], ['zaļš', 4], ['dzeltens', 8], ['melns', 5]]