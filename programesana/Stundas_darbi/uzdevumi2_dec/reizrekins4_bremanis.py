#reizināmais
x = int(input("Ievadiet x skaitli no 0-10:")) #reizināmais
if x>10: #pārbauda vai ir lielāks par 10
   a = 10
elif x<0: #pārbauda vai ir mazāks par 0
    a = 0 #dators ieliek 
else: #ja ir skaitlis no 0-10 tad reizina ar ievadīto skaitli
    a = x

y = 1 #maina y no 1 līdz 10 lai var sareizināt ar ievadīto x
while y < 11:
  print(x,"*",y,"=", a*y)
  y += 1
