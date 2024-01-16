a = str(input("Vai pie apmeklētājam/darbiniekam atrodas kāds nenodots izdevums?(j/n): "))#pārbauda vai drīkst kaut ko izņempt.
if a == "j":    #pārbauda vai drīks izņempt grāmatu vai nedrīkst.
    print("Piedodiet,bet mēs nedrīkstam izdot neko, kamēr nav atnests iepriekšējais izraksts")
    print("Sāc no jauna.")
elif a == "n":
    print("Drīkst saņempt izrakstus.")
else:
    print("Nepareizi ievadīti dati.")
g_v = str(input("Ko apmeklētājs/darbinieks vēlas izņempt no bibliotēkas?(grāmatu vai žurnālu): "))# ko vēlas izņempt no bibliotēkas?
p_g = str(input("Vai šī grāmata ir pieprasīto izrakstu sarakstā?(j/n): "))#vai atrodas pieprasīto izrakstu sarakstā?

if g_v == "grāmatu" and p_g == "j":
    print("Drīkst izsniegt grāmatu uz 2 dienām.")
elif g_v == "grāmatu" and p_g == "n":
    print("Drīkst izsniegt grāmatu personālālam uz 28 dienām un drīkst izsniekt studentam uz 14 dienām")
elif g_v == "žurnālu" and p_g == "n":
    print("Drīkst izsniegt žurnālu uz 7 dienām ikvienam")
else:
    print("Sāc n jauna.")