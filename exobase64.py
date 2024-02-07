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


    print(caracBin2, caracBin3)

    carac1_B64 = bin(int(caracBin1) >> 2) 
    carac2_B64 = ((bin(int(caracBin1) & 0x02))[2:] + (bin(int(caracBin2) >> 4))[2:])   
    carac3_B64 = (bin(int((f'{caracBin2:04b}'), 2) & 0x0F)[2:] + bin(int(f'0b{caracBin3:08b}', 2) >> 6)[2:])
    carac4_B64 = bin((int(caracBin3) & 0x3F))


    print(bin(caracBin3))
    print( int(f'{caracBin3:08b}', 2) >> 6 ) 

    print(carac3_B64)



    # lettres_B64 = []
    
    # lettres_B64.append( tableB64[int(carac1_B64, 0)])
    # lettres_B64.append( tableB64[int(carac2_B64, 0)])
    # lettres_B64.append( tableB64[int(carac3_B64, 0)])
    # lettres_B64.append( tableB64[int(carac4_B64, 0)])

    # print(lettres_B64)
    

InitialiserTable()
CodageEnB64(tableau[0])
