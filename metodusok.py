#megoldás
def osszeg(lapok)-> int:
    pont: int = 0
    for i in range(10):
        pont += lapok[i]
    return pont


def eredmeny(g_lapok: [int], j_lapok: [int]):
    gpont: int = osszeg(g_lapok)
    jpont: int = osszeg(j_lapok)
    jdb= len(j_lapok)
    gdb = len(g_lapok)
    if(jpont <= 21 and gpont <= 21):
        if jpont>gpont:
            szoveg = "Játékos nyert"
        elif gpont>jpont:
            szoveg = "gép nyert"
        elif gpont == jpont:
            if jdb < gdb:
                szoveg = "Játékos nyert"
            elif jdb > gdb:
                szoveg = "Gép nyert"
            else:
                szoveg = "Döntetlen, osztoztok a nyereségen"

    if gpont > 21:
        szoveg = "A gép vesztett!"
    if jpont > 21:
        szoveg = "A játékos vesztett!"
    if jpont > 21 and gpont >21:
        szoveg= "Döntetlen, a Ház nyert"
    elif gpont == 19 and len(g_lapok) > len(j_lapok):
        szoveg = "Gép nyert 19 pont több lap"
    elif jpont == 19 and len(j_lapok) > len(g_lapok):
        szoveg = "Játékos nyert 19 pont több lap"
    elif jpont == 19 and len(j_lapok) < len(g_lapok):
        szoveg = "Játékos nyert 19 pont de kevesebb lap"
    elif gpont == 19 and len(g_lapok) < len(j_lapok):
        szoveg = "Gép nyert 19 pont kevesebb lap"
    elif gpont == 19 and len(g_lapok) > len(j_lapok):
        szoveg = "Több lap 19 pont gép vesztett"
    elif gpont == 19 and len(g_lapok) < len(j_lapok):
        szoveg = "Kevesebb lap 19 pont gép vesztett"
    elif jpont == 19 and len(j_lapok) > len(g_lapok):
        szoveg = "Több lap 19 pont játékos vesztett"
    elif jpont == 19 and len(j_lapok) < len(g_lapok):
        szoveg = "Kevesebb lap 19 pont játékos vesztett"
    return szoveg

def teszt_esetek():
    jatekos_vesztett_21nel_nagyobb_teszt()
    jatekos_vesztett_21nel_kevesebb_teszt()
    jatekos_vesztett_tobb_huzas_teszt()
    jatekos_19_tobb_lap()
    jatekos_19_kevesebb_lap()

    gep_vesztett_21nel_nagyobb_teszt()
    gep_vesztett_21nel_kevesebb_teszt()
    gep_vesztett_tobb_huzas_teszt()
    gep_19_tobb_lap()
    gep_19_kevesebb_lap()

    dontetlen_uaLapok_teszt()
    dontetlen_tobb21()

def jatekos_vesztett_21nel_nagyobb_teszt():
    j_lapok = [10,9,3]
    g_lapok = [10,9]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos '21-nél több' teszt sikeres")
    else:
        print("A játékos '21-nél több' teszt megbukott")
    
def jatekos_vesztett_21nel_kevesebb_teszt():
    j_lapok = [10, 9, 1]
    g_lapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos '21-nél kevesebb' teszt sikeres")
    else:
        print("A játékos '21-nél kevesebb' teszt megbukott")

def jatekos_vesztett_tobb_huzas_teszt():
    j_lapok = [10, 9, 1, 1]
    g_lapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 'több húzás' teszt sikeres")
    else:
        print("A játékos 'több húzás' teszt megbukott")


def gep_vesztett_21nel_nagyobb_teszt():
    j_lapok = [10,9]
    g_lapok = [10,9,3]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép '21-nél több' teszt sikeres")
    else:
        print("A gép '21-nél több' teszt megbukott")

def gep_vesztett_21nel_kevesebb_teszt():
    j_lapok = [10, 9, 2]
    g_lapok = [10, 9, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép '21-nél kevesebb' teszt sikeres")
    else:
        print("A gép '21-nél kevesebb' teszt megbukott")

def gep_vesztett_tobb_huzas_teszt():
    j_lapok = [10, 9, 2]
    g_lapok = [10, 9, 1, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(j_lapok, g_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép 'több húzás' teszt sikeres")
    else:
        print("A gép 'több húzás' teszt megbukott")

def jatekos_19_tobb_lap():
    j_lapok = [10, 6, 3]
    g_lapok = [10, 6]
    vart_eredmeny = "Több lap 19 pont játékos vesztett"
    kapott_eredmeny = eredmeny(g_lapok, j_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("Több lap 19 pont játékos vesztett teszt sikeres")
    else:
        print("Több lap 19 pont játékos vesztett teszt megbukott")

def jatekos_19_kevesebb_lap():
    j_lapok = [11, 8]
    g_lapok = [10, 6, 3]
    vart_eredmeny = "Kevesebb lap 19 pont játékos vesztett"
    kapott_eredmeny = eredmeny(g_lapok, j_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("Kevesebb lap 19 pont játékos vesztett teszt sikeres")
    else:
        print("Kevesebb lap 19 pont játékos vesztett teszt megbukott")

def gep_19_tobb_lap():
    j_lapok = [11, 2]
    g_lapok = [10, 6, 3]
    vart_eredmeny = "Több lap 19 pont gép vesztett"
    kapott_eredmeny = eredmeny(g_lapok, j_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("Több lap 19 pont gép vesztett teszt sikeres")
    else:
        print("Több lap 19 pont gép vesztett teszt megbukott")
def gep_19_kevesebb_lap():
    j_lapok = [11, 2]
    g_lapok = [11, 8]
    vart_eredmeny = "Kevesebb lap 19 pont gép vesztett"
    kapott_eredmeny = eredmeny(g_lapok, j_lapok)
    if vart_eredmeny == kapott_eredmeny:
        print("Kevesebb lap 19 pont gép vesztett teszt sikeres")
    else:
        print("Kevesebb lap 19 pont gép vesztett teszt megbukott")

def dontetlen_uaLapok_teszt():
    jatekos_lapok = [5,8]
    gep_lapok = [8,5]
    vart_eredmeny = "Döntetlen, osztoztok a nyereségen"
    kapott_eredmeny = eredmeny(jatekos_lapok,gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("A 'döntetlen ua. olyan' teszt sikeres")
    else:
        print("A 'döntetlen ua. olyan' teszt megbukott")
def dontetlen_tobb21():
    gep = [11, 12, 6]
    jatekos = [11, 12, 5]
    vart_eredmeny = "Döntetlen, a Ház nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("Mindenkinek több 21-nél teszt sikeres")
    else:
        print("Mindenkinek több 21-nél teszt megbukott")





