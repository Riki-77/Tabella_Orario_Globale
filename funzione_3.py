def Ore_Disponibili(docenti,nomedocente):
    orario=[]
    
    for i in range(len(docenti)):
        if nomedocente in docenti[i]:
            for j in range(1,len(docenti[i])):
                orario.append(docenti[i][j])
    
    cont=0
    
    for i in range(len(orario)):
        if orario[i] == " D ":
            cont+=1
    
    return (cont)
