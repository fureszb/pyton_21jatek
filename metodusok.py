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
        print("A gép vesztett!")
    elif jpont > 21:
        print("A játékos vesztett!")
    #tesztesetek

