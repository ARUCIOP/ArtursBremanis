f = open('Demo.txt','r',encoding='utf-8')#atver failu
print(f.read())#izdrukā faila saturu

f = open('Demo.txt','r',encoding='utf-8')
print(f.readline())# nolasa pirmo rindiņu

#f = open('Demo.txt','r',encoding='utf-8')#atver failu
print(f.read(21))#izdrukā pirmos x daudzuma simbolus ieskaitot atstarpes un komatus un punktus.

f.close()