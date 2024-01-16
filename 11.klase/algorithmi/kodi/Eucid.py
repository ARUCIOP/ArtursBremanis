def beigt(stop):
    if stop == 'exit':
        exit()
def funkcija():
    x = int(input('ievadiet veselu skaitli x:\n'))
    beigt(x)
    y = int(input('ievadiet veselu skaitli y:\n'))
    beigt(y)
    if x>y:
        A=x
        B=y
    elif x<y:
        A=y
        B=x
    else:
        print('tika ievadīti nepareizi skaitļi')
    C= A%B
    if C!= 0:
        print(C)
        funkcija()
    else:
        funkcija()

funkcija()