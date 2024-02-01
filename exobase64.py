
tableB64 = []

def InitialiserTable():
    for i in range(62):
        if(i<26):
            tableB64.append(chr(ord('A') + i))
        elif(i<52):
            tableB64.append(chr(ord('a')+ i-26))
        else:
            tableB64.append(i-52)
    tableB64.append( '+')
    tableB64.append("/")
        
    print(tableB64)
    
    
def AfficherBinaire(entier, nbBits):
    for i in range(i, nbBits): 
        print("%d",(entier >> (nbBits-i-1))&0x01)
        
def AfficherTable():
    for i in range(64):
        print("%.2d : ",i)
        AfficherBinaire(i,6)
        print("\t%c\t", tableB64[i])
        if((i+1)%4==0): print("\n")

def Code3octetBase64(code,donnee):
    nb24bits = (donnee[0]<<16) + (donnee[1]<<8) + donnee[2]
    AfficherBinaire(nb24bits)
    print("\n") 
    code[4] = 0
    code[3] = tableB64[nb24bits&0x3f]
    nb24bits >>= 6
    code[2] = tableB64[nb24bits&0x3f]
    nb24bits >>= 6
    code[1] = tableB64[nb24bits&0x3f]
    nb24bits >>= 6
    code[1] = tableB64[nb24bits&0x3f]

def codeNoctetsB64(code,donnee,nbOctetsDonnees):
    ResteEnf12Seq = (nbOctetsDonnees*8)%24
    print("reste en fin de sequence : %d bits\n", ResteEnf12Seq)
    if ResteEnf12Seq==16:
        donnee[nbOctetsDonnees+1] = 0
          
        
