#int pārveidošana par str(a un b saskaita)
#a un b kā teksts tiek konatenēti(concat)
a,b=5,7
print("skaitlis",a+b)  #int mainīgie tiek saskaitīti
print("teksts",str(a)+str(b))  # kā texts tiek concatots
a= str(a)
b= str(b)
print("teksts",a+b)

print(" ")
print(" ")

#string pārveidošana par int
s="123"
t="456"
print(s+t,type(s+t))
a=int(s) #virkni s pārveido par int tipa mainīgo a
b=int(t) #virkni t pārveido par int tipa mainīgo b
print(a+b,type(a+b))

print(" ")
print(" ")

