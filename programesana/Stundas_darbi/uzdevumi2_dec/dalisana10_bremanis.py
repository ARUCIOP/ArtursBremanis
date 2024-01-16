x = 1 
while x < 41: #atkārto skaitli kamēr skaitlis ir 40
  if x>0:
    a1=x/2
    a2=x//2 
    b1=x/4
    b2=x//4
    if a1 == a2 and b1 == b2: # pārbauda vai dalās bez atlikuma ar 2 un 4.
        print(x,":dalās ar 2 un 4 bez atlikuma.",)#pasaka ja dalās ar 2 un 4.
    elif a1 == a2: # pārbauda vai dalās bez atlikuma ar tikkai 2.
        print(x,":dalās ar 2 bez atlikuma.")#pasaka ja dalās ar 2.
    elif b1 == b2: # pārbauda vai dalās bez atlikuma ar tikkai 4.
        print(x,":dalās ar 2 bez atlikuma.")#pasaka ja dalās ar 4.
    else:
        print(x)#ja nedalās ar 2 vai 4 izprintē tikai skaitli.
    x += 1
