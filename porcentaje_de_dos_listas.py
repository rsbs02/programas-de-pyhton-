#Esta función nos ayuda  a saber el porcentaje de dos listas con el mismo número de índice .
listao = [14597,14598,14642] 
listar = [14599,14600,14644]

def porcentajes(lista1,lista2):
    porcentaje = []
    j=0
    for i in range(0,len(lista1)) :
        for j in range(j,len(lista2)) :
            porcentaje.append(round((lista1[i]/lista2[j])*100,2))
            j=j+1
            break
    return porcentaje

porcentajes(listao,listar)








