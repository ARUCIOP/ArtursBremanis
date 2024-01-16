file_name = 'dzest.txt'
delete_me = 'KO gribi tagad darīt???'#glabā tektu ko var izdzēst

try:
    with open(file_name,'r',encoding='UTF-8') as data:
        #r atver failu l;assīšanai un saglabā mainīgajā datā
    #readlines ielasa visas rindas no faila un saglabā tās saraksr'
        rows = data.readlines()

    with open(file_name,'w',encoding='UTF-8') as data: #atver rakstīšanai
        #iziet visām sarakta rindām:
        for row in rows:
            if delete_me not in row:
                data.write(row)
        #ja neatrod vārdu tad ieraksta šo rindu atpakaļ
        #failā ignorējot vai izdzēšot rindas kuras atbilst     
    print(f'Rindas ar vārdu"{delete_me}" ir veiksmīgi dzēstas no faila"{file_name}".')
except FileNotFoundError:
    print('Kļūda: data "{file_name}"nav atrasts')
except Exception as e:
    print(f'Kļūda: Neparedzēta kļūda - {e}')