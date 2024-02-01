
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
    
    
        
        
