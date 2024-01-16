pasa = int(input("Ievadiet cik pasažieri kāps taksī? (max: 4 pasažieri) :"))

if pasa <= 0 or pasa > 4:
    print("error - (ievadiet pasažieru skaitu no 1-4)")
else:
    h = int(input("Īevadiet tagadējo stundu skaitu veselā skaitlī.(15:00 kā 15 vai 06:00 kā 6) :"))
    if h<0 or h > 24:
        print("error- (ievadiet veselu skaitni no 0-24)")
    elif h>=6 and h<22:
        print("Dienas brauciens un jāmaksā: 0,57$ pa 1 km")# "$"zīme domāta kā eiro zīme !!!!!!
        km_cen = 0.57
        viet = input("Vai taksis ir redzams stāvietā? (j/n) :")
        if viet == "n":
            print("Jāmaksā 3,45$(gan pa nolīgšanu, gan par izsaukšanu)")# "$"zīme domāta kā eiro zīme !!!!!!
            noligsana = int(1.25)
            izsauksana = int(2.20)
           
        elif viet == "j":
            print("Jāmaksā 1,25$(tikkai pa nolīgšanu")# "$"zīme domāta kā eiro zīme !!!!!!
            noligsana = int(1.25)
            izsauksana = int(0)
           
        else:
            print("error -(ievadiet(j vai n)")
        g_laiks = int(input("Cik ilgi pasažieri grib lai taksis gaida? (ja ievada 0 tad nav gaidīšanas laiks)"))
        #g_laiks pajautā cik/vai grib lai taksis pagaida min ceļa laikā)
        if g_laiks > 0:
            print("Pasažieri grib lai taksis pagaida",g_laiks,"min.")
            cen_min = g_laiks*0.13#apreiķina cik jāmaksā par izvēlētajajām min
        else:
            print("pasažieri negrib lai taksis pagaida")
            cen_min = 0
        km = int(input("Cik km ir jābrauc līdz galamērķim? :"))#cik km jābrauc
        cen_pa_km = km*km_cen
        print("Kōpā par iekāpšanu un braicienu un pa gaidītajām min pasažieriem ")
        rez = cen_pa_km + cen_min
        km = int(input("Cik km ir jābrauc līdz galamērķim? :"))#cik km jābrauc
        cen_pa_km = km*km_cen
        rez = cen_pa_km + cen_min + noligsana + izsauksana
        print("Par ",km," ceļu jāmaksā :",cen_pa_km)
        print("Par",g_laiks," min ceļā gaidītais laikā jāmaksā :",cen_min)
        print("Par nolīgšanu jāmaksā :",noligsana)
        print("Par izsaukšanu jāmaksā :",izsauksana)
        print("Par visu kopā jāmaksā :",rez)




    else:
        print("Nakts brauciens un jāmaksā: 0,67$ pa 1 km")# "$"zīme domāta kā eiro zīme !!!!!!
        km_cen = 0.67
        viet = input("Vai taksis ir redzams stāvietā? (j/n) :")
        if viet == "n":
            izsauksana = int(2.20)
            noligsana = int(1.25)
            print("Jāmaksā 3,45$(gan pa nolīgšanu, gan par izsaukšanu)")# "$"zīme domāta kā eiro zīme !!!!!!
        elif viet == "j":
            noligsana = int(1.25)
            izsauksana = int(0)
            print("Jāmaksā 1,25$(tikkai pa nolīgšanu)")# "$"zīme domāta kā eiro zīme !!!!!!
        else:
            print("error -(ievadiet(j vai n)")
        g_laiks = int(input("Cik ilgi pasažieri grib lai taksis gaida? (ja ievada 0 tad nav gaidīšanas laiks)"))
        #g_laiks pajautā cik/vai grib lai taksis pagaida min ceļa laikā)
        if g_laiks > 0:
            print("Pasažieri grib lai taksis pagaida",g_laiks,"min.")
            cen_min = g_laiks*0.13#apreiķina cik jāmaksā par izvēlētajajām min
        else:
            print("pasažieri negrib lai taksis pagaida")
            cen_min = 0
        km = int(input("Cik km ir jābrauc līdz galamērķim? :"))#cik km jābrauc
        cen_pa_km = km*km_cen
        rez = cen_pa_km + cen_min + noligsana + izsauksana
        print("Par ",km," ceļu jāmaksā :",cen_pa_km)
        print("Par",g_laiks," min ceļā gaidītais laikā jāmaksā :",cen_min)
        print("Par nolīgšanu jāmaksā :",noligsana)
        print("Par izsaukšanu jāmaksā :",izsauksana)
        print("Par visu kopā jāmaksā :",rez)


        