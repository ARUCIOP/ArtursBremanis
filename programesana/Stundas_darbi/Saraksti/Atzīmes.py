#izveidot sarakstu atzīmes ar punktiem tstā iegūtajiem pungtiem. Ar for funkciju iziet caur visam sarakstam
#ar elif nosacījumiematzime_b
#ja >= 90 A, >= 80B, starp 70 un 80 C no 60 -70 D zem 60 -f
#grūtāk var pielikt datu izcadi.atkarībā no ievadītā skaitļa, parādīt burtu

atzimes = ["78","93","81","87",]
rez = []
for burts in atzimes:
    if burts >= 90:
        atzime = "A"
    elif burts >= 80:
        atzime = "B"
    elif burts >= 70:
        atzime = "C"
    elif burts >= 60:
        atzime ="D"
    else:
        atzime = "F"
rez.append([burts, atzime])
