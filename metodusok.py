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
    jatekos_vesztett_teszt()
    
def jatekos_vesztett_teszt():
    jlapok = [10,9,3]
    glapok = [10,9]
    vart_eredmeny = "A játékos vesztett!"
    kapott_eredmeny = eredmeny(jlapok, glapok)
    if vart_eredmeny == kapott_eredmeny:
        print("teszt sikeres")
    else: 
        print("Teszt megbukott")
    

