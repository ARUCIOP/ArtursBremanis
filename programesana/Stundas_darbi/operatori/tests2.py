#tiek realizēta decimāl skaitļu ievade
#aprei\kināts izteiksmes (x+y)*(x-y)/x-y rezultats

print("ievadīt savu vārdu")
vards = input()
print("jūsu vārds ir:",vards)

print("ievadiet decimālskaitli:")
x = float(input(" ievadiet decimālskaitli")) #jāveiz konvertēšana no input jo input atgriež kā tekstu
print("ievadītais decimālskaitlis",x)

x = float(input(" ievadiet x:"))
y = float(input(" ievadiet y:"))
a = x+y
b = x-y
print(a*b/b)

