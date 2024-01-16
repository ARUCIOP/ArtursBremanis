import math #šo raksta sākumā tikkai vienu reizi!!!!!!!!!!
#skaitlis = int(input("ievadi skaili: "))
skaitlis = 21.6
print('Noalaļots uz leju',math.floor(skaitlis))
print("noapaļot uz augšu",math.ceil(skaitlis))

print('PI vērtība',math.pi) #aTGRIEŽ PI VĒRTĪBU
print('kāpināšana',math.pow(skaitlis,3)) #1. skaitlis ko kāpina un 2. skaitlis cik reizes kāpina(pakāpe)

#skaitļu formatēšana
x = 2346121380475/2983423 
print("bez formatēšanas",x)
print("ar formatēšanu","%.4f"%x)             #pirmais variants
print("Ar formatēšanu:" "{:.4f}".format(x))  #otrais variants
