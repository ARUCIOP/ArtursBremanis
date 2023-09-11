# Pēc Roberta un Jēkaba specifikācijām
parametri = input("Ievadi cik kg ābolu jums ir, cik maksā cukurs 1 kg (formāts (tikai cipari) kg, eiro): ") 
dotie = [float(lieta.strip()) for lieta in parametri.split(",")] #sadala ievadi divos mainīgajos un pārveido tos par float
print("Cukura cena: ", round((dotie[0] * dotie[1]), 2), "EUR") #tiek aprēķinātas un izvadītas cukura izmaksas (receptē ābolu, cukura proporcija ir 1)
