#megoldás
def Glapok_lista():
    glapjai = []
    gpont = 0
    for i in range(10):
        gpont+= glapjai[i]
    return gpont
def Jlapok_lista():
    jlapjai = []
    jpont = 0
    for i in range(10):
        jpont += jlapjai[i]
    return jpont

def eredmeny(gpont, jpont):
    if gpont> 21:
        print("A gép vesztett!")
    elif jpont > 21:
        print("A játékos vesztett!")
    #tesztesetek
