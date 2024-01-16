c_gadi = int(input("Ievadiet suņa gadus pēc cilvēka gadiem. :")) #ievada cilvēka gadus
if c_gadi < 0:
    print("gadiem vajag būt pozitīviem!")#beidz programu ja gadi<0
    exit()
elif c_gadi <= 2:
    s_gadi = c_gadi * 10.5
else:
    s_gadi = 21 + (c_gadi-2)*4

print("suņa gadi pēc cilvēka gadiem suņa gados:",s_gadi)