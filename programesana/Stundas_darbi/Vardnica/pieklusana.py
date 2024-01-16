
#izveidot vārdnīcu, kas satur sarakstu
valstis = {
    'Somija':['Helsinki','Rovaniemi','Tampere','Kemijarvi','Jyvaskyle'],
    'Norvēģija':['Oslo','Bergena','Arendāla','Trumse','Molde'],
    'Dānija':['Kopenhāgena','Odense','Esbjerga','Aarhus','Ronne']
}
'''
#1. variants ar for ciklu
for atslega, vertiba in valstis.items():
    for i in vertiba:
        print(atslega, ':', i)
    print('--------------------------')
'''
# 2. variants ar for ciklu vienai atslēgu grupai
for i in valstis['Dānija']:
    print(i)
print('--------------------')
for i in valstis['Norvēģija']:
    print(i)
print('--------------------')
for i in valstis['Somija'][-2:]:
    print(i)
print('--------------------')