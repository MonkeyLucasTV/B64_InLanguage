tableB64 = []

def InitialiserTable():
    for i in range(62):
        if(i<26):
            tableB64.append(chr(ord('A') + i))
        elif(i<52):
            tableB64.append(chr(ord('a')+ i-26))
        else:
            tableB64.append(i-52)
    tableB64.append('+')
    tableB64.append("/")
        
    print(tableB64)


cacou = ["sad","tue"]



tableau = []



lettres = input("Vos lettres : ")
print(lettres)



for i in range(0, len(lettres), 3):
    combinaison = lettres[i:i+3]
    tableau.append(combinaison)


print(tableau[0])


def CodageEnB64(Les3Lettres):
    Decoupage = []

    for Letre in Les3Lettres:
        Decoupage.append(Letre)
    
    caracBin1 = ord(Decoupage[0])
    caracBin2 = ord(Decoupage[1])
    caracBin3 = ord(Decoupage[2])

    print(caracBin1)

    print(caracBin2, caracBin3)

    carac1_B64 = caracBin1 >> 2
    carac2_B64 = str((caracBin1 & 0x03)) + str(Normalisation((caracBin2 >> 4), 4))                        
    carac3_B64 =  str(caracBin2 & 0x0F) + str(Normalisation((caracBin3 >> 6), 2))
    carac4_B64 = caracBin3 & 0x3F

    carac2_B64 = int(carac2_B64, 2)
    carac3_B64 = int(carac3_B64, 2)
    
    print("Le 1", carac1_B64)      
    print("Le 2", carac2_B64)
    print("Le 3", carac3_B64)
    print("Le 4", carac4_B64)


    lettres_B64 = []
    
    lettres_B64.append( tableB64[carac1_B64])
    lettres_B64.append( tableB64[carac2_B64])
    lettres_B64.append( tableB64[carac3_B64])
    lettres_B64.append( tableB64[carac4_B64])

    print(lettres_B64)
    
def Normalisation(entier, longueur):
    entierbin = bin(entier)[2:]
    long = len(entierbin)
    entierFinal = "0"*(longueur-long) + entierbin
    print(entierFinal)
    return entierFinal 
    
    


InitialiserTable()
CodageEnB64(tableau[0])
