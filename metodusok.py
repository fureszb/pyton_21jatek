#megoldás
def osszeg(lapok)-> int:
    pont: int = 0
    for i in range(10):
        pont += lapok[i]
    return pont


def eredmeny(g_lapok: [int], j_lapok: [int]):
    gpont: int = osszeg(g_lapok)
    jpont: int = osszeg(j_lapok)
    if gpont > 21:
        szoveg = "A gép vesztett!"
    elif jpont > 21:
        szoveg = "A játékos vesztett!"
    return szoveg

def teszt_esetek():
    jatekos_vesztett_21nel_nagyobb_teszt()
    jatekos_vesztett_21nel_kevesebb_teszt()
    jatekos_vesztett_tobb_huzas_teszt()
    
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
