pilsetu_saraksts = ["Sigulda\n","Rīga\n","Daugaupils\n",]
valsts_saraksts = ["Igaunija\n","Latvija\n","Lietuva\n",]

fails = open('dati2.txt','w',encoding='utf-8')
fails.writelines(pilsetu_saraksts)
fails = open('dati2.txt','r',encoding='utf-8')
print(fails.read())

#pārrakstīt faila saturu un 3 valstīm
fails = open('dati2.txt','w',encoding='utf-8')
fails.writelines(valsts_saraksts)

fails = open('dati2.txt','r',encoding='utf-8')
print(fails.read())
