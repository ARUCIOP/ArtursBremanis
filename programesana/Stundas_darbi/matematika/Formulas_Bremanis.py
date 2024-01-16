import math
import random
R = int(input("Ievadiet riņķa līnijas rādiusu: ")) #ievada rādiusu
print("%.1f"%R) 
rez1 = 2*math.pi*R    #aprēķini priekš riņķa līnijas garuma
print("Riņķa līnijas garums: ", "%.2f"%rez1)
rez2 = math.pi*(math.pow(R,2))    #aprēķini priekš riņķa laukuma
print("Riņķa līnijas laukums: ", "%.2f"%rez2)
k1 = int(input("Ievadiet Taisnleņķa pirmās katetes garumu: ")) #ievada pirmās katetes garumu
k2 = int(input("Ievadiet Taisnleņķa otrās katetes garumu: ")) #ievada otrās katetes garumu
h = math.sqrt(math.pow(k1,2)+math.pow(k2,2))    #aprēķina hipetanūzas garumu
print("Taisleņķa trijstūra hipetanūzas garums: ","%.2f"%h)
print("Gadījuma skaitlis no 0 -1: ",random.uniform(0, 1))