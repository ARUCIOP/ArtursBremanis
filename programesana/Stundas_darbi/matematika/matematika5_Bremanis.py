print("Programu iztrādātājs: Artūrs Brēmanis")
A = int(input("Ievadiet malas A garumu: ")) # ievada mainīgo A
print("Malas A garums: ","%.1f"%A)
print("    ****   ")
B = int(input("Ievadiet malas B garumu: ")) # ievada mainīgo B
print("Malas B garums: ","%.1f"%B)
print("    ****   ")
aug = int(input("Ievadiet augstumu: "))# ievada mainīgo Augstumu
print("Augstums: ","%.1f"%aug)
print("    ****   ")

s1 = (A*aug)/2   #matemātika priekš trijstūrim
print("Laukums trijstūrim: ",s1)

s2 = ((A+B)/2)*aug  #matemātika priekš trapecei
print("Laukums trapecei: ",s2)
s3 = A*aug   #matemātika priekš paraleogramam
print("Laukums paraleogramam",s3)

print("    ****   ")
print("Paldies!")
