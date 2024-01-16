##izveido jaunu faila nosaukumu
fails = open('ziema.txt','w',encoding='UTF-8') # raksta vai izveido jaunu failu



#ieraksta failā datus
saraksts = ['Alūksne\n','Valmiera\n','balvi\n']
fails.writelines(saraksts)
fails.write('čau es eju 11. klasē!!')
fails.close()


#faila satura pāraktīšanas
fails = open('ziema_copy.txt','w+',encoding='UTF-8')
fails.write('čau es eju 11. klasē!! \nUn tu?\n')
fails = open('ziema_copy.txt','w+',encoding='UTF-8')   #faila parādīšana uz ekrāna
print(fails.read())                #faila parādīšana uz ekrāna
fails.close()



fails = open('ziema_copy.txt','a+',encoding='UTF-8')
fails.write('Cerams puzdienas šodien būs garšīgas')
fails.close()


