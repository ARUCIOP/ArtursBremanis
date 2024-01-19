saraksts = [7,6,5,4,3,2,1,5]
sakartots_saraksts = []
x = 1
for i in saraksts: 
        if saraksts[i] == 0:
            sakartots_saraksts.append(saraksts[i])
            x=x+1
            print(sakartots_saraksts,'------------')
