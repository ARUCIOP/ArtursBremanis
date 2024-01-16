fails = open('dati.txt','a',encoding='utf-8')
fails.write('ingvera sula garšo pēc suši!!\n')
#katru reizi palaižot programu, texts tiek pievienots klāt

fails = open('dati.txt','r',encoding='utf-8')
print(fails.read())

fails = open('dati.txt','w',encoding='utf-8')
fails.write('Mācos rakstīt failā\n')
print(fails.read())

fails.close()