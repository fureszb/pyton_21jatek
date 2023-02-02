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
    else:
        if gpont > 21:
            szoveg = "A gép vesztett!"
        if jpont > 21:
            szoveg = "A játékos vesztett!"
        if jpont > 21 and gpont >21:
            szoveg= "Döntetlen, a Ház nyert"
    return szoveg

def teszt_esetek():
    jatekos_vesztett_21nel_nagyobb_teszt()
    jatekos_vesztett_21nel_kevesebb_teszt()
    jatekos_vesztett_tobb_huzas_teszt()

    gep_vesztett_21nel_nagyobb_teszt()
    gep_vesztett_21nel_kevesebb_teszt()
    gep_vesztett_tobb_huzas_teszt()

    dontetlen_teszt()

def jatekos_vesztett_21nel_nagyobb_teszt():
    jlapok = [10,9,3]
    glapok = [10,9]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos '21-nél több' teszt sikeres")
    else:
        print("A játékos '21-nél több' teszt megbukott")
    
def jatekos_vesztett_21nel_kevesebb_teszt():
    jlapok = [10, 9, 1]
    glapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos '21-nél kevesebb' teszt sikeres")
    else:
        print("A játékos '21-nél kevesebb' teszt megbukott")

def jatekos_vesztett_tobb_huzas_teszt():
    jlapok = [10, 9, 1, 1]
    glapok = [10, 9, 2]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A játékos 'több húzás' teszt sikeres")
    else:
        print("A játékos 'több húzás' teszt megbukott")


def gep_vesztett_21nel_nagyobb_teszt():
    jlapok = [10,9]
    glapok = [10,9,3]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép '21-nél több' teszt sikeres")
    else:
        print("A gép '21-nél több' teszt megbukott")

def gep_vesztett_21nel_kevesebb_teszt():
    jlapok = [10, 9, 2]
    glapok = [10, 9, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép '21-nél kevesebb' teszt sikeres")
    else:
        print("A gép '21-nél kevesebb' teszt megbukott")

def gep_vesztett_tobb_huzas_teszt():
    jlapok = [10, 9, 2]
    glapok = [10, 9, 1, 1]
    vart_eredmeny = "A gép vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("A gép 'több húzás' teszt sikeres")
    else:
        print("A gép 'több húzás' teszt megbukott")

def dontetlen_teszt():
    jatekos_lapok = [5,8]
    gep_lapok = [8,5]
    vart_eredmeny = "Döntetlen, osztoztok a nyereségen"
    kapott_eredmeny = eredmeny(jatekos_lapok,gep_lapok)
    if kapott_eredmeny == vart_eredmeny:
        print("A 'döntetlen' teszt sikeres")
    else:
        print("A 'döntetlen' teszt megbukott")



